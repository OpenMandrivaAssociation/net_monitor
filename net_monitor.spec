Name:		net_monitor
Version:	0.06
Release:	%mkrel 1
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
BuildRoot:	%{_tmppath}/%{name}-%{version}

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
rm -rf %{buildroot}

make install

%find_lang %name

%clean
rm -rf %{buildroot}

%files -f %{name}.lang
%defattr(-,root,root)
%doc AUTHORS COPYING README NEWS TODO
%_bindir/%{name}
%{py_platsitedir}/%{name}-%{version}-py*
%{py_platsitedir}/%{name}
