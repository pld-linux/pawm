Summary:	pawm - Light Weight Window Manager
Summary(pl.UTF-8):	pawm - lekki zarządca okien
Name:		pawm
Version:	2.0.3
Release:	1
License:	GPL
Group:		X11/Window Managers
Source0:	http://www.pleyades.net/pawm/files/%{name}-%{version}.tar.gz
# Source0-md5:	578979a5d9f461d129769fa46e0bbbdd
Source1:	%{name}.desktop
URL:		http://www.pleyades.net/pawm/
BuildRequires:	XFree86-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Pawm is a window manager for the X Window system. So it's not a
'desktop' and doesn't offer you a huge pile of useless options, just
the facilities needed to run X applications.

%description -l pl.UTF-8
Pawm jest zarządcą okien dla X Window. Nie jest do 'desktop' i nie
oferuje ogromnej liczby bezużytecznych opcji, daje tylko możliwość
uruchamiania aplikacji X.

%prep
%setup -q

%build
./0 \
	--prefix=%{_prefix} \
	--libdir=%{_libdir} \
	--statedir=/var/%{_lib} \
	--xbindir=%{_libdir}/pawm
%{__make} \
	LD="%{__cc}" \
	GCC="%{__cc}" \
	CFLAGS="%{rpmcflags}" \
	LDFLAGS="%{rpmldflags} -L/usr/X11R6/%{_lib}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_datadir}/xsessions

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install %{SOURCE1} $RPM_BUILD_ROOT%{_datadir}/xsessions/%{name}.desktop

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS INSTALL README THANKS
%attr(755,root,root) %{_bindir}/*
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/%{name}.conf
%{_datadir}/%{name}
%{_datadir}/xsessions/%{name}.desktop
