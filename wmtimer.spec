Summary:	wmtimer - dockable alarm clock for WindowMaker
Summary(pl):	wmtimer - dokowalny czasomierz z alarmem dla WindowMakera
Name:		wmtimer
Version:	2.4
Release:	1
License:	GPL
Group:		X11/Window Managers/Tools
Source0:	http://www.dwave.net/~jking/wmtimer/%{name}-%{version}.tar.gz
Source1:	%{name}.desktop
Patch0:		%{name}-opts.patch
URL:		http://www.dwave.net/~jking/wmtimer/index.html
BuildRequires:	gtk+-devel >= 1.2.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define 	_prefix		/usr/X11R6

%description
Wmtimer is a dockable alarm clock for WindowMaker. Wmtimer can be run
in alarm, coutdown timer, or chronograph mode. In alarm or timer mode
you can either execute a command or sound the system bell when the
time is reached, and it is configurable through the command line or
the GTK GUI.

%description -l pl
Wmtimer jest dokowalnym czasomierzem z alarmem dla WindowMakera. Mo¿e
byæ uruchamiany w trybie 'budzika', stopera odliczaj±cego w dó³, lub
chronometru. Dwa pierwsze tryby pozwalaj± na wykonanie polecenia lub
wys³anie sygna³u d¼wiêkowego w wyznaczonym czasie. Program umo¿liwia
konfigrowanie okre¶lonych funkcji przez graficzny interfejs w GTK lub
bezpo¶rednio w linii poleceñ.

%prep
%setup -q
%patch -p1

%build
%{__make} clean -C %{name}
%{__make} -C %{name} \
	OPTS="%{rpmcflags} -Wall"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_applnkdir}/DockApplets} 

install %{name}/%{name} $RPM_BUILD_ROOT%{_bindir}
#install %{SOURCE1} $RPM_BUILD_ROOT%{_applnkdir}/DockApplets

gzip -9nf Changelog README CREDITS

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz

%attr(755,root,root) %{_bindir}/%{name}

#%{_applnkdir}/DockApplets/%{name}.desktop
