#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
%define keepstatic 1
Name     : mod_wsgi
Version  : 4.6.7
Release  : 52
URL      : https://github.com/GrahamDumpleton/mod_wsgi/archive/4.6.7/mod_wsgi-4.6.7.tar.gz
Source0  : https://github.com/GrahamDumpleton/mod_wsgi/archive/4.6.7/mod_wsgi-4.6.7.tar.gz
Summary  : Python WSGI adapter module for Apache
Group    : Development/Tools
License  : Apache-2.0
Requires: mod_wsgi-data = %{version}-%{release}
Requires: mod_wsgi-lib = %{version}-%{release}
Requires: mod_wsgi-license = %{version}-%{release}
BuildRequires : apr-dev
BuildRequires : apr-util-dev
BuildRequires : buildreq-distutils3
BuildRequires : httpd-data
BuildRequires : httpd-dev
BuildRequires : httpd-extras
BuildRequires : pluggy
BuildRequires : py-python
BuildRequires : pytest
BuildRequires : tox
BuildRequires : virtualenv
Patch1: 0001-default-WSGI-configuration-for-httpd.patch
Patch2: 0002-defaults.patch

%description
Overview
--------
The mod_wsgi package provides an Apache module that implements a WSGI
compliant interface for hosting Python based web applications on top of the
Apache web server.

%package data
Summary: data components for the mod_wsgi package.
Group: Data

%description data
data components for the mod_wsgi package.


%package lib
Summary: lib components for the mod_wsgi package.
Group: Libraries
Requires: mod_wsgi-data = %{version}-%{release}
Requires: mod_wsgi-license = %{version}-%{release}

%description lib
lib components for the mod_wsgi package.


%package license
Summary: license components for the mod_wsgi package.
Group: Default

%description license
license components for the mod_wsgi package.


%prep
%setup -q -n mod_wsgi-4.6.7
%patch1 -p1
%patch2 -p1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1560880109
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -falign-functions=32 -ffat-lto-objects -flto=4 -fno-math-errno -fno-semantic-interposition -fno-trapping-math "
export FCFLAGS="$CFLAGS -O3 -falign-functions=32 -ffat-lto-objects -flto=4 -fno-math-errno -fno-semantic-interposition -fno-trapping-math "
export FFLAGS="$CFLAGS -O3 -falign-functions=32 -ffat-lto-objects -flto=4 -fno-math-errno -fno-semantic-interposition -fno-trapping-math "
export CXXFLAGS="$CXXFLAGS -O3 -falign-functions=32 -ffat-lto-objects -flto=4 -fno-math-errno -fno-semantic-interposition -fno-trapping-math "
%configure
make  %{?_smp_mflags} DEFAULTFLAGS="$CFLAGS"

%install
export SOURCE_DATE_EPOCH=1560880109
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/mod_wsgi
cp LICENSE %{buildroot}/usr/share/package-licenses/mod_wsgi/LICENSE
%make_install
## install_append content
install -m 0755 -d %{buildroot}/usr/share/defaults/httpd/conf.modules.d/
install -p -D -m 644 etc/httpd/conf.d/wsgi.conf  %{buildroot}/usr/share/defaults/httpd/conf.modules.d/
## install_append end

%files
%defattr(-,root,root,-)

%files data
%defattr(-,root,root,-)
/usr/share/defaults/httpd/conf.modules.d/wsgi.conf

%files lib
%defattr(-,root,root,-)
/usr/lib/httpd/modules/mod_wsgi.so

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/mod_wsgi/LICENSE
