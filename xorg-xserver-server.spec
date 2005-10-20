# TODO:
# - Xdmx DDX (now disabled in configure)
#
Summary:	X.org server
Summary(pl):	Serwer X.org
Name:		xorg-xserver-server
Version:	0.99.2
Release:	0.01
License:	MIT
Group:		X11/Applications
Source0:	http://xorg.freedesktop.org/releases/X11R7.0-RC1/xserver/xorg-server-%{version}.tar.bz2
# Source0-md5:	8467f86e0832a5c532b30387c82d1e49
Source1:	http://dl.sourceforge.net/mesa3d/MesaLib-6.3.2.tar.bz2
# Source1-md5:	0df27701df0924d17ddf41185efa8ce1
Patch0:		%{name}-ncurses.patch
URL:		http://xorg.freedesktop.org/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libdrm
BuildRequires:	ncurses-devel
BuildRequires:	pkgconfig >= 0.19
BuildRequires:	xorg-lib-libfontenc-devel
BuildRequires:	xorg-lib-libXau-devel
BuildRequires:	xorg-lib-libXaw-devel
BuildRequires:	xorg-lib-libXfont-devel
BuildRequires:	xorg-lib-libXmu-devel
BuildRequires:	xorg-lib-libXpm-devel
BuildRequires:	xorg-lib-libXt-devel
BuildRequires:	xorg-lib-libXxf86dga-devel
BuildRequires:	xorg-lib-libXxf86misc-devel
BuildRequires:	xorg-lib-libXxf86vm-devel
BuildRequires:	xorg-lib-libxkbfile-devel
BuildRequires:	xorg-lib-libxkbui-devel
BuildRequires:	xorg-lib-xtrans-devel
BuildRequires:	xorg-proto-bigreqsproto-devel
BuildRequires:	xorg-proto-compositeproto-devel
BuildRequires:	xorg-proto-damageproto-devel
BuildRequires:	xorg-proto-fixesproto-devel
BuildRequires:	xorg-proto-fontsproto-devel
BuildRequires:	xorg-proto-glproto-devel
BuildRequires:	xorg-proto-randrproto-devel
BuildRequires:	xorg-proto-recordproto-devel
BuildRequires:	xorg-proto-renderproto-devel
BuildRequires:	xorg-proto-resourceproto-devel
BuildRequires:	xorg-proto-scrnsaverproto-devel
BuildRequires:	xorg-proto-videoproto-devel
BuildRequires:	xorg-proto-xcmiscproto-devel
BuildRequires:	xorg-proto-xextproto-devel
BuildRequires:	xorg-proto-xf86bigfontproto-devel
BuildRequires:	xorg-proto-xf86driproto-devel
BuildRequires:	xorg-proto-xf86miscproto-devel
BuildRequires:	xorg-proto-xf86vidmodeproto-devel
BuildRequires:	xorg-proto-xineramaproto-devel
BuildRequires:	xorg-proto-xproto-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
X.org server

%description -l pl
Serwer X.org

%package devel
Summary:	Header files for X.org server
Summary(pl):	Pliki nag³ówkowe dla servera X.org
Group:		X11/Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header files for X.org server.

%description devel -l pl
Pliki nag³ówkowe dla servera X.org.

%prep
%setup -q -a1 -n xorg-server-%{version}
%patch0 -p1

%build
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--with-mesa-source="`pwd`/Mesa-6.3.2"

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

rm $RPM_BUILD_ROOT%{_libdir}/xorg/modules/*/*{.la,.a}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/*
%{_includedir}/X11/*

# app-default should go to xorg-lib-libX11?
%{_libdir}/X11/*
# broken symlinks:
%exclude %{_libdir}/X11/xserver/C/print
%{_libdir}/xorg

%{_datadir}/X11/xkb/compiled

%{_mandir}/man1/*.1*
%{_mandir}/man4x/*.4x*
%{_mandir}/man5x/*.5x*

%files devel
%defattr(644,root,root,755)
%{_includedir}/xorg
%{_pkgconfigdir}/xorg-server.pc
