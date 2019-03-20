Name: product-manifest
Version: 0
Release: 1%{?dist}
Summary: Product build information

License: %{_platform_licence}
Source0: %{name}-%{version}.tar.gz
Vendor:  %{_platform_vendor}

BuildArch: noarch

%description
Platform build information

%prep
%autosetup

%install
mkdir -p %{buildroot}/etc
cp product-release %{buildroot}/etc/

%files
/etc/product-release

