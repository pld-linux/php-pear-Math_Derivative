%include	/usr/lib/rpm/macros.php
%define		_class		Math
%define		_subclass	Derivative
%define		_status		beta
%define		_pearname	Math_Derivative

Summary:	%{_pearname} - Calculate the derivative of a mathematical expression
Summary(pl):	%{_pearname} - Obliczanie pochodnej wyra¿enia matematycznego
Name:		php-pear-%{_pearname}
Version:	0.1.0
Release:	1
License:	PHP License
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
# Source0-md5:	a44c1a91dc4c19a8f6e23db9fd5c9da8
URL:		http://pear.php.net/package/Math_Derivative/
BuildRequires:	php-pear-PEAR
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
Requires:	php-pear
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This package allows you to calculate the derivative of an expression
stored in a string.

In PEAR status of this package is: %{_status}.

%description -l pl
Klasa ta pozwala na obliczenie pochodnej wyra¿enia przechowywanego w
³añcuchu znaków.

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
%{php_pear_dir}/.registry/*.reg
%{php_pear_dir}/Math/Derivative.php
