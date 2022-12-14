Summary:	Utilities for loading kernel modules
Name:		kmod
Version:	25
Release:	1
License:	GPLv2
URL:		http://www.kernel.org/pub/linux/utils/kernel/kmod
Group:		Applications/System
Vendor:		ungtb10d
Distribution:	lymfs
Source:		http://www.kernel.org/pub/linux/utils/kernel/kmod/%{name}-%{version}.tar.xz
%description
The Kmod package contains libraries and utilities for loading kernel modules
%prep
%setup -q
%build
./configure \
	--prefix=%{_prefix} \
	--bindir=/bin \
	--sysconfdir=%{_sysconfdir} \
	--with-rootlibdir=%{_lib} \
	--disable-manpages \
	--with-xz \
	--with-zlib
make %{?_smp_mflags}
%install
rm -rf $RPM_BUILD_ROOT
make DESTDIR=$RPM_BUILD_ROOT install
install -vdm 755 %{buildroot}/sbin
for target in depmod insmod modinfo modprobe rmmod; do
	ln -sfv ../bin/kmod %{buildroot}/sbin/$target
done
ln -sfv kmod %{buildroot}/bin/lsmod
find %{buildroot} -name '*.la' -delete
%check
make -k check |& tee %{_specdir}/%{name}-check-log || %{nocheck}
%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig
%files
%defattr(-,root,root)
/bin/*
%{_lib}/*
/sbin/*
%{_libdir}/*
%{_includedir}/*
%{_datadir}/bash-completion/completions/kmod
%changelog
*	Sun Apr 06 2014 baho-utot <root@blckswan.no> 16-1
*	Sat Aug 24 2013 baho-utot <root@blckswan.no> 14-1
*	Fri May 10 2013 baho-utot <root@blckswan.no> 13-1
-	Initial version	

