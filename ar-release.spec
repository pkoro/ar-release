Name:		ar-release
Version:	1.0.1
Release:	1%{?dist}
Summary:	Repository files for ar mini project
Group:		EGI/SA4
BuildArch:	noarch
License:	ASL 2.0
URL:		http://code.grnet.gr/
Source0:	%{name}-%{version}.tar.gz
BuildRoot:	%(mktemp -ud %{_tmppath}/%{name}-%{version}-%{release}-XXXXXX)

%description
This package includes the A/R Comp Engine release file
and the needed repository configuration.

Includes repository definition for:
- EGI-trustanchors repository
- A/R Comp Engine repository

%prep
%setup -q


%build


%install
rm -rf %{buildroot}

install -dm 755 $RPM_BUILD_ROOT%{_sysconfdir}/yum.repos.d
install -pm 644 repos.d/EGI-trustanchors.repo $RPM_BUILD_ROOT%{_sysconfdir}/yum.repos.d
install -pm 644 repos.d/arstats.repo $RPM_BUILD_ROOT%{_sysconfdir}/yum.repos.d/arstats.repo

%clean
rm -rf %{buildroot}


%files
%defattr(-,root,root,-)
%doc licenses/*
%config(noreplace) /etc/yum.repos.d/*


%changelog
* Thu Aug 29 2013 Paschalis Korosoglou <pkoro@grid.auth.gr> - 1.0.0-2%{?dist}
- Added buildarch to noarch
* Mon Aug 26 2013 Paschalis Korosoglou <pkoro@grid.auth.gr> - 1.0.0-1%{?dist}
- Initial release package
