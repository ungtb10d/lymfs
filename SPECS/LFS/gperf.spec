Name:           gperf
Version:        3.1
Release:        1%{?dist}
Summary:        Gperf generates a perfect hash function from a key set.
Vendor:			ungtb10d
Distribution:	lymfs

Group:          Applications/System
License:        GPLv3
URL:            https://www.gnu.org/software/gperf/
Source0:        http://ftp.gnu.org/pub/gnu/${name}/%{name}-%{version}.tar.gz

%description
Gperf generates a perfect hash function from a key set.

%prep
%setup -q


%build
%configure --docdir=%{_defaultdocdir}/%{name}-%{version}
make %{?_smp_mflags}

%check
make -j1 check

%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT


%clean
rm -rf $RPM_BUILD_ROOT


%files
%{!?_licensedir:%global license %%doc}
%license COPYING
%{_bindir}/*
%{_defaultdocdir}
%{_mandir}/*/*
%{_infodir}/*


%changelog
