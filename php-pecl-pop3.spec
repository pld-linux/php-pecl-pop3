%define		_modname	pop3
%define		_status		alpha

Summary:	%{_modname} Client Library
Summary(pl):	Biblioteka klienta %{_modname} 
Name:		php-pecl-%{_modname}
Version:	0.1
Release:	1
License:	PHP
Group:		Development/Languages/PHP
Source0:	http://pecl.php.net/get/%{_modname}-%{version}.tgz
# Source0-md5:	c0f9946f2d6adefbf3f5908444387b61
URL:		http://pecl.php.net/package/POP3/
BuildRequires:	libspopc-devel
BuildRequires:	libtool
BuildRequires:	php-devel
Requires:	php-common
Obsoletes:	php-pear-%{_modname}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_sysconfdir	/etc/php
%define		extensionsdir	%{_libdir}/php

%description
The POP3 extension makes it possible for a PHP
script to connect to and interact with a POP3 mail server.
Based on libspopc (http://brouits.free.fr/libspopc/), it is
built for performance and ease of use.

This extension has in PEAR status: %{_status}.

%description -l pl
Rozszerzenie POP3 umo¿liwia skryptowi PHP pod³±czenie i wspó³pracê z
serwerem POP3. Biblioteka bazuj±ca na libspopc
(http://brouits.free.fr/libspopc/), stworzona zosta³a z my¶l± o
wydajno¶ci i ³atwo¶ci u¿ycia.

To rozszerzenie ma w PEAR status: %{_status}.

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
