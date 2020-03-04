Name: product-manifest
Version: %{_platform_product_release_build_id}
Release: 2%{?dist}
Summary: Product build information

License: %{_platform_licence}
Vendor:  %{_platform_vendor}

BuildArch: noarch

%description
Product build information

%prep

%install
mkdir -p %{buildroot}/etc
cat > %{buildroot}/etc/product-release <<EOF
release=%{_platform_product_release_label}
build=%{_platform_product_release_build_id}
EOF

%files
/etc/product-release

