%define		_state		stable
%define		orgname		libkcompactdisc
%define		qtver		4.8.1

Summary:	K Desktop Environment - compact disc library
Name:		kde4-%{orgname}
Version:	4.12.2
Release:	1
License:	GPL v2+
Group:		X11/Libraries
Source0:	ftp://ftp.kde.org/pub/kde/%{_state}/%{version}/src/%{orgname}-%{version}.tar.xz
# Source0-md5:	dc2cebedc269ef9eec0a49322ad933ef
BuildRequires:	alsa-lib-devel
BuildRequires:	cmake >= 2.8.0
BuildRequires:	kde4-kdelibs-devel >= %{version}
BuildRequires:	libstdc++-devel
BuildRequires:	pkgconfig
BuildRequires:	qt4-build >= %{qtver}
BuildRequires:	qt4-qmake >= %{qtver}
BuildRequires:	rpmbuild(macros) >= 1.600
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A KDE compact disc library

%package devel
Summary:	Header files for libkcompactdisc library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki libkcompactdisc
Group:		X11/Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header files for libkcompactdisc library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki libkcompactdisc.

%prep
%setup -q -n %{orgname}-%{version}

%build
install -d build
cd build
%cmake \
	../

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} -C build install \
	DESTDIR=$RPM_BUILD_ROOT \
	kde_htmldir=%{_kdedocdir}

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libkcompactdisc.so.4.*.*
%attr(755,root,root) %ghost %{_libdir}/libkcompactdisc.so.?

%files devel
%defattr(644,root,root,755)
%{_includedir}/libkcompactdisc
%attr(755,root,root) %{_libdir}/libkcompactdisc.so
%dir %{_libdir}/cmake/libkcompactdisc
%{_libdir}/cmake/libkcompactdisc/LibkcompactdiscConfig.cmake
%{_libdir}/cmake/libkcompactdisc/LibkcompactdiscTargets-pld.cmake
%{_libdir}/cmake/libkcompactdisc/LibkcompactdiscTargets.cmake
