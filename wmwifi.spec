Summary:	A dockapp to monitor wireless network signal strength
Summary(pl.UTF-8):	Aplet monitorujący siłę sygnału sieci bezprzewodowej
Name:		wmwifi
Version:	0.6
Release:	1
License:	GPL
Group:		X11/Window Managers/Tools
Source0:	http://digitalssg.net/debian/%{name}-%{version}.tar.gz
# Source0-md5:	b170d4a6c4fc42774b9798cf98af1c27
Source1:	%{name}.desktop
Patch0:		%{name}-include.patch
URL:		http://wmwifi.digitalssg.net/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
wmwifi monitors the first wireless network interface displaying the
signal strength between card and wireless access point as a
percentage, and has an LCD look-alike user interface.

%description -l pl.UTF-8
wmwifi monitoruje pierwszy interfejs sieci bezprzewodowej wyświetlając
w procentach siłę sygnału pomiędzy kartą a punktem dostępowym.
Posiada interfejs użytkownika przypominający wyświetlacz LCD.

%prep
%setup -q
%patch0 -p1

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
