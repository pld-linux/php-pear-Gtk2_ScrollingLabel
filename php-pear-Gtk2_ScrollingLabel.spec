%include	/usr/lib/rpm/macros.php
%define		_class		Gtk2
%define		_subclass	ScrollingLabel
%define		_status		beta
%define		_pearname	Gtk2_ScrollingLabel

Summary:	%{_pearname} - a scrolling label for PHP-Gtk2
Summary(pl):	%{_pearname} - przewijaj±ca siê etykieta (scrolling label) dla PHP-Gtk2
Name:		php-pear-%{_pearname}
Version:	0.4.1
Release:	1
License:	LGPL Version 2.1
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
# Source0-md5:	928f6445b8b096aa2993d5bce0af806a
URL:		http://pear.php.net/package/Gtk2_ScrollingLabel/
BuildRequires:	php-pear-PEAR
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
BuildRequires:	rpmbuild(macros) >= 1.300
Requires:	php-gtk
Requires:	php-pear
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A scrolling Gtk label for PHP-Gtk2. This class provides a simple, easy
to understand API for setting up and controlling the label. It allows
for the ability to scroll in either direction, start and stop the
scroll, pause and unpause the scroll, get and set the text, and set
display properites of the text.

In PEAR status of this package is: %{_status}.

%description -l pl
Przewijaj±ca siê etykieta (scrolling label) dla Gtk2. Ta klasa
dostarcza prostego, ³atwego do zrozumienia API do ustawiania i
kontrolowania takiej etykiety. Pozwala na ustawienie przewijania w
dowolnym kierunku, uruchamiania lub zatrzymywania przewijania,
ustawienie i pobieranie tekstu oraz jego w³a¶ciwo¶ci.

Ta klasa ma w PEAR status: %{_status}.

%prep
%pear_package_setup

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_pear_dir}
%pear_package_install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc install.log docs/%{_pearname}/example.php
%{php_pear_dir}/.registry/*.reg
%{php_pear_dir}/Gtk2/ScrollingLabel.php
