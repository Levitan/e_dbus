%global svn_revision svn81788

Name:           e_dbus
Version:        1.7.99
Release:        1.%{svn_revision}%{?dist}
License:        BSD
Group:          System Environment/Libraries
URL:            http://www.enlightenment.org/
Summary:        EFL Wrapper for DBus
Source:         %{name}-%{version}.%{svn_revision}.tar.xz
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  efl-devel >= %{version}
BuildRequires:  libtool
BuildRequires:  dbus-devel

%description
e_dbus provides a convenience wrapper for EFL applications using DBus.

%package devel
Summary:        e_dbus headers, static libraries, documentation and test programs
Group:          System Environment/Libraries
License:        BSD
Requires:       %{name}-libs%{?_isa} = %{version}-%{release}

%description devel
Headers, static libraries, test programs and documentation for e_dbus

%package -n e_dbus-libs
Summary:        E_Dbus Dynamic Library
Group:          System Environment/Libraries

%description -n e_dbus-libs
Main dynamic library of E_Dbus.

%prep
%setup -q -n %{name}-%{version}.%{svn_revision}

%build
autoreconf -ifv
%{configure} --disable-silent-rules \
             --disable-static \
             --enable-ebluez \
             --enable-econnman0_7x \
             --enable-eofono \
             
make %{?_smp_mflags}

%install
make install DESTDIR="%buildroot"
find %{buildroot}%{_libdir} -name '*.la' -exec rm -v {} \;
# Get rid of unneeded testing cruft.
%{__rm} -rf $RPM_BUILD_ROOT%{_datadir}/%{name}

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%doc AUTHORS COPYING* README
%{_bindir}/*

%files -n e_dbus-libs
%{_libdir}/*.so.*

%files devel
%{_includedir}/e_dbus-1/
%{_libdir}/*.so
%{_libdir}/pkgconfig/*

%changelog
* Sat Dec 29 2012 <vlevitan91@gmail.com> - 1.7.99-1.svn81788
- Let's start e_dbus