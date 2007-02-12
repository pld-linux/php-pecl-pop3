%define		_modname	pop3
%define		_status		stable
Summary:	POP3 Client Library
Summary(pl.UTF-8):   Biblioteka klienta POP3
Name:		php-pecl-%{_modname}
Version:	1.0.2
Release:	7
License:	PHP
Group:		Development/Languages/PHP
Source0:	http://pecl.php.net/get/%{_modname}-%{version}.tgz
# Source0-md5:	cdbe4f41aa37bcf45e651d5568f3a8d2
Patch0:		%{name}-php51.patch
URL:		http://pecl.php.net/package/POP3/
BuildRequires:	libspopc-devel
BuildRequires:	php-devel >= 3:5.0.0
BuildRequires:	rpmbuild(macros) >= 1.344
%{?requires_php_extension}
Requires:	php-common >= 4:5.0.4
Obsoletes:	php-pear-%{_modname}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The POP3 extension makes it possible for a PHP script to connect to
and interact with a POP3 mail server. Based on libspopc
(http://brouits.free.fr/libspopc/), it is built for performance and
ease of use.

In PECL status of this package is: %{_status}.

%description -l pl.UTF-8
Rozszerzenie POP3 umożliwia skryptowi PHP podłączenie i współpracę z
serwerem POP3. Biblioteka bazująca na libspopc
(http://brouits.free.fr/libspopc/), stworzona została z myślą o
wydajności i łatwości użycia.

To rozszerzenie ma w PECL status: %{_status}.

%prep
%setup -q -c
%patch0 -p1

%build
cd %{_modname}-%{version}
phpize
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{php_sysconfdir}/conf.d,%{php_extensiondir}}

install %{_modname}-%{version}/modules/%{_modname}.so $RPM_BUILD_ROOT%{php_extensiondir}
cat <<'EOF' > $RPM_BUILD_ROOT%{php_sysconfdir}/conf.d/%{_modname}.ini
; Enable %{_modname} extension module
extension=%{_modname}.so
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
%doc %{_modname}-%{version}/{CREDITS,EXPERIMENTAL}
%config(noreplace) %verify(not md5 mtime size) %{php_sysconfdir}/conf.d/%{_modname}.ini
%attr(755,root,root) %{php_extensiondir}/%{_modname}.so
