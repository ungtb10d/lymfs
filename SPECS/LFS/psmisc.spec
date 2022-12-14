Summary:	Displays information about running processes
Name:		psmisc
Version:	23.1
Release:	1
License:	GPLv2
URL:		http://psmisc.sourceforge.net/
Group:		Applications/System
Vendor:		ungtb10d
Distribution:	lymfs
Source:		http://prdownloads.sourceforge.net/psmisc/%{name}-%{version}.tar.xz
%description
The Psmisc package contains programs for displaying information
about running processes.
%prep
%setup -q
%build
./configure \
	--prefix=%{_prefix}
make %{?_smp_mflags}
%install
make DESTDIR=%{buildroot} install
install -vdm 755 %{buildroot}/bin
mv -v %{buildroot}%{_bindir}/fuser   %{buildroot}/bin
mv -v %{buildroot}%{_bindir}/killall %{buildroot}/bin
%find_lang %{name}
%check
make -k check |& tee %{_specdir}/%{name}-check-log || %{nocheck}
%files -f %{name}.lang
%defattr(-,root,root)
/bin/*
%{_bindir}/*
%{_mandir}/*/*
%changelog
*	Wed Mar 21 2013 baho-utot <root@blckswan.no> 22.20-1
-	Upgrade version
