Summary:	The Gzip package contains programs for compressing and decompressing files.
Name:		tools-gzip
Version:	1.9
Release:	1
License:	GPL
URL:		http://ftp.gnu.org/gnu/gzip
Group:		LFS/Tools
Vendor:	Octothorpe
BuildRequires:	tools-grep
Source0:	http://ftp.gnu.org/gnu/gzip/gzip-%{version}.tar.xz
%description
	The Gzip package contains programs for compressing and decompressing files.
%prep
%setup -q -n gzip-%{version}
%build
	./configure \
		--prefix=%{_prefix}
	make %{?_smp_mflags}
%install
	make DESTDIR=%{buildroot} install
	rm -rf %{buildroot}%{_infodir}
	rm -rf %{buildroot}%{_mandir}
	#	Create file list
	find %{buildroot} -name '*.la' -delete
	find "${RPM_BUILD_ROOT}" -not -type d -print > filelist.rpm
	sed -i "s|^${RPM_BUILD_ROOT}||" filelist.rpm
%files -f filelist.rpm
   %defattr(-,lfs,lfs)
%changelog
*	Sun Mar 11 2018 baho-utot <root@blckswan.no> 1.9-1
*	Mon Jan 01 2018 baho-utot <root@blckswan.no> 1.8-1
-	LFS-8.1
