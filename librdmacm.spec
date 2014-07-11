%define major 1
%define libname %mklibname rdmacm %{major}
%define devname %mklibname -d rdmacm
%define static %mklibname -s rdmacm

Name:		librdmacm
Version:	1.0.17
Release:	7
Summary:	Userspace RDMA Connection Manager
Group:		Development/Other
License:	GPL/BSD
Url:		http://www.openfabrics.org/
Source0:	http://www.openfabrics.org/downloads/librdmacm/%{name}-%{version}.tar.gz
#Source100: librdmacm.rpmlintrc
BuildRequires:	libibverbs-devel >= 1.1
BuildRequires:	autoconf

%description 
librdmacm provides a userspace RDMA Communication Managment API.

%package -n	%{devname}
Summary:	Development files for the librdmacm library
Group:		Development/Other
Requires:	%{libname} = %{version}-%{release}
Provides:	rdmacm-devel = %{version}-%{release}
Provides:	%{name}-devel = %{version}-%{release}

%description -n %{devname}
Development files for the librdmacm library.

%package -n	%{libname}
Summary:	Userspace RDMA Connection Manager
Group:		System/Libraries

%description -n %{libname}
librdmacm provides a userspace RDMA Communication Managment API.

%package utils
Summary: Examples for the librdmacm library
Group: Development/Other

%description utils
Example test programs for the librdmacm library.

%package -n	%{static}
Summary:	Static version of the librdmacm library
Group:		Development/Other
Requires:	%{devname} = %{version}-%{release}
Provides:	%{name}-static = %{version}-%{release}
Provides:	rdmacm-static-devel = %{version}-%{release}

%description -n %{static}
Static version of the librdmacm library.

%prep
%setup -q 

%build
export LDFLAGS="-lpthread"
autoreconf
%configure --enable-static
%make

%install
%makeinstall
# remove unpackaged files from the buildroot

%files -n %{libname}
%{_libdir}/librdmacm*.so.*
%{_libdir}/rsocket/librspreload.so.*

%files -n %{devname}
%doc AUTHORS COPYING ChangeLog README
%{_libdir}/lib*.so
%{_libdir}/rsocket/lib*.so
%{_includedir}/*
%{_mandir}/man3/*
%{_mandir}/man7/*

%files utils
%{_bindir}/*
%{_mandir}/man1/*

%files -n %{static}
%{_libdir}/*.a
%{_libdir}/rsocket/*.a
