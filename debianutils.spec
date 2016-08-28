Summary:	Miscellaneous utilities specific to Debian
Summary(pl.UTF-8):	Różne narzędzia specyficzne dla Debiana
Name:		debianutils
Version:	4.8
Release:	1
License:	GPL v2+, distributale
Group:		Applications
Source0:	http://ftp.debian.org/debian/pool/main/d/debianutils/%{name}_%{version}.tar.xz
# Source0-md5:	66a37e5ff17be431319bd0b43e9a46b5
URL:		http://git.debian.org/?p=private/schizo/debianutils.git
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This package provides a number of small utilities which are used
primarily by the installation scripts of Debian packages, although you
may use them directly.

The specific utilities included are: add-shell installkernel ischroot
remove-shell savelog tempfile.

%description -l pl.UTF-8
Ten pakiet udostępnia kilka małych narzędzi które są używane głównie
przez skrypty instalacyjne pakietów Debiana, aczkolwiek możesz używać
ich bezpośrednio.

Te specyficzne narzędzia to: add-shell installkernel ischroot
remove-shell savelog tempfile.

%prep
%setup -q

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

# which.spec is more advanced and is binary
%{__rm} -r $RPM_BUILD_ROOT{%{_bindir},%{_mandir}/{*/,}man1}/which*

# run-parts is contained in rc-scripts
%{__rm} $RPM_BUILD_ROOT{%{_bindir},%{_mandir}/{*/,}man8}/run-parts*

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/ischroot
%attr(755,root,root) %{_bindir}/savelog
%attr(755,root,root) %{_bindir}/tempfile
%attr(755,root,root) %{_sbindir}/add-shell
%attr(755,root,root) %{_sbindir}/installkernel
%attr(755,root,root) %{_sbindir}/remove-shell
%{_mandir}/man1/ischroot.1*
%{_mandir}/man1/tempfile.1*
%{_mandir}/man8/add-shell.8*
%{_mandir}/man8/installkernel.8*
%{_mandir}/man8/remove-shell.8*
%{_mandir}/man8/savelog.8*
%lang(de) %{_mandir}/de/man1/tempfile.1*
%lang(de) %{_mandir}/de/man8/add-shell.8*
%lang(de) %{_mandir}/de/man8/installkernel.8*
%lang(de) %{_mandir}/de/man8/remove-shell.8*
%lang(de) %{_mandir}/de/man8/savelog.8*
%lang(es) %{_mandir}/es/man1/tempfile.1*
%lang(es) %{_mandir}/es/man8/add-shell.8*
%lang(es) %{_mandir}/es/man8/installkernel.8*
%lang(es) %{_mandir}/es/man8/remove-shell.8*
%lang(es) %{_mandir}/es/man8/savelog.8*
%lang(fr) %{_mandir}/fr/man1/tempfile.1*
%lang(fr) %{_mandir}/fr/man8/add-shell.8*
%lang(fr) %{_mandir}/fr/man8/installkernel.8*
%lang(fr) %{_mandir}/fr/man8/remove-shell.8*
%lang(fr) %{_mandir}/fr/man8/savelog.8*
%lang(it) %{_mandir}/it/man1/tempfile.1*
%lang(it) %{_mandir}/it/man8/add-shell.8*
%lang(it) %{_mandir}/it/man8/installkernel.8*
%lang(it) %{_mandir}/it/man8/remove-shell.8*
%lang(it) %{_mandir}/it/man8/savelog.8*
%lang(ja) %{_mandir}/ja/man1/tempfile.1*
%lang(ja) %{_mandir}/ja/man8/add-shell.8*
%lang(ja) %{_mandir}/ja/man8/installkernel.8*
%lang(ja) %{_mandir}/ja/man8/remove-shell.8*
%lang(ja) %{_mandir}/ja/man8/savelog.8*
%lang(pl) %{_mandir}/pl/man1/tempfile.1*
%lang(pl) %{_mandir}/pl/man8/add-shell.8*
%lang(pl) %{_mandir}/pl/man8/installkernel.8*
%lang(pl) %{_mandir}/pl/man8/remove-shell.8*
%lang(pl) %{_mandir}/pl/man8/savelog.8*
%lang(sl) %{_mandir}/sl/man1/tempfile.1*
%lang(sl) %{_mandir}/sl/man8/add-shell.8*
%lang(sl) %{_mandir}/sl/man8/installkernel.8*
%lang(sl) %{_mandir}/sl/man8/remove-shell.8*
%lang(sl) %{_mandir}/sl/man8/savelog.8*
