Summary:	Miscellaneous utilities specific to Debian
Name:		debianutils
Version:	2.30
Release:	0.1
License:	GPL v2+ / distributale
Group:		Base
Source0:	http://ftp.debian.org/debian/pool/main/d/debianutils/%{name}_%{version}.tar.gz
# Source0-md5:	7e989a8b0562054aea22c654507f2cb5
URL:		http://git.debian.org/?p=private/schizo/debianutils.git
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This package provides a number of small utilities which are used
primarily by the installation scripts of Debian packages, although you
may use them directly.

The specific utilities included are: installkernel mkboot run-parts
savelog sensible-browser sensible-editor sensible-pager tempfile
which.

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
rm -rf $RPM_BUILD_ROOT{%{_bindir},%{_mandir}/{fr/,}man1}/which*

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/run-parts
%attr(755,root,root) %{_bindir}/savelog
%attr(755,root,root) %{_bindir}/sensible-browser
%attr(755,root,root) %{_bindir}/sensible-editor
%attr(755,root,root) %{_bindir}/sensible-pager
%attr(755,root,root) %{_bindir}/tempfile
%attr(755,root,root) %{_sbindir}/add-shell
%attr(755,root,root) %{_sbindir}/installkernel
%attr(755,root,root) %{_sbindir}/mkboot
%attr(755,root,root) %{_sbindir}/remove-shell
%{_mandir}/man1/sensible-editor.1*
%{_mandir}/man1/tempfile.1*
%{_mandir}/man8/add-shell.8*
%{_mandir}/man8/installkernel.8*
%{_mandir}/man8/mkboot.8*
%{_mandir}/man8/remove-shell.8*
%{_mandir}/man8/run-parts.8*
%{_mandir}/man8/savelog.8*
%lang(fr) %{_mandir}/fr/man1/sensible-editor.1*
%lang(fr) %{_mandir}/fr/man1/tempfile.1*
%lang(fr) %{_mandir}/fr/man8/add-shell.8*
%lang(fr) %{_mandir}/fr/man8/installkernel.8*
%lang(fr) %{_mandir}/fr/man8/mkboot.8*
%lang(fr) %{_mandir}/fr/man8/remove-shell.8*
%lang(fr) %{_mandir}/fr/man8/run-parts.8*
%lang(fr) %{_mandir}/fr/man8/savelog.8*
