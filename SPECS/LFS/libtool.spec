Summary:	Shared libraries, portable interface
Name:		libtool
Version:	2.4.6
Release:	1
License:	GPLv2
URL:		http://www.gnu.org/software/libtool
Group:		Development/Tools
Vendor:		ungtb10d
Distribution:	lymfs
Source:		http://ftp.gnu.org/gnu/libtool/%{name}-%{version}.tar.xz
%description
It wraps the complexity of using shared libraries in a 
consistent, portable interface.
%prep
%setup -q
%build
./configure \
	--prefix=%{_prefix}
make %{?_smp_mflags}
%install
make DESTDIR=%{buildroot} install
find %{buildroot}%{_libdir} -name '*.la' -delete
rm -rf %{buildroot}%{_infodir}
%check
make -k check |& tee %{_specdir}/%{name}-check-log || %{nocheck}
%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig
%files
%defattr(-,root,root)
%{_bindir}/*
%{_libdir}/*
%{_includedir}/*
%{_datarootdir}/aclocal/*
%{_datarootdir}/%{name}/*
%{_mandir}/*/*
%changelog
*	Wed Jan 30 2013 baho-utot <root@blckswan.no> 2.4.2-1
-	Initial build.	First version
