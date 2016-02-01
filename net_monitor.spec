Summary:	Network monitoring tool
Name:		net_monitor
Version:	0.22
Release:	1
License:	GPLv2
Group:		Monitoring
Url:		http://gitweb.mageia.org/software/net_monitor
Source0:	%{name}-%{version}.tar.xz
BuildRequires:	python-setuptools
BuildRequires:	libiw-devel
BuildRequires:	pkgconfig(python)
Requires:	python
Requires:	vnstat
Requires:	typelib(Gdk) == 3.0
Requires:	typelib(Gtk) == 3.0

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

%find_lang %{name}

%files -f %{name}.lang
%doc AUTHORS COPYING README NEWS TODO
%{_bindir}/%{name}
%{_sysconfdir}/sysconfig/network-scripts/if*.d/netmonitor*
%{py_platsitedir}/%{name}-%{version}-py*
%{py_platsitedir}/%{name}
%ghost %{_logdir}/%{name}.log

