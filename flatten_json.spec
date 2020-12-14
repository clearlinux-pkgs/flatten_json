#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : flatten_json
Version  : 0.1.7
Release  : 12
URL      : https://files.pythonhosted.org/packages/49/e1/02d1f28a0276c0018c5dbe09929b12953c7c6a6d6b887686492ce53278a1/flatten_json-0.1.7.tar.gz
Source0  : https://files.pythonhosted.org/packages/49/e1/02d1f28a0276c0018c5dbe09929b12953c7c6a6d6b887686492ce53278a1/flatten_json-0.1.7.tar.gz
Summary  : Flatten JSON objects
Group    : Development/Tools
License  : MIT
Requires: flatten_json-bin = %{version}-%{release}
Requires: flatten_json-python = %{version}-%{release}
Requires: flatten_json-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3

%description
[![Build Status](https://travis-ci.org/amirziai/flatten.svg?branch=master)](https://travis-ci.org/amirziai/flatten) [![PyPI version](https://badge.fury.io/py/flatten_json.svg)](https://badge.fury.io/py/flatten_json) [![Codacy Badge](https://api.codacy.com/project/badge/Coverage/7ae779ec4e99462f907c5afecfd5de48)](https://www.codacy.com/app/amirziai/flatten?utm_source=github.com&utm_medium=referral&utm_content=amirziai/flatten&utm_campaign=Badge_Coverage)

%package bin
Summary: bin components for the flatten_json package.
Group: Binaries

%description bin
bin components for the flatten_json package.


%package python
Summary: python components for the flatten_json package.
Group: Default
Requires: flatten_json-python3 = %{version}-%{release}

%description python
python components for the flatten_json package.


%package python3
Summary: python3 components for the flatten_json package.
Group: Default
Requires: python3-core
Provides: pypi(flatten_json)

%description python3
python3 components for the flatten_json package.


%prep
%setup -q -n flatten_json-0.1.7
cd %{_builddir}/flatten_json-0.1.7

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1595972135
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=4 "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=4 "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=4 "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/flatten_json

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
