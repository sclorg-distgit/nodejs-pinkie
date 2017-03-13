%{?scl:%scl_package nodejs-%{module_name}}
%{!?scl:%global pkg_name %{name}}
%{?nodejs_find_provides_and_requires}

%global enable_tests 0
%global module_name pinkie

Name:           %{?scl_prefix}nodejs-%{module_name}
Version:    2.0.4
Release:    1%{?dist}
Summary:        Itty bitty little widdle twinkie pinkie ES6 Promise implementation

License:        MIT
URL:            https://github.com/floatdrop/pinkie
Source0:        https://github.com/floatdrop/%{module_name}/archive/v%{version}.tar.gz
BuildArch:      noarch
ExclusiveArch:  %{ix86} x86_64 %{arm} noarch

BuildRequires:  %{?scl_prefix}nodejs-devel

%if 0%{?enable_tests}
BuildRequires:  %{?scl_prefix}npm(mocha)
%endif

%description
%{summary}.

%prep
%setup -q -n %{module_name}-%{version}
rm -rf node_modules

%build
# nothing to build

%install
mkdir -p %{buildroot}%{nodejs_sitelib}/%{module_name}
cp -pr package.json index.js %{buildroot}%{nodejs_sitelib}/%{module_name}
%nodejs_symlink_deps

%if 0%{?enable_tests}

%check
%nodejs_symlink_deps --check
mocha
%endif

%files
%{!?_licensedir:%global license %doc}
%doc readme.md 
%doc license
%{nodejs_sitelib}/%{module_name}

%changelog
* Wed Sep 14 2016 Zuzana Svetlikova <zsvetlik@redhat.com> - 2.0.4-1
- Updated with script

* Tue Feb 16 2016 Zuzana Svetlikova <zsvetlik@redhat.com> - 2.0.1-6
- Use macro in -runtime dependency

* Sun Feb 14 2016 Zuzana Svetlikova <zsvetlik@redhat.com> - 2.0.1-5
- Rebuilt with updated metapackage

* Fri Jan 15 2016 Tomas Hrcka <thrcka@redhat.com> - 2.0.1-4
- Enable scl macros

* Mon Nov 23 2015 Parag Nemade <pnemade AT redhat DOT com> - 2.0.1-1
- update to 2.0.1

* Wed Jul 15 2015 Parag Nemade <pnemade AT redhat DOT com> - 1.0.0-1
- Initial packaging
