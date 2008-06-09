%define name jrtplib
%define version 3.7.1
%define release %mkrel 1
%define api %version
%define libname %mklibname jrtp %api
%define develname %mklibname -d jrtp

Summary: Real-time Transport Protocol library
Name: %{name}
Version: %{version}
Release: %{release}
Source0: http://research.edm.uhasselt.be/jori/jrtplib/%{name}-%{version}.tar.bz2
License: MIT
Group: System/Libraries
Url: http://research.edm.uhasselt.be/~jori/page/index.php?n=CS.Jrtplib
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires: libjthread-devel

%description
The library offers support for the Real-time Transport Protocol (RTP),
defined in RFC 3550. It makes it very easy to send and receive RTP
packets and the RTCP (RTP Control Protocol) functions are handled
entirely internally. For more detailed information you should take a
look at the documentation included in the package.

%package -n %libname
Group:System/Libraries
Summary: Real-time Transport Protocol library

%description -n %libname
The library offers support for the Real-time Transport Protocol (RTP),
defined in RFC 3550. It makes it very easy to send and receive RTP
packets and the RTCP (RTP Control Protocol) functions are handled
entirely internally. For more detailed information you should take a
look at the documentation included in the package.

%package -n %develname
Group: Development/C++
Summary: Real-time Transport Protocol library
Requires: %libname = %version
Provides: libjrtp-devel = %version-%release

%description -n %develname
The library offers support for the Real-time Transport Protocol (RTP),
defined in RFC 3550. It makes it very easy to send and receive RTP
packets and the RTCP (RTP Control Protocol) functions are handled
entirely internally. For more detailed information you should take a
look at the documentation included in the package.



%prep
%setup -q

%build
%configure2_5x
%make

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall_std

%clean
rm -rf $RPM_BUILD_ROOT

%if %mdkversion < 200900
%post -n %libname -p /sbin/ldconfig
%endif
%if %mdkversion < 200900
%postun -n %libname -p /sbin/ldconfig
%endif

%files -n %libname
%defattr(-,root,root)
%doc *.TXT
%_libdir/libjrtp-%{api}.so

%files -n %develname
%defattr(-,root,root)
%doc ChangeLog
%_includedir/jrtplib3
%_libdir/pkgconfig/jrtplib.pc
%_libdir/libjrtp.so
%_libdir/libjrtp.a
%_libdir/libjrtp.la
