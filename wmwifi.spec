Summary:	A dockapp to monitor wireless network signal strength
Summary(pl):	Aplet monitoruj±cy si³ê sygna³u sieci bezprzewodowej
Name:		wmwifi
Version:	0.4
Release:	1
License:	GPL
Group:		X11/Window Managers/Tools
Source0:	http://digitalssg.net/debian/%{name}-%{version}.tar.gz
# Source0-md5:	b367d1180f83729b6edb6a4466f8a4b8
Source1:	%{name}.desktop
URL:		http://wmwifi.digitalssg.net/
BuildRequires:	XFree86-devel
BuildRequires:	autoconf
BuildRequires:	automake
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
wmwifi monitors the first wireless network interface displaying the
signal strength between card and wireless access point as a
percentage, and has an LCD look-alike user interface.

%description -l pl
wmwifi monitoruje pierwszy interfejs sieci bezprzewodowej wy¶wietlaj±c
w procentach si³ê sygna³u pomiêdzy kart± a punktem dostêpowym.
Posiada interfejs u¿ytkownika przypominaj±cy wy¶wietlacz LCD.

%prep
%setup -q

%build
%{__aclocal}
%{__autoconf}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_desktopdir}/docklets

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install %{SOURCE1} $RPM_BUILD_ROOT%{_desktopdir}/docklets

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README
%attr(755,root,root) %{_bindir}/*
%{_desktopdir}/docklets/*
%{_mandir}/man1/%{name}.1*
