Summary:	wmtimer - dockable alarm clock for WindowMaker
Summary(pl):	wmtimer - dokowalny czasomierz z alarmem dla WindowMakera
Name:		wmtimer
Version: 	2.1
Release:	1
License:	GPL
Group:		X11/Window Managers/Tools
Group(pl):	X11/Zarz�dcy Okien/Narz�dzia
Source0:	http://www.dwave.net/~jking/wmtimer/%{name}-%{version}.tar.gz
Source1:	wmtimer.desktop
Patch:		wmtimer-opts.patch
URL:		http://www.dwave.net/~jking/wmtimer/index.html
BuildRequires:	XFree86-devel
BuildRequires:	xpm-devel
BuildRequires:	glib-devel >= 1.2.0
BuildRequires:	gtk+-devel >= 1.2.0
BuildRoot:	/tmp/%{name}-%{version}-root

%define 	_prefix		/usr/X11R6
%define		_applnkdir	%{_datadir}/applnk

%description
Wmtimer is a dockable alarm clock for WindowMaker. Wmtimer can be run
in alarm, coutdown timer, or chronograph mode. In alarm or timer mode
you can either execute a command or sound the system bell when the time
is reached, and it is configurable through the command line or the GTK
GUI.

%description -l pl
Wmtimer jest dokowalnym czasomierzem z alarmem dla WindowMakera. Mo�e
by� uruchamiany w trybie 'budzika', stopera odliczaj�cego w d�, lub 
chronometru. Dwa pierwsze tryby pozwalaj� na wykonanie polecenia lub
wys�anie sygna�u d�wi�kowego w wyznaczonym czasie. Program umo�liwia
konfigrowanie okre�lonych funkcji przez graficzny interfejs w GTK lub
bezpo�rednio w linii polece�.

%prep
%setup -q
%patch -p1

%build
make clean -C %{name}
make -C %{name} \
	OPTS="$RPM_OPT_FLAGS -Wall"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_applnkdir}/DockApplets} 

install -s %{name}/%{name} $RPM_BUILD_ROOT%{_bindir}
install %{SOURCE1} $RPM_BUILD_ROOT%{_applnkdir}/DockApplets

gzip -9nf Bugs Changelog README CREDITS

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc {Bugs,Changelog,README,CREDITS}.gz

%attr(755,root,root) %{_bindir}/%{name}

%{_applnkdir}/DockApplets/%{name}.desktop
