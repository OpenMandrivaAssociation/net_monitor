Name:		net_monitor
Version:	0.11
Release:	%mkrel 3
Summary:	Network monitoring tool
License:	GPLv2
Group:		Monitoring
Url:		http://git.mandriva.com/?p=projects/net_monitor.git
Source0:	%{name}-%{version}.tar.bz2
Requires:	pygtk2.0
Requires:	python
Requires:	vnstat
BuildRequires:	python-devel
BuildRequires:	python-setuptools
BuildRequires:	libiw-devel

%description
This is a network monitoring tool for Mandriva Linux, intended to replace the
old net_monitor from drakx-net.  It supports graphical network monitoring and
some advanced features, such as network profiling, activity monitoring,
detailed logging and network traffic statistics with help of vnstat reporting.

%prep
%setup -q

%build
make all

%install
make install
mkdir -p %{buildroot}%{_logdir}
touch %{buildroot}%{_logdir}/%{name}.log

%files
%defattr(-,root,root)
%doc AUTHORS COPYING README NEWS TODO
%_bindir/%{name}
%{_sysconfdir}/sysconfig/network-scripts/if*.d/netmonitor*
%{py_platsitedir}/%{name}-%{version}-py*
%{py_platsitedir}/%{name}
%ghost %{_logdir}/%{name}.log


%changelog
* Wed May 04 2011 Oden Eriksson <oeriksson@mandriva.com> 0.11-3mdv2011.0
+ Revision: 666608
- mass rebuild

* Mon Nov 01 2010 Funda Wang <fwang@mandriva.org> 0.11-2mdv2011.0
+ Revision: 591291
- rebuild for py2.7

* Mon Jun 14 2010 Eugeni Dodonov <eugeni@mandriva.com> 0.11-1mdv2010.1
+ Revision: 548031
- 0.11:
- properly check if device dissapears (#57108)

* Mon Jun 14 2010 Eugeni Dodonov <eugeni@mandriva.com> 0.10-1mdv2010.1
+ Revision: 547998
- 0.10:
- properly check for /var/log/net_monitor.log permissions (#59777)

* Sat Jun 05 2010 Eugeni Dodonov <eugeni@mandriva.com> 0.09-1mdv2010.1
+ Revision: 547137
- 0.09:
- add support for displaying network connections
- fix handling unsupported network card parameters
- fix crash on x86_64 bits when displaying route information

* Tue May 25 2010 Eugeni Dodonov <eugeni@mandriva.com> 0.08-1mdv2010.1
+ Revision: 546017
- 0.08:
- properly detect default route on x86_64 systems
- properly calculate network uptime
- modified timeouts to improve system power usage

* Mon Mar 01 2010 Eugeni Dodonov <eugeni@mandriva.com> 0.07-1mdv2010.1
+ Revision: 513263
- 0.07:
- implement initial connection uptime monitoring in GUI
- added ifup.d and ifdown.d scripts to account network uptime

* Wed Oct 14 2009 Eugeni Dodonov <eugeni@mandriva.com> 0.06-1mdv2010.0
+ Revision: 457417
- 0.06:
- support selecting default monitoring interface from command line
- support running from draknetcenter
- display interface icons when available

* Tue Oct 13 2009 Eugeni Dodonov <eugeni@mandriva.com> 0.05-1mdv2010.0
+ Revision: 457191
- 0.05:
- prevent crashing when running for long time
- pretty-format traffic data

* Thu Oct 01 2009 Eugeni Dodonov <eugeni@mandriva.com> 0.04-1mdv2010.0
+ Revision: 452202
- 0.04:
- simplified UI

* Wed Sep 30 2009 Eugeni Dodonov <eugeni@mandriva.com> 0.03-1mdv2010.0
+ Revision: 451674
- 0.03:
- improved network traffic graphics
- displaying global system information in statusbar (routes, DNS, ...)

* Wed Sep 30 2009 Eugeni Dodonov <eugeni@mandriva.com> 0.02-1mdv2010.0
+ Revision: 451116
- 0.02:
- largely improved execution overhead
- converted to use standard python routines
- interactively monitoring wireless link level
- correctly detecting network interface data
- displaying more detailed interface information
- using two fixed columns for interface data

* Fri Sep 25 2009 Eugeni Dodonov <eugeni@mandriva.com> 0.01-1mdv2010.0
+ Revision: 448548
- first version.
- Created package structure for net_monitor.

