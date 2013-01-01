
Name: app-samba-common
Epoch: 1
Version: 1.4.14
Release: 1%{dist}
Summary: Samba Common - Core
License: LGPLv3
Group: ClearOS/Libraries
Source: app-samba-common-%{version}.tar.gz
Buildarch: noarch

%description
The Samba Common app provides base libraries that can be used in both Samba 3 and Samba 4

%package core
Summary: Samba Common - Core
Requires: app-base-core

%description core
The Samba Common app provides base libraries that can be used in both Samba 3 and Samba 4

This package provides the core API and libraries.

%prep
%setup -q
%build

%install
mkdir -p -m 755 %{buildroot}/usr/clearos/apps/samba_common
cp -r * %{buildroot}/usr/clearos/apps/samba_common/

install -d -m 0775 %{buildroot}/var/clearos/samba_common/lock

%post core
logger -p local6.notice -t installer 'app-samba-common-core - installing'

if [ $1 -eq 1 ]; then
    [ -x /usr/clearos/apps/samba_common/deploy/install ] && /usr/clearos/apps/samba_common/deploy/install
fi

[ -x /usr/clearos/apps/samba_common/deploy/upgrade ] && /usr/clearos/apps/samba_common/deploy/upgrade

exit 0

%preun core
if [ $1 -eq 0 ]; then
    logger -p local6.notice -t installer 'app-samba-common-core - uninstalling'
    [ -x /usr/clearos/apps/samba_common/deploy/uninstall ] && /usr/clearos/apps/samba_common/deploy/uninstall
fi

exit 0

%files core
%defattr(-,root,root)
%exclude /usr/clearos/apps/samba_common/packaging
%exclude /usr/clearos/apps/samba_common/tests
%dir /usr/clearos/apps/samba_common
%dir %attr(0775,root,webconfig) /var/clearos/samba_common/lock
/usr/clearos/apps/samba_common/deploy
/usr/clearos/apps/samba_common/language
/usr/clearos/apps/samba_common/libraries
