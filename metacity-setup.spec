Summary: Metacity window manager configuration program
Name: metacity-setup
Version: 0.6
Release: 3mdk
Source0: %{name}-%{version}.tar.bz2
License: GPL
Group: Graphical desktop/GNOME
BuildRoot: %{_tmppath}/%{name}-buildroot
Prefix: %{_prefix}
URL: http://plastercast.tzo.com/~plastercast/Projects/
Requires: metacity
BuildRequires: libgnomeui2-devel 

%description
metacity-setup is simply a much easier way to configure Metacity then
having to use gconftool or gconf-editor. It allows you to change
themes, focus settings, and the number of workspaces.


%prep
%setup -q

%build
%configure
%make

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall_std
mkdir -p $RPM_BUILD_ROOT%{_menudir}
cat << EOF > $RPM_BUILD_ROOT%{_menudir}/%{name} 
?package(%{name}): command="%{_bindir}/%name" icon="%{_datadir}/pixmaps/metacity-setup-icon.png" longtitle="Metacity Window Manager Properties" title="Metacity-Setup" needs=gnome section="Configuration/GNOME"
EOF

%clean
rm -rf $RPM_BUILD_ROOT

%post
%{update_menus}

%postun
%{clean_menus}


%files
%defattr(-,root,root)
%doc README AUTHORS ChangeLog
%_bindir/metacity-setup
%_datadir/pixmaps/metacity-setup-icon.png
%_datadir/metacity-setup/pixmaps/metacity-setup-icon.png
%_datadir/control-center-2.0/capplets/metacity-setup.desktop
%_menudir/%name

%changelog
* Mon Jul 22 2002 Frederic Crozat <fcrozat@mandrakesoft.com> 0.6-3mdk
- Fix menu entry

* Tue Jul 09 2002 Lenny Cartier <lenny@mandrakesoft.com> 0.6-2mdk
- buildrequires libgtk+-x11-2.0_0-devel

* Tue Jul  2 2002 Götz Waschk <waschk@linux-mandrake.com> 0.6-1mdk
- initial package
