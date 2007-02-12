Summary:	DVR-like media player
Summary(pl.UTF-8):	Odtwarzacz multimedialny w stylu DVR
Name:		elation
Version:	0.0.1.001
%define	_snap	20050701
Release:	0.%{_snap}.0.1
License:	BSD
Group:		X11/Applications
#Source0:	http://dl.sourceforge.net/enlightenment/%{name}-%{version}.tar.gz
Source0:	http://sparky.homelinux.org/snaps/enli/e17/apps/%{name}-%{_snap}.tar.gz
# Source0-md5:	f24d1a01e2ca6d258abc04e198f07aab
URL:		http://enlightenment.org/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	ecore-devel
BuildRequires:	embryo-devel
BuildRequires:	emotion-devel
BuildRequires:	libtool
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Elation is a DVR-like media player.

%description -l pl.UTF-8
Elation to odtwarzacz multimedialny w stylu DVR.

%prep
%setup -q -n %{name}

%build
%{__libtoolize}
%{__aclocal} -I m4
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--disable-static
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS COPYING README
%attr(755,root,root) %{_bindir}/%{name}
%dir %{_libdir}/%{name}
%attr(755,root,root) %{_libdir}/%{name}/*.so
%{_datadir}/%{name}
