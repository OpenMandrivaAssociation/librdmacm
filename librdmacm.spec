
Name:	librdmacm
Version: 1.0.16
Release: 1
Summary: Userspace RDMA Connection Manager
Group: Development/Other
License: GPL/BSD
Url: http://www.openfabrics.org/
Source: http://www.openfabrics.org/downloads/librdmacm/%{name}-%{version}.tar.gz
BuildRequires: libibverbs-devel >= 1.1 autoconf

%description 
librdmacm provides a userspace RDMA Communication Managment API.

%package devel
Summary: Development files for the librdmacm library
Group: Development/Other
provides: lib%{name}-devel = %{version}-%{release}
provides: %{name}-devel = %{version}-%{release}

%description devel
Development files for the librdmacm library.

%package utils
Summary: Examples for the librdmacm library
Group: Development/Other

%description utils
Example test programs for the librdmacm library.

%package static
Summary: Static version of the librdmacm library
Group: Development/Other
Requires: %{name}-devel = %{version}-%{release}
provides: lib%{name}-static = %{version}-%{release}
provides: %{name}-static = %{version}-%{release}

%description static
Static version of the librdmacm library.

%prep
%setup -q 

%build
export LDFLAGS="-lpthread"
autoreconf
%configure
%make

%install
%makeinstall
# remove unpackaged files from the buildroot

%clean

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files 
%defattr(-,root,root,-)
%{_libdir}/librdmacm*.so.*
%doc AUTHORS COPYING ChangeLog README

%files devel
%defattr(-,root,root)
%{_libdir}/lib*.so
%{_includedir}/*
%{_mandir}/man3/*
%{_mandir}/man7/*

%files utils
%defattr(-,root,root,-)
%{_bindir}/*
%{_mandir}/man1/*

%files static
%defattr(-,root,root,-)
%{_libdir}/*.a



%changelog
* Sun Dec 05 2010 Oden Eriksson <oeriksson@mandriva.com> 1.0.11-3mdv2011.0
+ Revision: 609776
- rebuild

* Wed Jan 27 2010 Antoine Ginies <aginies@mandriva.com> 1.0.11-2mdv2010.1
+ Revision: 497205
- bump the release
- fix typo
- the name already contains the lib prefix

* Wed Jan 27 2010 Antoine Ginies <aginies@mandriva.com> 1.0.11-1mdv2010.1
+ Revision: 497200
- fix some pb in spec file (import from fedora one)
- import librdmacm


