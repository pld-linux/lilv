Summary:	LV2 host library to make LV2 plugin use as simple as possible
Summary(pl.UTF-8):	Biblioteka hosta LV2 ułatwiająca korzystanie z wtyczek LV2
Name:		lilv
Version:	0.16.0
Release:	1
License:	ISC
Group:		Libraries
Source0:	http://download.drobilla.net/%{name}-%{version}.tar.bz2
# Source0-md5:	12eb71f2b5b8a68e15c1c816896bcb9f
URL:		http://drobilla.net/software/lilv/
BuildRequires:	doxygen
BuildRequires:	libstdc++-devel
BuildRequires:	lv2-devel >= 1.0.0
BuildRequires:	pkgconfig
BuildRequires:	python
BuildRequires:	python-modules
BuildRequires:	serd-devel >= 0.14.0
BuildRequires:	sord-devel >= 0.12.0
BuildRequires:	sratom-devel >= 0.4.0
Requires:	lv2 >= 1.0.0
Requires:	serd >= 0.14.0
Requires:	sord >= 0.12.0
Requires:	sratom >= 0.4.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Lilv is a library to make the use of LV2 plugins as simple as possible
for applications. Lilv is the successor to SLV2, rewritten to be
significantly faster and have minimal dependencies.

%description -l pl.UTF-8
Lilv to biblioteka ułatwiająca korzystanie z wtyczek LV2 w
aplikacjach. Jest następczynią SLV2; została przepisana tak, aby była
znacznie szybsza i miała minimalne zależności.

%package devel
Summary:	Header files for Lilv library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki Lilv
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	lv2-devel >= 1.0.0
Requires:	serd-devel >= 0.14.0
Requires:	sord-devel >= 0.12.0
Requires:	sratom-devel >= 0.4.0

%description devel
Header files for Lilv library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki Lilv.

%package -n bash-completion-lilv
Summary:	Bash auto-completion for lilv commands
Summary(pl.UTF-8):	Bashowe dopełnianie składni dla poleceń lilv
Group:		Applications/Shells
Requires:	bash-completion

%description -n bash-completion-lilv
Bash auto-completion script for lv2info and lv2jack commands.

%description -n bash-completion-lilv -l pl.UTF-8
Skrypt bashowego dopełniania parametrów dla poleceń lv2info i lv2jack.

%prep
%setup -q

%build
CC="%{__cc}" \
CFLAGS="%{rpmcflags}" \
./waf configure \
	--prefix=%{_prefix} \
	--libdir=%{_libdir} \
	--configdir=/etc \
	--strict

./waf -v

%install
rm -rf $RPM_BUILD_ROOT

./waf install \
	--destdir=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS COPYING NEWS README
%attr(755,root,root) %{_bindir}/lilv-bench
%attr(755,root,root) %{_bindir}/lv2bench
%attr(755,root,root) %{_bindir}/lv2info
%attr(755,root,root) %{_bindir}/lv2ls
%attr(755,root,root) %{_libdir}/liblilv-0.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/liblilv-0.so.0
%{_mandir}/man1/lv2info.1*
%{_mandir}/man1/lv2ls.1*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/liblilv-0.so
%{_includedir}/lilv-0
%{_pkgconfigdir}/lilv-0.pc

%files -n bash-completion-lilv
%defattr(644,root,root,755)
/etc/bash_completion.d/lilv
