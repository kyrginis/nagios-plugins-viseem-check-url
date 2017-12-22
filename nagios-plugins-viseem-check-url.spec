Name:		nagios-plugins-viseem-check-url
Version:	0.1
Release:	1%{?dist}
Summary:	Nagios URL probe
License:	GPLv3+
Packager:	Kyriakos Gkinis <kyrginis@admin.grnet.gr>

Source:		%{name}-%{version}.tar.gz
BuildArch:	noarch
BuildRoot:	%{_tmppath}/%{name}-%{version}

Requires:	python
Requires:	python-argparse

%description
Wrapper for default check_http that adjust options to url type, port etc.

%prep
%setup -q

%define _unpackaged_files_terminate_build 0 

%install

install -d %{buildroot}/%{_libexecdir}/argo-monitoring/probes/viseem-check-url
install -m 755 check_url.py %{buildroot}/%{_libexecdir}/argo-monitoring/probes/viseem-check-url/check_url.py

%files
%dir /%{_libexecdir}/argo-monitoring
%dir /%{_libexecdir}/argo-monitoring/probes/
%dir /%{_libexecdir}/argo-monitoring/probes/viseem-check-url

%attr(0755,root,root) /%{_libexecdir}/argo-monitoring/probes/viseem-check-url/check_url.py

%changelog
* Fri Dec 22 2017 Kyriakos Gkinis <kyrginis@admin.grnet.gr> - 0.1-1
- Initial version of the package
