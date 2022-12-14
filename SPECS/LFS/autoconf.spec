Summary:	The Autoconf package contains programs for producing shell scripts that can automatically configure source code.
Name:		autoconf
Version:	2.69
Release:	1
License:	GPLv2

URL:		http://www.gnu.org/software/autoconf
Group:		LFS/Base
Vendor:		ungtb10d
Distribution:	lymfs
Source:		http://ftp.gnu.org/gnu/autoconf/%{name}-%{version}.tar.xz
%description
The package contains programs for producing shell scripts that can
automatically configure source code.
%prep
%setup -q
%build
./configure \
	--prefix=%{_prefix}
make %{?_smp_mflags}
%install
rm -rf $RPM_BUILD_ROOT
make DESTDIR=$RPM_BUILD_ROOT install
rm -v $RPM_BUILD_ROOT%{_infodir}/dir

%files
%defattr(-,root,root)
%{_bindir}/*
%doc %{_mandir}/*/*
%doc %{_infodir}/*
%{_datarootdir}/autoconf/*

%changelog
*	Wed Jan 30 2013 baho-utot <root@blckswan.no> 2.69-1
-	Initial build.	First version

