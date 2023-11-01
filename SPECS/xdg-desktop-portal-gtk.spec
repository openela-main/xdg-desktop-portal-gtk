# Required for xdp_impl_background_emit_running_applications_changed
%global xdg_desktop_portal_version 1.5.4

Name:           xdg-desktop-portal-gtk
Version:        1.8.0
Release:        1%{?dist}
Summary:        Backend implementation for xdg-desktop-portal using GTK+

License:        LGPLv2+
URL:            https://github.com/flatpak/%{name}
Source0:        https://github.com/flatpak/%{name}/releases/download/%{version}/%{name}-%{version}.tar.xz

BuildRequires:  make
BuildRequires:  gcc
BuildRequires:  gettext
BuildRequires:  pkgconfig(fontconfig)
BuildRequires:  pkgconfig(gnome-desktop-3.0)
BuildRequires:  pkgconfig(gsettings-desktop-schemas)
BuildRequires:  pkgconfig(gtk+-unix-print-3.0)
BuildRequires:  pkgconfig(xdg-desktop-portal) >= %{xdg_desktop_portal_version}
%{?systemd_requires}
BuildRequires:  systemd
Requires:       dbus
Requires:       xdg-desktop-portal >= %{xdg_desktop_portal_version}
%if 0%{?fedora}
# Use rich deps to pull in this package when gtk3 and flatpak (or snapd) are both installed
Supplements:    (gtk3 and (flatpak or snapd))
%endif

%description
A backend implementation for xdg-desktop-portal that is using GTK+ and various
pieces of GNOME infrastructure, such as the org.gnome.Shell.Screenshot or
org.gnome.SessionManager D-Bus interfaces.


%prep
%autosetup -p1


%build
%configure --disable-silent-rules
%make_build


%install
%make_install
%find_lang %{name}


%post
%systemd_user_post %{name}.service

%preun
%systemd_user_preun %{name}.service


%files -f %{name}.lang
%license COPYING
%doc NEWS
%{_libexecdir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/dbus-1/services/org.freedesktop.impl.portal.desktop.gtk.service
%{_datadir}/xdg-desktop-portal/portals/gtk.portal
%{_userunitdir}/%{name}.service



%changelog
* Sat Mar 26 2022 Debarshi Ray <rishi@fedoraproject.org> - 1.8.0-1
- Rebase to 1.8.0
- Remove unnecessary non-arch-specific explicit library Requires
Resolves: #2062432

* Mon May 25 2020 Jonas Ådahl <jadahl@redhat.com> - 1.6.0-1
- Rebase to 1.6.0 (#1837413)
- Bump supported Mutter screen cast API version (#1837413)
- Backport bugfix (#1837413)

* Sat Oct 26 2019 David King <dking@redhat.com> - 1.4.0-1
- Rebase to 1.4.0 (#1748335)

* Tue Sep 18 2018 Kalev Lember <klember@redhat.com> - 1.0.2-1
- Update to 1.0.2

* Tue Jul 31 2018 David King <dking@redhat.com> - 0.99-1
- Update to 0.99

* Wed Apr 25 2018 David King <amigadave@amigadave.com> - 0.11-1
- Update to 0.11 (#1545226)

* Wed Feb 14 2018 David King <amigadave@amigadave.com> - 0.10-1
- Update to 0.10 (#1545226)

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.9-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sun Nov 19 2017 David King <amigadave@amigadave.com> - 0.9-1
- Update to 0.9 (#1514775)

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.7-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Tue Jun 06 2017 David King <amigadave@amigadave.com> - 0.7-1
- Update to 0.7

* Fri Mar 31 2017 David King <amigadave@amigadave.com> - 0.6-1
- Update to 0.6

* Fri Feb 17 2017 Kalev Lember <klember@redhat.com> - 0.5-3
- Use rich deps to pull in this package when flatpak and gtk3 are both installed

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Jan 18 2017 David King <amigadave@amigadave.com> - 0.5-1
- Update to 0.5

* Fri Sep 02 2016 David King <amigadave@amigadave.com> - 0.3-1
- Update to 0.3

* Fri Jul 29 2016 David King <amigadave@amigadave.com> - 0.2-1
- Update to 0.2 (#1361576)

* Wed Jul 13 2016 David King <amigadave@amigadave.com> - 0.1-1
- Initial Fedora packaging
