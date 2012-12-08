Summary:	Utilities for working with md5sum implanted in ISO images
Name:		isomd5sum
Version:	1.0.7
Release:	%mkrel 1
License:	GPLv2+
Group:		Archiving/Cd burning
URL:		http://git.fedorahosted.org/git/?p=isomd5sum.git;a=summary
Source0:	http://fedorahosted.org/releases/i/s/isomd5sum/%{name}-%{version}.tar.bz2
Patch0:		isomd5sum-1.0.7-makefile.patch
Patch1:		isomd5sum-1.0.7-unused.patch
Patch2:		isomd5sum-1.0.7-nowerror.patch
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root
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


%prep
%setup -q
%apply_patches

%build
make checkisomd5 implantisomd5

%install
rm -rf $RPM_BUILD_ROOT
make DESTDIR=$RPM_BUILD_ROOT install-bin install-devel

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%doc COPYING
%_bindir/implantisomd5
%_bindir/checkisomd5
%_mandir/man*/*

%files devel
%defattr(-,root,root,-)
%_includedir/*.h
%_libdir/*.a



%changelog
* Fri Apr 15 2011 Eugeni Dodonov <eugeni@mandriva.com> 1.0.7-1mdv2011.0
+ Revision: 653214
- New version 1.0.7.
  P0: compile with make
  P1: declare variable as unused
  P2: disable -Werror

  + Oden Eriksson <oeriksson@mandriva.com>
    - the mass rebuild of 2010.1 packages

* Fri Feb 19 2010 Sandro Cazzaniga <kharec@mandriva.org> 1.0.5-2mdv2010.1
+ Revision: 508385
- fix rpmlint warning on spec (mixed of spaces and tabs)

* Sun Dec 20 2009 Thierry Vignaud <tv@mandriva.org> 1.0.5-1mdv2010.1
+ Revision: 480256
- import isomd5sum


* Sun Dec 20 2009 Thierry Vignaud <tvignaud@mandriva.com> 1.0.5-1mdv2010.1
- initial release
