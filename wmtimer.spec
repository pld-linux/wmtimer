Summary:	wmtimer - dockable alarm clock for WindowMaker
Summary(pl.UTF-8):	wmtimer - dokowalny czasomierz z alarmem dla WindowMakera
Name:		wmtimer
Version:	2.92
Release:	2
License:	GPL
Group:		X11/Window Managers/Tools
Source0:	http://www.darkops.net/wmtimer/%{name}-%{version}.tar.gz
# Source0-md5:	425bbb4b0cc852f858da025538d7c900
Source1:	%{name}.desktop
Patch0:		%{name}-opts.patch
URL:		http://www.darkops.net/wmtimer/
BuildRequires:	gtk+2-devel >= 2:2.2.0
BuildRequires:	pkgconfig
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)


%description
Wmtimer is a dockable alarm clock for WindowMaker. Wmtimer can be run
in alarm, coutdown timer, or chronograph mode. In alarm or timer mode
you can either execute a command or sound the system bell when the
time is reached, and it is configurable through the command line or
the GTK+ GUI.

%description -l pl.UTF-8
Wmtimer jest dokowalnym czasomierzem z alarmem dla WindowMakera. Może
być uruchamiany w trybie 'budzika', stopera odliczającego w dół, lub
chronometru. Dwa pierwsze tryby pozwalają na wykonanie polecenia lub
wysłanie sygnału dźwiękowego w wyznaczonym czasie. Program umożliwia
konfigurowanie określonych funkcji przez graficzny interfejs w GTK+ lub
bezpośrednio w linii poleceń.

%prep
%setup -q
%patch0 -p1

%build
%{__make} clean -C %{name}
%{__make} -C %{name} \
	OPTS="%{rpmcflags} -Wall"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_desktopdir}/docklets}

install %{name}/%{name} $RPM_BUILD_ROOT%{_bindir}
install %{SOURCE1} $RPM_BUILD_ROOT%{_desktopdir}/docklets

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changelog README CREDITS
%attr(755,root,root) %{_bindir}/%{name}
%{_desktopdir}/docklets/%{name}.desktop
