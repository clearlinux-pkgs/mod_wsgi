#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
%define keepstatic 1
Name     : mod_wsgi
Version  : 4.5.20
Release  : 36
URL      : https://github.com/GrahamDumpleton/mod_wsgi/archive/4.5.20.tar.gz
Source0  : https://github.com/GrahamDumpleton/mod_wsgi/archive/4.5.20.tar.gz
Summary  : No detailed summary available
Group    : Development/Tools
License  : Apache-2.0
Requires: mod_wsgi-lib
Requires: mod_wsgi-data
BuildRequires : apr-dev
BuildRequires : apr-util-dev
BuildRequires : httpd-data
BuildRequires : httpd-dev
BuildRequires : httpd-extras
BuildRequires : pbr
BuildRequires : pip
BuildRequires : pluggy
BuildRequires : py-python
BuildRequires : pytest
BuildRequires : python-dev
BuildRequires : python3-dev
BuildRequires : setuptools
BuildRequires : tox
BuildRequires : virtualenv
Patch1: 0001-default-WSGI-configuration-for-httpd.patch

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
Requires: mod_wsgi-data

%description lib
lib components for the mod_wsgi package.


%prep
%setup -q -n mod_wsgi-4.5.20
%patch1 -p1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1507011491
export CFLAGS="$CFLAGS -O3 -falign-functions=32 -fno-common -fno-math-errno -fno-semantic-interposition -fno-trapping-math "
export FCFLAGS="$CFLAGS -O3 -falign-functions=32 -fno-common -fno-math-errno -fno-semantic-interposition -fno-trapping-math "
export FFLAGS="$CFLAGS -O3 -falign-functions=32 -fno-common -fno-math-errno -fno-semantic-interposition -fno-trapping-math "
export CXXFLAGS="$CXXFLAGS -O3 -falign-functions=32 -fno-common -fno-math-errno -fno-semantic-interposition -fno-trapping-math "
%configure  --with-python=/usr/bin/python3
make V=1  %{?_smp_mflags}

%install
export SOURCE_DATE_EPOCH=1507011491
rm -rf %{buildroot}
%make_install
## make_install_append content
install -m 0755 -d %{buildroot}/usr/share/defaults/httpd/conf.modules.d/
install -p -D -m 644 etc/httpd/conf.d/wsgi.conf  %{buildroot}/usr/share/defaults/httpd/conf.modules.d/
## make_install_append end

%files
%defattr(-,root,root,-)

%files data
%defattr(-,root,root,-)
/usr/share/defaults/httpd/conf.modules.d/wsgi.conf

%files lib
%defattr(-,root,root,-)
/usr/lib/httpd/modules/mod_wsgi.so
