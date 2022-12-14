<<<<<<< HEAD
Summary:	The Bison package contains a parser generator.
Name:		bison
Version:	3.0.4
Release:	1
License:	Any
URL:		Any
Group:		LFS/Base
Vendor:		Octothorpe
Source0:	http://ftp.gnu.org/gnu/%{name}/%{name}-%{version}.tar.xz
%description
	The Bison package contains a parser generator.
%prep
%setup -q -n %{NAME}-%{VERSION}
%build
	./configure \
		--prefix=%{_prefix} \
		--docdir=%{_docdir}/%{name}-%{version}
	make %{?_smp_mflags}
%install
	make DESTDIR=%{buildroot} install
	#	Copy license/copying file
	#	install -D -m644 LICENSE %{buildroot}/usr/share/licenses/%{name}/LICENSE
	#	Create file list
	rm  %{buildroot}%{_infodir}/dir
	find %{buildroot} -name '*.la' -delete
	find "${RPM_BUILD_ROOT}" -not -type d -print > filelist.rpm
	sed -i "s|^${RPM_BUILD_ROOT}||" filelist.rpm
	sed -i '/man\/man/d' filelist.rpm
	sed -i '/\/usr\/share\/info/d' filelist.rpm
%clean
%files -f filelist.rpm
	%defattr(-,root,root)
	%{_infodir}/*.gz
	%{_mandir}/man1/*.gz
%changelog
*	Tue Jan 09 2018 baho-utot <root@blckswan.no> 3.0.4-1
-	Initial build.	First version
=======
Summary:	Contains a parser generator
Name:		bison
Version:	3.0.4
Release:	1
License:	GPLv3
URL:		http://www.gnu.org/software/bison
Group:		LFS/Base
Vendor:		ungtb10d
Distribution:	lymfs
Source:		http://ftp.gnu.org/gnu/bison/%{name}-%{version}.tar.xz
%description
This package contains a parser generator
%prep
%setup -q
%build
./configure \
	--prefix=%{_prefix} \
	--docdir=%{_defaultdocdir}/%{name}-%{version}
make %{?_smp_mflags}
%install
make DESTDIR=%{buildroot} install
rm -rf %{buildroot}%{_infodir}
%find_lang %{name}
%check
make -k check |& tee %{_specdir}/%{name}-check-log || %{nocheck}
%files -f %{name}.lang
%defattr(-,root,root)
%{_defaultdocdir}/*
%{_bindir}/*
%{_libdir}/*
%{_datarootdir}/%{name}/*
%{_datarootdir}/aclocal/*
%lang(ast) %{_datarootdir}/locale/ast/LC_MESSAGES/bison-runtime.mo
%lang(da) %{_datarootdir}/locale/da/LC_MESSAGES/bison-runtime.mo
%lang(de) %{_datarootdir}/locale/de/LC_MESSAGES/bison-runtime.mo
%lang(el) %{_datarootdir}/locale/el/LC_MESSAGES/bison-runtime.mo
%lang(eo) %{_datarootdir}/locale/eo/LC_MESSAGES/bison-runtime.mo
%lang(es) %{_datarootdir}/locale/es/LC_MESSAGES/bison-runtime.mo
%lang(et) %{_datarootdir}/locale/et/LC_MESSAGES/bison-runtime.mo
%lang(fi) %{_datarootdir}/locale/fi/LC_MESSAGES/bison-runtime.mo
%lang(fr) %{_datarootdir}/locale/fr/LC_MESSAGES/bison-runtime.mo
%lang(ga) %{_datarootdir}/locale/ga/LC_MESSAGES/bison-runtime.mo
%lang(gl) %{_datarootdir}/locale/gl/LC_MESSAGES/bison-runtime.mo
%lang(hr) %{_datarootdir}/locale/hr/LC_MESSAGES/bison-runtime.mo
%lang(hu) %{_datarootdir}/locale/hu/LC_MESSAGES/bison-runtime.mo
%lang(ia) %{_datarootdir}/locale/ia/LC_MESSAGES/bison-runtime.mo
%lang(id) %{_datarootdir}/locale/id/LC_MESSAGES/bison-runtime.mo
%lang(it) %{_datarootdir}/locale/it/LC_MESSAGES/bison-runtime.mo
%lang(ja) %{_datarootdir}/locale/ja/LC_MESSAGES/bison-runtime.mo
%lang(ky) %{_datarootdir}/locale/ky/LC_MESSAGES/bison-runtime.mo
%lang(lt) %{_datarootdir}/locale/lt/LC_MESSAGES/bison-runtime.mo
%lang(lv) %{_datarootdir}/locale/lv/LC_MESSAGES/bison-runtime.mo
%lang(ms) %{_datarootdir}/locale/ms/LC_MESSAGES/bison-runtime.mo
%lang(nb) %{_datarootdir}/locale/nb/LC_MESSAGES/bison-runtime.mo
%lang(nl) %{_datarootdir}/locale/nl/LC_MESSAGES/bison-runtime.mo
%lang(pl) %{_datarootdir}/locale/pl/LC_MESSAGES/bison-runtime.mo
%lang(pt) %{_datarootdir}/locale/pt/LC_MESSAGES/bison-runtime.mo
%lang(pt_BR) %{_datarootdir}/locale/pt_BR/LC_MESSAGES/bison-runtime.mo
%lang(ro) %{_datarootdir}/locale/ro/LC_MESSAGES/bison-runtime.mo
%lang(ru) %{_datarootdir}/locale/ru/LC_MESSAGES/bison-runtime.mo
%lang(sl) %{_datarootdir}/locale/sl/LC_MESSAGES/bison-runtime.mo
%lang(sq) %{_datarootdir}/locale/sq/LC_MESSAGES/bison-runtime.mo
%lang(sr) %{_datarootdir}/locale/sr/LC_MESSAGES/bison-runtime.mo
%lang(sv) %{_datarootdir}/locale/sv/LC_MESSAGES/bison-runtime.mo
%lang(th) %{_datarootdir}/locale/th/LC_MESSAGES/bison-runtime.mo
%lang(tr) %{_datarootdir}/locale/tr/LC_MESSAGES/bison-runtime.mo
%lang(uk) %{_datarootdir}/locale/uk/LC_MESSAGES/bison-runtime.mo
%lang(vi) %{_datarootdir}/locale/vi/LC_MESSAGES/bison-runtime.mo
%lang(zh_CN) %{_datarootdir}/locale/zh_CN/LC_MESSAGES/bison-runtime.mo
%lang(zh_TW) %{_datarootdir}/locale/zh_TW/LC_MESSAGES/bison-runtime.mo
%{_mandir}/*/*
%changelog
*	Sun Apr 06 2014 baho-utot <root@blckswan.no> 3.0.2-1
*	Sat Aug 24 2013 baho-utot <root@blckswan.no> 3.0-1
*	Fri May 10 2013 baho-utot <root@blckswan.no> 2.7.1-1
*	Wed Mar 21 2013 baho-utot <root@blckswan.no> 2.7-1
>>>>>>> Initial Commit.
