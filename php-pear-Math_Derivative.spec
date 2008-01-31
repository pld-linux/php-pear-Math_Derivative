%include	/usr/lib/rpm/macros.php
%define		_class		Math
%define		_subclass	Derivative
%define		_status		beta
%define		_pearname	Math_Derivative
%define		subver		RC1
%define		rel	1
Summary:	%{_pearname} - Calculate the derivative of a mathematical expression
Summary(pl.UTF-8):	%{_pearname} - Obliczanie pochodnej wyrażenia matematycznego
Name:		php-pear-%{_pearname}
Version:	1.0.0
Release:	%{subver}.%{rel}
License:	PHP License
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}%{subver}.tgz
# Source0-md5:	06503fd9916d82c4201a5557dc1d895f
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

%description -l pl.UTF-8
Klasa ta pozwala na obliczenie pochodnej wyrażenia przechowywanego w
łańcuchu znaków.

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
