Summary:	Utilities for working with md5sum implanted in ISO images
Name:		isomd5sum
Version:	1.0.10
Release:	5
License:	GPLv2+
Group:		Archiving/Cd burning
URL:		http://git.fedorahosted.org/git/?p=isomd5sum.git;a=summary
Source0:	http://fedorahosted.org/releases/i/s/isomd5sum/%{name}-%{version}.tar.bz2
BuildRequires:	popt-devel

%description
The isomd5sum package contains utilities for implanting and verifying
an md5sum implanted into an ISO9660 image.

%package devel
Summary: Development headers and library for using isomd5sum 
Group: Development/C
Requires: %{name} = %{version}

%description devel
This contains header files and a library for working with the isomd5sum
implanting and checking.

%package -n python-isomd5sum
Summary: Python bindings for isomd5sum
BuildRequires: python-devel
Group: Development/Python

%description -n python-isomd5sum
Python bindings for isomd5sum.

%prep
%setup -q

%build
export CFLAGS="%{optflags} -Wno-strict-aliasing"
make checkisomd5 implantisomd5 pyisomd5sum.so

%install
make DESTDIR=%{buildroot} install-bin install-devel install-python

%files
%doc COPYING
%_bindir/implantisomd5
%_bindir/checkisomd5
%_mandir/man*/*

%files devel
%_includedir/*.h
%_libdir/*.a

%files -n python-isomd5sum
%{python_sitearch}/pyisomd5sum.so
