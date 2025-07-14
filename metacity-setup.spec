Summary:	Metacity window manager configuration program
Summary(pl.UTF-8):	Program konfiguracyjny dla zarządcy okien Metacity
Name:		metacity-setup
Version:	0.7.1
Release:	4
License:	GPL
Group:		X11/Applications
Source0:	http://dl.sourceforge.net/sourceforge/%{name}/%{name}-%{version}.tar.gz
# Source0-md5:	e898a13ea95d38dcc1f9dba5dd03581f
Patch0:		%{name}-themes_path.patch
URL:		http://sourceforge.net/projects/metacity-setup/
BuildRequires:	GConf2-devel >= 1.2.0
BuildRequires:	autoconf
BuildRequires:	gnome-vfs2-devel >= 2.0.1
BuildRequires:	gtk+2-devel >= 1:2.0.5
BuildRequires:	intltool
BuildRequires:	libglade2-devel >= 2.0.0
BuildRequires:	libgnomeui-devel >= 2.3.3.1-2
BuildRequires:	pkgconfig
Requires:	metacity
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
metacity-setup is simply a much easier way to configure Metacity then
having to use gconftool or gconf-editor. It allows you to change
themes, focus settings, and the number of workspaces.

%description -l pl.UTF-8
Użycie metacity-setup jest dużo prostszym sposobem na skonfigurowanie
Metacity niż używanie gconftoola lub gconf-editora. metacity-setup
pozwala na zmianę motywów, ustawień focusa i liczby ekranów
wirtualnych.

%prep
%setup -q
%patch -P0 -p1

%build
%{__autoconf}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README AUTHORS ChangeLog
%attr(755,root,root) %{_bindir}/*
%{_pixmapsdir}/metacity-setup-icon.png
%dir %{_datadir}/metacity-setup
%dir %{_datadir}/metacity-setup/pixmaps
%{_datadir}/metacity-setup/pixmaps/metacity-setup-icon.png
%{_datadir}/control-center-2.0/capplets/metacity-setup.desktop
