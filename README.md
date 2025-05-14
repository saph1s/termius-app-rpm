# termius-app-rpm

Port of the [Termius](https://www.termius.com/) app for Linux using the RPM package format.

## Installation

You can install the RPM package from copr repository:

```bash
sudo dnf copr enable saph1s/termius-app
sudo dnf install termius-app
```

## How to build

1. Clone the repository:

```bash
git clone https://github.com/saph1s/termius-app-rpm && cd termius-app-rpm
```

2. Install the required dependencies:

```bash
sudo dnf install -y rpmdevtools rpm-build
```

3. Set up the RPM build environment:

```bash
rpmdev-setuptree
```

4. Build the RPM package:

```bash
rpmbuild -bb termius.spec
```

5. Install the RPM package:

```bash
sudo dnf install ~/rpmbuild/RPMS/x86_64/termius-*.rpm
```
