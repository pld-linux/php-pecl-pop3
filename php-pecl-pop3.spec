%define		_modname	pop3
%define		_status		stable

Summary:	POP3 Client Library
Summary(pl):	Biblioteka klienta POP3
Name:		php-pecl-%{_modname}
Version:	1.0.2
Release:	1
License:	PHP
Group:		Development/Languages/PHP
Source0:	http://pecl.php.net/get/%{_modname}-%{version}.tgz
# Source0-md5:	cdbe4f41aa37bcf45e651d5568f3a8d2
URL:		http://pecl.php.net/package/POP3/
BuildRequires:	libspopc-devel
BuildRequires:	libtool
BuildRequires:	php-devel >= 3:5.0.0
Requires:	php-common
Obsoletes:	php-pear-%{_modname}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_sysconfdir	/etc/php
%define		extensionsdir	%{_libdir}/php

%description
The POP3 extension makes it possible for a PHP script to connect to
and interact with a POP3 mail server. Based on libspopc
(http://brouits.free.fr/libspopc/), it is built for performance and
ease of use.

In PECL status of this package is: %{_status}.

%description -l pl
Rozszerzenie POP3 umo¿liwia skryptowi PHP pod³±czenie i wspó³pracê z
serwerem POP3. Biblioteka bazuj±ca na libspopc
(http://brouits.free.fr/libspopc/), stworzona zosta³a z my¶l± o
wydajno¶ci i ³atwo¶ci u¿ycia.

To rozszerzenie ma w PECL status: %{_status}.

%prep
%setup -q -c

%build
cd %{_modname}-%{version}
phpize
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{extensionsdir}

install %{_modname}-%{version}/modules/%{_modname}.so $RPM_BUILD_ROOT%{extensionsdir}

%clean
rm -rf $RPM_BUILD_ROOT

%post
%{_sbindir}/php-module-install install %{_modname} %{_sysconfdir}/php-cgi.ini

%preun
if [ "$1" = "0" ]; then
	%{_sbindir}/php-module-install remove %{_modname} %{_sysconfdir}/php-cgi.ini
fi

%files
%defattr(644,root,root,755)
%doc %{_modname}-%{version}/{CREDITS,EXPERIMENTAL}
%attr(755,root,root) %{extensionsdir}/%{_modname}.so
