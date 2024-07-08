%define _disable_ld_no_undefined 1
%define _disable_lto 1

Summary:	Utilities for working with md5sum implanted in ISO images
Name:		isomd5sum
Version:	1.2.5
Release:	1
License:	GPLv2+
Group:		Archiving/Cd burning
URL:		http://git.fedorahosted.org/git/?p=isomd5sum.git;a=summary
Source0:	https://github.com/rhinstaller/isomd5sum/archive/%{version}.tar.gz
BuildRequires:	pkgconfig(popt)
BuildRequires:	pkgconfig(python)

%description
The isomd5sum package contains utilities for implanting and verifying
an md5sum implanted into an ISO9660 image.

%package devel
Summary:	Development headers and library for using isomd5sum
Group:		Development/C
Requires:	%{name} = %{version}

%description devel
This contains header files and a library for working with the isomd5sum
implanting and checking.

%package -n python-isomd5sum
Summary:	Python bindings for isomd5sum
Group:		Development/Python

%description -n python-isomd5sum
Python bindings for isomd5sum.

%prep
%autosetup -p1

%build
export CFLAGS="%{optflags} -Wno-strict-aliasing -Qunused-arguments -fuse-ld=bfd"
export CXXFLAGS="%{optflags} -Qunused-arguments"

PYTHON=%{__python} %make_build checkisomd5 implantisomd5 pyisomd5sum.so

%install
PYTHON=%{__python} %make_install install-bin install-devel install-python

%files
%doc COPYING
%{_bindir}/implantisomd5
%{_bindir}/checkisomd5
%{_mandir}/man*/*

%files devel
%{_datadir}/pkgconfig/isomd5sum.pc
%{_includedir}/*.h
%{_libdir}/*.a

%files -n python-isomd5sum
%{python_sitearch}/pyisomd5sum.so
