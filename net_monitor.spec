Summary:	Network monitoring tool
Name:		net_monitor
Version:	0.11
Release:	9
License:	GPLv2
Group:		Monitoring
Url:		http://git.mandriva.com/?p=projects/net_monitor.git
Source0:	%{name}-%{version}.tar.bz2
BuildRequires:	python-setuptools
BuildRequires:	libiw-devel
BuildRequires:	pkgconfig(python)
Requires:	pygtk2.0
Requires:	python
Requires:	vnstat

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
%doc AUTHORS COPYING README NEWS TODO
%{_bindir}/%{name}
%{_sysconfdir}/sysconfig/network-scripts/if*.d/netmonitor*
%{py_platsitedir}/%{name}-%{version}-py*
%{py_platsitedir}/%{name}
%ghost %{_logdir}/%{name}.log

