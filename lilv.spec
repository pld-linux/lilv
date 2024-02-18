#
# Conditional build:
%bcond_with	apidocs	# API documentation

Summary:	LV2 host library to make LV2 plugin use as simple as possible
Summary(pl.UTF-8):	Biblioteka hosta LV2 ułatwiająca korzystanie z wtyczek LV2
Name:		lilv
Version:	0.24.24
Release:	1
License:	ISC
Group:		Libraries
Source0:	http://download.drobilla.net/%{name}-%{version}.tar.xz
# Source0-md5:	02e4d830bb82314aff2ceb441fe4d0c1
URL:		http://drobilla.net/software/lilv/
BuildRequires:	libsndfile-devel >= 1.0.0
BuildRequires:	libstdc++-devel
BuildRequires:	lv2-devel >= 1.18.2
BuildRequires:	meson >= 0.56.0
BuildRequires:	ninja >= 1.5
BuildRequires:	pkgconfig
# or python 2.6+, but no sense to introduce in 2020
BuildRequires:	python3 >= 1:3.4
BuildRequires:	python3-modules >= 1:3.4
BuildRequires:	rpm-build >= 4.6
BuildRequires:	rpmbuild(macros) >= 1.736
BuildRequires:	serd-devel >= 0.30.10
BuildRequires:	sord-devel >= 0.16.15
BuildRequires:	sratom-devel >= 0.6.10
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
BuildRequires:	zix-devel >= 0.4.0
%if %{with apidocs}
BuildRequires:	doxygen
BuildRequires:	sphinx-pdg
BuildRequires:	sphinxygen
%endif
Requires:	lv2 >= 1.18.2
Requires:	serd >= 0.30.10
Requires:	sord >= 0.16.15
Requires:	sratom >= 0.6.10
Requires:	zix >= 0.4.0
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
Requires:	lv2-devel >= 1.18.2
Requires:	serd-devel >= 0.30.10
Requires:	sord-devel >= 0.16.15
Requires:	sratom-devel >= 0.6.10
Requires:	zix-devel >= 0.4.0

%description devel
Header files for Lilv library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki Lilv.

%package -n bash-completion-lilv
Summary:	Bash auto-completion for lilv commands
Summary(pl.UTF-8):	Bashowe dopełnianie składni dla poleceń lilv
Group:		Applications/Shells
Requires:	bash-completion
BuildArch:	noarch

%description -n bash-completion-lilv
Bash auto-completion script for lv2info and lv2jack commands.

%description -n bash-completion-lilv -l pl.UTF-8
Skrypt bashowego dopełniania parametrów dla poleceń lv2info i lv2jack.

%package -n python3-lilv
Summary:	Python binding for lilv
Summary(pl.UTF-8):	Wiązania Pythona do lilv
Group:		Libraries/Python
Requires:	%{name} = %{version}-%{release}
Requires:	python3-modules >= 1:3.4

%description -n python3-lilv
Python binding for lilv.

%description -n python3-lilv -l pl.UTF-8
Wiązania Pythona do lilv.

%prep
%setup -q

%build
%meson build \
	--default-library=shared \
	%{!?with_apidocs:-Ddocs=disabled}

%ninja_build -C build

%install
rm -rf $RPM_BUILD_ROOT

%ninja_install -C build

%py3_comp $RPM_BUILD_ROOT%{py3_sitescriptdir}
%py3_ocomp $RPM_BUILD_ROOT%{py3_sitescriptdir}

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS COPYING NEWS README.md
%attr(755,root,root) %{_bindir}/lv2apply
%attr(755,root,root) %{_bindir}/lv2bench
%attr(755,root,root) %{_bindir}/lv2info
%attr(755,root,root) %{_bindir}/lv2ls
%attr(755,root,root) %{_libdir}/liblilv-0.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/liblilv-0.so.0
%{_mandir}/man1/lv2apply.1*
%{_mandir}/man1/lv2bench.1*
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

%files -n python3-lilv
%defattr(644,root,root,755)
%{py3_sitescriptdir}/lilv.py
%{py3_sitescriptdir}/__pycache__/lilv.cpython-*.py[co]
