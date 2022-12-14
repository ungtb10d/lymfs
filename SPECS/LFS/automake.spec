Summary:	Programs for generating Makefiles
Name:		automake
Version:	1.15.1
Release:	1
License:	GPLv2
URL:		http://www.gnu.org/software/automake/
Group:		LFS/Base
Vendor:		ungtb10d
Distribution:	lymfs
Source:		http://ftp.gnu.org/gnu/automake/%{name}-%{version}.tar.xz
%description
Contains programs for generating Makefiles for use with Autoconf.
%prep
%setup -q
%build
./configure \
	--prefix=%{_prefix} \
	--docdir=%{_docdir}/%{name}-%{version}
make %{?_smp_mflags}
%check
sed -i "s:./configure:LEXLIB=/usr/lib/libfl.a &:" t/lex-{clean,depend}-cxx.sh
make -k check %{?_smp_mflags} |& tee %{_specdir}/%{name}-check-log || %{nocheck}
%install
rm -rf $RPM_BUILD_ROOT
make DESTDIR=%{buildroot} install
rm -f %{buildroot}%{_infodir}/dir
%files
%defattr(-,root,root)
%{_bindir}/*
%{_datarootdir}/aclocal/README
%{_datarootdir}/%{name}-1.15/*
%{_datarootdir}/aclocal-1.15/*
%doc %{_docdir}/%{name}-%{version}/*
%doc %{_infodir}/*
%doc %{_mandir}/*/*
%changelog
*	Sun Apr 06 2014 baho-utot <root@blckswan.no> 1.14.1-1
*	Fri Jun 28 2013 baho-utot <root@blckswan.no> 1.14-1
-	Upgrade version