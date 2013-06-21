%define		php_name	php%{?php_suffix}
%define		modname	pop3
%define		status		stable
Summary:	POP3 Client Library
Summary(pl.UTF-8):	Biblioteka klienta POP3
Name:		%{php_name}-pecl-%{modname}
Version:	1.0.2
Release:	8
License:	PHP
Group:		Development/Languages/PHP
Source0:	http://pecl.php.net/get/%{modname}-%{version}.tgz
# Source0-md5:	cdbe4f41aa37bcf45e651d5568f3a8d2
Patch0:		php-pecl-%{modname}-php51.patch
URL:		http://pecl.php.net/package/POP3/
BuildRequires:	libspopc-devel
BuildRequires:	%{php_name}-devel >= 3:5.0.0
BuildRequires:	rpmbuild(macros) >= 1.650
%{?requires_php_extension}
Requires:	php-common >= 4:5.0.4
Obsoletes:	php-pear-%{modname}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The POP3 extension makes it possible for a PHP script to connect to
and interact with a POP3 mail server. Based on libspopc
(http://brouits.free.fr/libspopc/), it is built for performance and
ease of use.

In PECL status of this package is: %{status}.

%description -l pl.UTF-8
Rozszerzenie POP3 umożliwia skryptowi PHP podłączenie i współpracę z
serwerem POP3. Biblioteka bazująca na libspopc
(http://brouits.free.fr/libspopc/), stworzona została z myślą o
wydajności i łatwości użycia.

To rozszerzenie ma w PECL status: %{status}.

%prep
%setup -qc
mv %{modname}-%{version}/* .
%patch0 -p2

%build
phpize
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{php_sysconfdir}/conf.d,%{php_extensiondir}}
install -p modules/%{modname}.so $RPM_BUILD_ROOT%{php_extensiondir}
cat <<'EOF' > $RPM_BUILD_ROOT%{php_sysconfdir}/conf.d/%{modname}.ini
; Enable %{modname} extension module
extension=%{modname}.so
EOF

%clean
rm -rf $RPM_BUILD_ROOT

%post
%php_webserver_restart

%postun
if [ "$1" = 0 ]; then
	%php_webserver_restart
fi

%files
%defattr(644,root,root,755)
%doc CREDITS EXPERIMENTAL
%config(noreplace) %verify(not md5 mtime size) %{php_sysconfdir}/conf.d/%{modname}.ini
%attr(755,root,root) %{php_extensiondir}/%{modname}.so
