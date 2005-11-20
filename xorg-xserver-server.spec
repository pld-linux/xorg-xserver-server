# TODO:
# - Xdmx DDX (now disabled in configure)
#
Summary:	X.org server
Summary(pl):	Serwer X.org
Name:		xorg-xserver-server
Version:	0.99.3
Release:	0.1
License:	MIT
Group:		X11/Applications
Source0:	http://xorg.freedesktop.org/releases/X11R7.0-RC2/xserver/xorg-server-%{version}.tar.bz2
# Source0-md5:	82a9ccf391ee2473c456407a8eceda2d
Source1:	http://dl.sourceforge.net/mesa3d/MesaLib-6.4.tar.bz2
Patch0:		%{name}-ncurses.patch
URL:		http://xorg.freedesktop.org/
# for glx headers
BuildRequires:	Mesa-libGL-devel
BuildRequires:	autoconf >= 2.57
BuildRequires:	automake
BuildRequires:	cpp
BuildRequires:	libdrm-devel
BuildRequires:	libtool
BuildRequires:	ncurses-devel
BuildRequires:	perl-base
BuildRequires:	pkgconfig >= 1:0.19
BuildRequires:	xorg-lib-libXau-devel
BuildRequires:	xorg-lib-libXaw-devel
BuildRequires:	xorg-lib-libXdmcp-devel
BuildRequires:	xorg-lib-libXfont-devel
BuildRequires:	xorg-lib-libXi-devel
BuildRequires:	xorg-lib-libXmu-devel
BuildRequires:	xorg-lib-libXpm-devel
BuildRequires:	xorg-lib-libXres-devel
BuildRequires:	xorg-lib-libXt-devel
BuildRequires:	xorg-lib-libXtst-devel
BuildRequires:	xorg-lib-libXxf86dga-devel
BuildRequires:	xorg-lib-libXxf86misc-devel
BuildRequires:	xorg-lib-libXxf86vm-devel
BuildRequires:	xorg-lib-libdmx-devel
BuildRequires:	xorg-lib-libfontenc-devel
BuildRequires:	xorg-lib-liblbxutil-devel
BuildRequires:	xorg-lib-libxkbfile-devel
BuildRequires:	xorg-lib-libxkbui-devel
BuildRequires:	xorg-lib-xtrans-devel
BuildRequires:	xorg-proto-bigreqsproto-devel
BuildRequires:	xorg-proto-compositeproto-devel
BuildRequires:	xorg-proto-damageproto-devel
BuildRequires:	xorg-proto-evieext-devel
BuildRequires:	xorg-proto-fixesproto-devel
BuildRequires:	xorg-proto-fontsproto-devel
BuildRequires:	xorg-proto-glproto-devel >= 1.4.1
BuildRequires:	xorg-proto-printproto-devel
BuildRequires:	xorg-proto-randrproto-devel
BuildRequires:	xorg-proto-recordproto-devel
BuildRequires:	xorg-proto-renderproto-devel
BuildRequires:	xorg-proto-resourceproto-devel
BuildRequires:	xorg-proto-scrnsaverproto-devel
BuildRequires:	xorg-proto-trapproto-devel
BuildRequires:	xorg-proto-videoproto-devel
BuildRequires:	xorg-proto-xcmiscproto-devel
BuildRequires:	xorg-proto-xextproto-devel
BuildRequires:	xorg-proto-xf86bigfontproto-devel
BuildRequires:	xorg-proto-xf86dgaproto-devel
BuildRequires:	xorg-proto-xf86driproto-devel
BuildRequires:	xorg-proto-xf86miscproto-devel
BuildRequires:	xorg-proto-xf86vidmodeproto-devel
BuildRequires:	xorg-proto-xineramaproto-devel
BuildRequires:	xorg-proto-xproto-devel
BuildRequires:	xorg-util-util-macros >= 0.99.1
# for rgb.txt
Requires:	xorg-app-rgb
Requires:	xorg-app-xkbcomp
# just for %{_includedir}/bitmaps dir
Requires:	xorg-data-xbitmaps
Requires:	xorg-data-xkbdata
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
X.org server.

%description -l pl
Serwer X.org.

%package devel
Summary:	Header files for X.org server
Summary(pl):	Pliki nag³ówkowe dla servera X.org
Group:		X11/Development/Libraries
Requires:	libdrm-devel
Requires:	xorg-proto-fontsproto-devel
Requires:	xorg-proto-renderproto-devel
Requires:	xorg-proto-videoproto-devel
Requires:	xorg-proto-xextproto-devel

%description devel
Header files for X.org server.

%description devel -l pl
Pliki nag³ówkowe dla serwera X.org.

%prep
%setup -q -a1 -n xorg-server-%{version}
%patch0 -p1

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--enable-dga \
	--enable-lbx \
	--enable-xevie \
	--enable-xtrap \
	--with-default-font-path="%{_fontsdir}/misc,%{_fontsdir}/TTF,%{_fontsdir}/OTF,%{_fontsdir}/Type1,%{_fontsdir}/CID,%{_fontsdir}/100dpi,%{_fontsdir}/75dpi" \
	--with-mesa-source="`pwd`/Mesa-6.4"

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	appmandir=%{_mandir}/man1 \
	drivermandir=%{_mandir}/man4 \
	filemandir=%{_mandir}/man5

rm -f $RPM_BUILD_ROOT%{_libdir}/xorg/modules/{*,*/*}.{la,a}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog
%attr(755,root,root) %{_bindir}/*
%{_includedir}/X11/bitmaps/*
%{_includedir}/X11/pixmaps
%{_libdir}/X11/Cards
%{_libdir}/X11/app-defaults/*
%{_libdir}/X11/getconfig
%{_libdir}/X11/xserver
# broken symlinks:
%exclude %{_libdir}/X11/xserver/C/print
%dir %{_libdir}/xorg
%dir %{_libdir}/xorg/modules
%attr(755,root,root) %{_libdir}/xorg/modules/lib*.so
%dir %{_libdir}/xorg/modules/extensions
%attr(755,root,root) %{_libdir}/xorg/modules/extensions/libdri.so
%dir %{_libdir}/xorg/modules/linux
%attr(755,root,root) %{_libdir}/xorg/modules/linux/libdrm.so
%dir %{_libdir}/xorg/modules/multimedia
%attr(755,root,root) %{_libdir}/xorg/modules/multimedia/*.so
%{_datadir}/X11/xkb/compiled
%dir %{_libdir}/xserver
%{_libdir}/xserver/SecurityPolicy
%{_mandir}/man1/*.1*
%{_mandir}/man4/*.4x*
%{_mandir}/man5/*.5x*

%files devel
%defattr(644,root,root,755)
%{_includedir}/xorg
%{_aclocaldir}/xorg-server.m4
%{_pkgconfigdir}/xorg-server.pc
