Summary:	Metacity window manager configuration program
Name:		metacity-setup
Version:	0.6.1
Release:	1
License:	GPL
Group:		X11/Applications
Source0:	http://plastercast.tzo.com/~plastercast/Projects/%{name}-%{version}.tar.gz
URL:		http://plastercast.tzo.com/~plastercast/Projects/
BuildRequires:	libgnomeui-devel
Requires:	metacity
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix  /usr/X11R6/bin

%description
metacity-setup is simply a much easier way to configure Metacity then
having to use gconftool or gconf-editor. It allows you to change
themes, focus settings, and the number of workspaces.

%description -l pl
U¿ycie metacity-setup jest du¿o prostszym sposobem na skonfigurowanie
Metacity ni¿ u¿ywanie gconftoola lub gconf-editora. metacity-setup
pozwala na zmianê motywów, ustawieñ focusa i liczby ekranów
wirtualnych.

%prep
%setup -q

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} DESTDIR=$RPM_BUILD_ROOT install


%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README AUTHORS ChangeLog
%{_bindir}/metacity-setup
%{_pixmapsdir}/metacity-setup-icon.png
%dir %{_datadir}/metacity-setup
%dir %{_datadir}/metacity-setup/pixmaps
%{_datadir}/metacity-setup/pixmaps/metacity-setup-icon.png
%{_datadir}/control-center-2.0/capplets/metacity-setup.desktop
%{_menudir}/%{name}
