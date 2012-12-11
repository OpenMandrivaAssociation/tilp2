Name: tilp2
Url: http://lpg.ticalc.org/prj_tilp
Version: 1.16
Release: 1
Source0: http://downloads.sourceforge.net/project/tilp/tilp2-linux/tilp2-1.16/%{name}-%{version}.tar.bz2
Group: Communications
License: GPLv2+

BuildRequires: pkgconfig(libusb) pkgconfig(tifiles2) pkgconfig(ticalcs2) pkgconfig(ticonv)
BuildRequires: glade pkgconfig(libglade-2.0)
Requires: xdg-utils >= 1.0.0
Summary: TiLP is a TI<->PC linking program

%description
TiLP is a TI<->PC linking program

%prep
%setup

%build
%configure2_5x
%make

%install
%makeinstall_std
mkdir -p %buildroot/usr/share/applications
cat >%buildroot/usr/share/applications/tilp.desktop <<EOF
[Desktop Entry]
Name=TiLP
Name[fr_FR]=TiLP
Comment=Ti Linking Program
Comment[fr_FR]=Programme de connexion pour calculatrices TI
GenericName=TI Linking Program
GenericName[fr_FR]=Connexion calculatrices TI
Encoding=UTF-8
Version=1.0
Type=Application
Exec=/usr/bin/tilp
Icon=/usr/share/tilp2/pixmaps/icon.xpm
Terminal=false
Categories=Utility;X-KDE-Utilities-Peripherals;
MimeType=application/x-tilp
EOF
desktop-file-install --delete-original --vendor lpg     \
  --dir ${RPM_BUILD_ROOT}%{_datadir}/applications          \
  ${RPM_BUILD_ROOT}/usr/share/applications/tilp.desktop
mkdir -p ${RPM_BUILD_ROOT}%{_datadir}/mime/packages
cat >${RPM_BUILD_ROOT}%{_datadir}/mime/packages/tilp.xml <<EOF
<?xml version="1.0" encoding="UTF-8"?>
<mime-info xmlns="http://www.freedesktop.org/standards/shared-mime-info">
    <mime-type type="application/x-tilp">
        <comment xml:lang="en">TI File</comment>
        <comment xml:lang="fr">Fichier TI</comment>
        <glob pattern="*.73?" />
        <glob pattern="*.82?" />
        <glob pattern="*.8[xX]?" />
        <glob pattern="*.85?" />
        <glob pattern="*.86?" />
        <glob pattern="*.89?" />
        <glob pattern="*.92?" />
        <glob pattern="*.9[xX]?" />
        <glob pattern="*.[vV]2?" />
  </mime-type>
</mime-info>
EOF

%post
update-mime-database %{_datadir}/mime > /dev/null 2>&1 || :
update-desktop-database %{_datadir}/applications > /dev/null 2>&1 || :

%postun
update-mime-database %{_datadir}/mime > /dev/null 2>&1 || :
update-desktop-database %{_datadir}/applications > /dev/null 2>&1 || :

%files
%{_bindir}/tilp
#% {_mandir}/man1/tilp*
%{_datadir}/tilp2
%{_datadir}/applications/lpg-tilp.desktop
%{_datadir}/mime/packages/tilp.xml
%{_datadir}/locale/fr/LC_MESSAGES/*.mo


%changelog
* Mon Feb 20 2012 Alexander Khrukin <akhrukin@mandriva.org> 1.15-1
+ Revision: 778212
- test build without man
- files section fix
- imported package tilp2

