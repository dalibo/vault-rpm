%global debug_package %{nil}
%{!?pkgrevision: %global pkgrevision 1}

Name: vault
Version: %{pkgversion}
Release: %{pkgrevision}%{?dist}
Summary: A tool for secrets management
License: MPLv2.0
URL: https://www.vaultproject.io/
Source0: vault_%{version}_linux_amd64.zip
Source1: vault.hcl
Source2: vault.service
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildArch: x86_64

%description
Vault is a tool for secrets management, encryption as a service, and
privileged access management.

%prep
%setup -c -n %{name}-%{version}
%{__cp} %{_sourcedir}/vault.hcl %{_builddir}/%{name}-%{version}
%{__cp} %{_sourcedir}/vault.service %{_builddir}/%{name}-%{version}

%build

%install
%{__install} -d -m 750 %{buildroot}/var/lib/vault
%{__install} -d -m 750 %{buildroot}/var/log/vault
%{__install} -d -m 755 %{buildroot}/usr/bin
%{__install} -m 755 vault %{buildroot}/usr/bin/vault

%{__install} -d -m 750 %{buildroot}/etc/vault
%{__install} -m 640 vault.hcl %{buildroot}/etc/vault/vault.hcl
%{__install} -d %{buildroot}%{_unitdir}
%{__install} -m 644 vault.service %{buildroot}%{_unitdir}/vault.service

%pre
useradd -r -m -d /var/lib/vault -s /bin/false -c "Vault Server" vault >/dev/null 2>&1 || :

%post
setcap cap_ipc_lock=+ep /usr/bin/vault

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-,vault,vault)
%attr(-,root,root)/usr/bin/vault
%dir /etc/vault
%config(noreplace) /etc/vault/vault.hcl
/var/lib/vault
/var/log/vault
%attr(-,root,root) %{_unitdir}/vault.service

%changelog
* Tue Jan 14 2020 Nicolas Thauvin <nicolas.thauvin@dalibo.com> - 1.3.1-1
- Initial release
