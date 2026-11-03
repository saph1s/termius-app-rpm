%global package_version 10.3.0

Name:           termius-app
Version:        %{package_version}
Release:        2%{?dist}
Summary:        Desktop SSH Client

License:        unknown
URL:            https://termius.com/
Source0:        https://termius.com/download/linux/Termius.deb

BuildRequires:  wget, tar, zlib, binutils
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
%ifarch x86_64
rm -f "%{buildroot}/opt/Termius/resources/app.asar.unpacked/node_modules/@termius/minidump-parser/target/minidump-parser.linux-arm64-gnu.node"
%endif
chmod 4755 %{buildroot}/opt/Termius/chrome-sandbox

%files
/etc/cron.daily/termius-app
/opt/Termius/
%{_datadir}/applications/termius-app.desktop
%{_datadir}/icons/hicolor/
%{_datadir}/doc/termius-app/

%changelog