%global package_version 9.32.2

Name:           termius-app
Version:        %{package_version}
Release:        1%{?dist}
Summary:        Desktop SSH Client

License:        unknown
URL:            https://termius.com/
Source0:        https://termius.com/download/linux/Termius.deb

BuildRequires:  wget, tar
Requires:       gtk3, libnotify, nss, libXScrnSaver, libXtst, xdg-utils, at-spi2-core, libuuid, libsecret, libappindicator-gtk3

ExclusiveArch:  x86_64

%description
Desktop SSH Client

%prep
wget -O %{_sourcedir}/termius.deb https://termius.com/download/linux/Termius.deb
cd %{_builddir}
ar x %{_sourcedir}/termius.deb 

%install
mkdir -p %{buildroot}/opt/Termius
tar -xJf %{_builddir}/data.tar.xz -C %{buildroot}
chmod 4755 %{buildroot}/opt/Termius/chrome-sandbox

%files
/etc/cron.daily/termius-app
/opt/Termius/
%{_datadir}/applications/termius-app.desktop
%{_datadir}/icons/hicolor/
%{_datadir}/doc/termius-app/

%changelog