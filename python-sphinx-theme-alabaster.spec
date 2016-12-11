%global pypi_name alabaster
%global srcname sphinx-theme-%{pypi_name}

Name:           python-%{srcname}
Version:        0.7.9
Release:        2%{?dist}
Summary:        Configurable sidebar-enabled Sphinx theme

License:        BSD
URL:            https://pypi.python.org/pypi/%{pypi_name}
Source0:        https://pypi.python.org/packages/71/c3/70da7d8ac18a4f4c502887bd2549e05745fa403e2cd9d06a8a9910a762bc/%{pypi_name}-%{version}.tar.gz

BuildArch:      noarch
BuildRequires:  python2-devel
BuildRequires:  python-setuptools

%description
This theme is a modified "Kr" Sphinx theme from @kennethreitz (especially as
used in his Requests project), which was itself originally based on @mitsuhiko's
theme used for Flask & related projects.


%package -n python2-%{srcname}
Summary:        Configurable sidebar-enabled Sphinx theme
%{?python_provide:%python_provide python2-%{srcname}}

%description -n python2-%{srcname}
This theme is a modified "Kr" Sphinx theme from @kennethreitz (especially as
used in his Requests project), which was itself originally based on @mitsuhiko's
theme used for Flask & related projects.


%package -n     python%{python3_pkgversion}-%{srcname}
Summary:        Configurable sidebar-enabled Sphinx theme
BuildArch:      noarch
BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-setuptools
%{?python_provide:%python_provide python%{python3_pkgversion}-%{srcname}}

%description -n python%{python3_pkgversion}-%{srcname}
This theme is a modified "Kr" Sphinx theme from @kennethreitz (especially as
used in his Requests project), which was itself originally based on @mitsuhiko's
theme used for Flask & related projects.


%prep
%setup -qn %{pypi_name}-%{version}

# Remove bundled eggs
rm -rf %{pypi_name}.egg-info


%build
%py2_build
%py3_build


%install
%py2_install
%py3_install


%files -n python2-%{srcname}
%license LICENSE
%doc README.rst
%{python2_sitelib}/%{pypi_name}-%{version}-py%{python2_version}.egg-info/
%{python2_sitelib}/%{pypi_name}/

%files -n python%{python3_pkgversion}-%{srcname}
%license LICENSE
%doc README.rst
%{python3_sitelib}/%{pypi_name}-%{version}-py%{python3_version}.egg-info/
%{python3_sitelib}/%{pypi_name}/


%changelog
* Fri Dec 09 2016 Charalampos Stratakis <cstratak@redhat.com> - 0.7.9-2
- Rebuild for Python 3.6

* Sun Sep 18 2016 Julien Enselme <jujens@jujens.eu> - 0.7.9-1
- Update to 0.7.9

* Fri May 13 2016 Julien Enselme <jujens@jujens.eu> - 0.7.8-1
- Use %%python3_pkgversion macro for EPEL7 release

* Fri May 13 2016 Julien Enselme <jujens@jujens.eu> - 0.7.8-1
- Update to 0.7.8 (#1334952)

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.6-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Nov 5 2015 Julien Enselme <jujens@jujens.eu> - 0.7.6-5
- Rebuilt for python 3.5

* Fri Jul 31 2015 Julien Enseme <jujens@jujens.eu> - 0.7.6-4
- Use %%py2_build, %%py3build, %%py2_install and %%py2_install
- Make a python2 subpackage

* Thu Jul 30 2015 Julien Enselme <jujens@jujens.eu> - 0.7.6-3
- Add provides for python2-sphinx-theme-alabaster
- Remove usage of python2 and python3 dirs

* Fri Jul 24 2015 Julien Enselme <jujens@jujens.eu> - 0.7.6-2
- Remove %%py3dir macro
- Add CFLAGS in %%build

* Sat Jul 18 2015 Julien Enselme <jujens@jujens.eu> - 0.7.6-1
- Initial packaging
