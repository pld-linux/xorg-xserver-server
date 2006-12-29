Summary:	X.org server
Summary(pl):	Serwer X.org
Name:		xorg-xserver-server
Version:	1.1.99.903
Release:	0.4
License:	MIT
Group:		X11/Servers
Source0:	http://xorg.freedesktop.org/releases/individual/xserver/xorg-server-%{version}.tar.bz2
# Source0-md5:	aa7d6b3577d4d851faf1c591df490bd5
%define		mesa_version	6.5.2
Source1:	http://dl.sourceforge.net/mesa3d/MesaLib-%{mesa_version}.tar.bz2
# Source1-md5:	e4d894181f1859651658b3704633e10d
Source2:	xserver.pamd
Patch0:		%{name}-ncurses.patch
Patch1:		%{name}-symlinks.patch
Patch2:		%{name}-xwrapper.patch
Patch3:		%{name}-bug-5825.patch
Patch4:		%{name}-mesa-6.5.2.patch
Patch5:		%{name}-white_cube.patch
URL:		http://xorg.freedesktop.org/
# for glx headers
BuildRequires:	OpenGL-GLX-devel
BuildRequires:	autoconf >= 2.57
BuildRequires:	automake
BuildRequires:	cpp
BuildRequires:	libdrm-devel >= 2.3.0
BuildRequires:	libtool
BuildRequires:	ncurses-devel
BuildRequires:	pam-devel
BuildRequires:	perl-base
BuildRequires:	pkgconfig >= 1:0.19
BuildRequires:	xorg-app-mkfontscale
BuildRequires:	xorg-lib-libX11-devel
BuildRequires:	xorg-lib-libXau-devel
BuildRequires:	xorg-lib-libXaw-devel
BuildRequires:	xorg-lib-libXdmcp-devel
BuildRequires:	xorg-lib-libXext-devel
BuildRequires:	xorg-lib-libXfont-devel
BuildRequires:	xorg-lib-libXi-devel
BuildRequires:	xorg-lib-libXmu-devel
BuildRequires:	xorg-lib-libXpm-devel
BuildRequires:	xorg-lib-libXrender-devel
BuildRequires:	xorg-lib-libXres-devel
BuildRequires:	xorg-lib-libXt-devel >= 1.0.0
BuildRequires:	xorg-lib-libXtst-devel
BuildRequires:	xorg-lib-libXxf86dga-devel
BuildRequires:	xorg-lib-libXxf86misc-devel
BuildRequires:	xorg-lib-libXxf86vm-devel
BuildRequires:	xorg-lib-libdmx-devel
BuildRequires:	xorg-lib-libfontenc-devel
BuildRequires:	xorg-lib-liblbxutil-devel
BuildRequires:	xorg-lib-libxkbfile-devel
BuildRequires:	xorg-lib-libxkbui-devel >= 1.0.2
BuildRequires:	xorg-lib-xtrans-devel
BuildRequires:	xorg-proto-bigreqsproto-devel
BuildRequires:	xorg-proto-compositeproto-devel >= 0.3
BuildRequires:	xorg-proto-damageproto-devel
BuildRequires:	xorg-proto-dmxproto-devel
BuildRequires:	xorg-proto-evieext-devel
BuildRequires:	xorg-proto-fixesproto-devel >= 4.0
BuildRequires:	xorg-proto-fontcacheproto-devel
BuildRequires:	xorg-proto-fontsproto-devel
BuildRequires:	xorg-proto-glproto-devel >= 1.4.7
BuildRequires:	xorg-proto-inputproto-devel
BuildRequires:	xorg-proto-kbproto-devel >= 1.0.3
BuildRequires:	xorg-proto-printproto-devel
BuildRequires:	xorg-proto-randrproto-devel
BuildRequires:	xorg-proto-recordproto-devel
BuildRequires:	xorg-proto-renderproto-devel
BuildRequires:	xorg-proto-resourceproto-devel
BuildRequires:	xorg-proto-scrnsaverproto-devel >= 1.1.0
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
BuildRequires:	xorg-util-util-macros >= 0.99.2
# xcalibrateproto, tslib (for KDRIVE only)
# glitz-devel >= 0.4.3 (for XGL and EGL only)
# for rgb.txt
Requires:	xorg-app-rgb >= 0.99.3
Requires:	xorg-app-xkbcomp
# just for %{_includedir}/bitmaps dir
Requires:	xorg-data-xbitmaps
# xserver requires default fixed and cursosr fonts.
Requires:	xorg-font-font-alias
Requires:	xorg-font-font-cursor-misc
Requires:	xorg-font-font-misc-misc-base >= 1.0.0-0.3
# for new app-defaults location
Requires:	xorg-lib-libXt >= 1.0.0
Obsoletes:	X11-Xserver
Obsoletes:	X11-modules
Obsoletes:	XFree86-Xserver
Obsoletes:	XFree86-modules
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Xorg server is a generally used X server which uses display hardware.
It requires proper driver for your display hardware.

%description -l pl
Serwer Xorg to podstawowy serwer X wy¶wietlaj±cy obraz na karcie
graficznej. Do dzia³ania wymaga odpowiedniego sterownika.

%package -n xorg-xserver-Xdmx
Summary:	Xdmx - distributed multi-head X server
Summary(pl):	Xdmx - rozproszony, wielomonitorowy serwer X
Group:		X11/Servers

%description -n xorg-xserver-Xdmx
Xdmx - distributed multi-head X server.

%description -n xorg-xserver-Xdmx -l pl
Xdmx - rozproszony, wielomonitorowy serwer X.

%package -n xorg-xserver-Xnest
Summary:	Xnest - nested X server
Summary(pl):	Xnest - zagnie¿d¿ony serwer X
Group:		X11/Servers
Obsoletes:	X11-Xnest
Obsoletes:	XFree86-Xnest

%description -n xorg-xserver-Xnest
Xnest is an X Window System server which runs in an X window. Xnest is
a 'nested' window server, actually a client of the real X server,
which manages windows and graphics requests for Xnest, while Xnest
manages the windows and graphics requests for its own clients.

%description -n xorg-xserver-Xnest -l pl
Xnest jest serwerem X uruchamianym w okienku innego serwera X. Xnest
zachowuje siê jak klient X w stosunku do prawdziwego serwera X, a jak
serwer X dla w³asnych klientów.

%description -n xorg-xserver-Xnest -l ru
Xnest - ÜÔÏ ÓÅÒ×ÅÒ X Window System, ËÏÔÏÒÙÊ ÒÁÂÏÔÁÅÔ × ÏËÎÅ X. îÁ
ÓÁÍÏÍ ÄÅÌÅ ÜÔÏ ËÌÉÅÎÔ ÒÅÁÌØÎÏÇÏ X-ÓÅÒ×ÅÒÁ, ËÏÔÏÒÙÊ ÕÐÒÁ×ÌÑÅÔ ÏËÎÁÍÉ É
ÇÒÁÆÉÞÅÓËÉÍÉ ÚÁÐÒÏÓÁÍÉ ÄÌÑ Xnest × ÔÏ ×ÒÅÍÑ, ËÁË Xnest ÕÐÒÁ×ÌÑÅÔ
ÏËÎÁÍÉ É ÇÒÁÆÉÞÅÓËÉÍÉ ÚÁÐÒÏÓÁÍÉ ÄÌÑ Ó×ÏÉÈ ÓÏÂÓÔ×ÅÎÎÙÈ ËÌÉÅÎÔÏ×.

%description -n xorg-xserver-Xnest -l uk
Xnest - ÃÅ ÓÅÒ×ÅÒ X Window System, ÑËÉÊ ÐÒÁÃÀ¤ Õ ×¦ËÎ¦ X. æÁËÔÉÞÎÏ ÃÅ
ËÌ¦¤ÎÔ ÒÅÁÌØÎÏÇÏ X-ÓÅÒ×ÅÒÁ, ÑËÉÊ ËÅÒÕ¤ ×¦ËÎÁÍÉ ÔÁ ÇÒÁÆ¦ÞÎÉÍÉ ÚÁÐÉÔÁÍÉ
ÄÌÑ Xnest × ÔÏÊ ÞÁÓ, ÑË Xnest ËÅÒÕ¤ ×¦ËÎÁÍÉ ÔÁ ÇÒÁÆ¦ÞÎÉÍÉ ÚÁÐÉÔÁÍÉ ÄÌÑ
Ó×Ï§È ×ÌÁÓÎÉÈ ËÌ¦¤ÎÔ¦×.

%package -n xorg-xserver-Xprt
Summary:	Xprt - Xprint server for X
Summary(pl):	Xprt - serwer Xprint dla X
Group:		X11/Servers
Obsoletes:	X11-Xprt
Obsoletes:	XFree86-Xprt

%description -n xorg-xserver-Xprt
Xprt is the Xprint print server for X Window System for non display
devices such as printers and fax machines.

%description -n xorg-xserver-Xprt -l pl
Xprt to serwer wydruków Xprint dla X Window System dla urz±dzeñ nie
wy¶wietlaj±cych, takich jak drukarki czy faksy.

%package -n xorg-xserver-Xvfb
Summary:	Xvfb - virtual framebuffer X server
Summary(pl):	Xvfb - serwer X z wirtualnym framebufferem
Group:		X11/Servers
Obsoletes:	X11-Xvfb
Obsoletes:	XFree86-Xvfb

%description -n xorg-xserver-Xvfb
Xvfb (X Virtual Frame Buffer) is an X Window System server that is
capable of running on machines with no display hardware and no
physical input devices. Xvfb emulates a dumb framebuffer using virtual
memory. Xvfb doesn't open any devices, but behaves otherwise as an X
display. Xvfb is normally used for testing servers. Using Xvfb, the
mfb or cfb code for any depth can be exercised without using real
hardware that supports the desired depths. Xvfb has also been used to
test X clients against unusual depths and screen configurations, to do
batch processing with Xvfb as a background rendering engine, to do
load testing, to help with porting an X server to a new platform, and
to provide an unobtrusive way of running applications which really
don't need an X server but insist on having one.

%description -n xorg-xserver-Xvfb -l pl
Xvfb (X Virtual Frame Buffer) jest serwerem X, który mo¿na uruchamiaæ
na maszynach bez urz±dzeñ wy¶wietlaj±cych ani fizycznych urz±dzeñ
wej¶ciowych. Xvfb emuluje prosty framebuffer w pamiêci. Zwykle jest
u¿ywany do testowania serwerów X, mo¿e te¿ byæ u¿ywany do testowania
klientów X w rzadko u¿ywanych konfiguracjach ekranu. Mo¿na te¿ u¿yæ
Xvfb do uruchomienia aplikacji, które w rzeczywisto¶ci nie wymagaj±
serwera X, ale odmawiaj± uruchomienia bez niego.

%package devel
Summary:	Header files for X.org server
Summary(pl):	Pliki nag³ówkowe dla servera X.org
Group:		X11/Development/Libraries
Requires:	libdrm-devel >= 2.3.0
Requires:	xorg-proto-fontsproto-devel
Requires:	xorg-proto-renderproto-devel
Requires:	xorg-proto-videoproto-devel
Requires:	xorg-proto-xextproto-devel
Obsoletes:	X11-Xserver-devel
Obsoletes:	X11-XFree86-devel

%description devel
Header files for X.org server.

%description devel -l pl
Pliki nag³ówkowe dla serwera X.org.

%package -n xorg-xserver-libglx
Summary:	GLX extension library fo X.org server
Summary(pl):	Biblioteka rozszerzenia GLX dla serwera X.org
Group:		X11/Servers
Requires:	%{name} = %{version}-%{release}
Provides:	xorg-xserver-libglx(glapi) = %{mesa_version}
Provides:	xorg-xserver-modules-libglx
Obsoletes:	xorg-driver-video-nvidia

%description -n xorg-xserver-libglx
GLX extension library fo X.org server.

%description -n xorg-xserver-libglx -l pl
Biblioteka rozszerzenia GLX dla serwera X.org.

%prep
%setup -q -a1 -n xorg-server-%{version}
%patch0 -p1
%patch1 -p1
%patch2 -p0
%patch3 -p0
%patch4 -p1
%patch5 -p1

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--with-os-name="PLD/Linux" \
	--with-os-vendor="PLD/Team" \
	--enable-dga \
	--enable-builddocs \
	--enable-lbx \
	--enable-xevie \
	--with-dri-driver-path=%{_libdir}/xorg/modules/dri \
	--with-default-font-path="%{_fontsdir}/misc,%{_fontsdir}/TTF,%{_fontsdir}/OTF,%{_fontsdir}/Type1,%{_fontsdir}/100dpi,%{_fontsdir}/75dpi" \
	--with-mesa-source="`pwd`/Mesa-%{mesa_version}" \
	--with-xkb-output=/var/lib/xkb

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install -D %{SOURCE2} $RPM_BUILD_ROOT/etc/pam.d/xserver
install -d $RPM_BUILD_ROOT/etc/security/console.apps
install -d $RPM_BUILD_ROOT%{_libdir}/xorg/modules/{dri,drivers,input}
install hw/xfree86/parser/xf86Parser.h $RPM_BUILD_ROOT%{_includedir}/xorg/xf86Parser.h
install hw/xfree86/parser/xf86Optrec.h $RPM_BUILD_ROOT%{_includedir}/xorg/xf86Optrec.h
install hw/xfree86/parser/libxf86config.a $RPM_BUILD_ROOT%{_libdir}/libxf86config.a
:> $RPM_BUILD_ROOT/etc/security/console.apps/xserver
:> $RPM_BUILD_ROOT/etc/security/blacklist.xserver

rm -f $RPM_BUILD_ROOT%{_libdir}/xorg/modules/{*,*/*}.{la,a}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc COPYING
%attr(755,root,root) %{_bindir}/X
%attr(755,root,root) %{_bindir}/Xorg
%attr(4755,root,root) %{_bindir}/Xwrapper
%attr(755,root,root) %{_bindir}/cvt
%attr(755,root,root) %{_bindir}/gtf
%attr(755,root,root) %{_bindir}/in[bwl]
%attr(755,root,root) %{_bindir}/ioport
%attr(755,root,root) %{_bindir}/out[bwl]
%attr(755,root,root) %{_bindir}/pcitweak
%attr(755,root,root) %{_bindir}/scanpci
%attr(755,root,root) %{_bindir}/xorgcfg
%attr(755,root,root) %{_bindir}/xorgconfig
%{_includedir}/X11/bitmaps/*
%{_includedir}/X11/pixmaps
%{_libdir}/X11/Cards
%{_libdir}/X11/Options
%dir %{_libdir}/xorg
%dir %{_libdir}/xorg/modules
%dir %{_libdir}/xorg/modules/dri
%dir %{_libdir}/xorg/modules/drivers
%dir %{_libdir}/xorg/modules/extensions
%attr(755,root,root) %{_libdir}/xorg/modules/extensions/libGLcore.so
%attr(755,root,root) %{_libdir}/xorg/modules/extensions/libdbe.so
%attr(755,root,root) %{_libdir}/xorg/modules/extensions/libdri.so
%attr(755,root,root) %{_libdir}/xorg/modules/extensions/libextmod.so
%attr(755,root,root) %{_libdir}/xorg/modules/extensions/librecord.so
%attr(755,root,root) %{_libdir}/xorg/modules/extensions/libxtrap.so
%dir %{_libdir}/xorg/modules/fonts
%attr(755,root,root) %{_libdir}/xorg/modules/fonts/lib*.so
%dir %{_libdir}/xorg/modules/input
%dir %{_libdir}/xorg/modules/linux
%attr(755,root,root) %{_libdir}/xorg/modules/linux/libfbdevhw.so
%dir %{_libdir}/xorg/modules/multimedia
%attr(755,root,root) %{_libdir}/xorg/modules/multimedia/*.so
%attr(755,root,root) %{_libdir}/xorg/modules/lib*.so
%dir %{_libdir}/xserver
%{_libdir}/xserver/SecurityPolicy
%{_datadir}/X11/app-defaults/XOrgCfg
%dir /var/lib/xkb
/var/lib/xkb/README.compiled
%attr(640,root,root) %config(noreplace) %verify(not md5 mtime size) /etc/pam.d/xserver
%attr(640,root,root) %config(noreplace) %verify(not md5 mtime size) /etc/security/blacklist.xserver
%config(missingok) /etc/security/console.apps/xserver
%{_mandir}/man1/Xorg.1x*
%{_mandir}/man1/Xserver.1x*
%{_mandir}/man1/cvt.1*
%{_mandir}/man1/gtf.1x*
%{_mandir}/man1/pcitweak.1x*
%{_mandir}/man1/scanpci.1x*
%{_mandir}/man1/xorgcfg.1x*
%{_mandir}/man1/xorgconfig.1*
%{_mandir}/man4/exa.4*
%{_mandir}/man4/fbdevhw.4*
%{_mandir}/man5/xorg.conf.5x*

%files -n xorg-xserver-Xdmx
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/Xdmx
%attr(755,root,root) %{_bindir}/dmxaddinput
%attr(755,root,root) %{_bindir}/dmxaddscreen
%attr(755,root,root) %{_bindir}/dmxreconfig
%attr(755,root,root) %{_bindir}/dmxresize
%attr(755,root,root) %{_bindir}/dmxrminput
%attr(755,root,root) %{_bindir}/dmxrmscreen
%attr(755,root,root) %{_bindir}/dmxtodmx
%attr(755,root,root) %{_bindir}/dmxwininfo
%attr(755,root,root) %{_bindir}/vdltodmx
%attr(755,root,root) %{_bindir}/xdmx
%attr(755,root,root) %{_bindir}/xdmxconfig
%{_mandir}/man1/Xdmx.1x*
%{_mandir}/man1/dmxtodmx.1x*
%{_mandir}/man1/vdltodmx.1x*
%{_mandir}/man1/xdmxconfig.1x*

%files -n xorg-xserver-Xnest
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/Xnest
%{_mandir}/man1/Xnest.1x*

%files -n xorg-xserver-Xprt
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/Xprt
%{_libdir}/X11/xserver
%{_mandir}/man1/Xprt.1x*

%files -n xorg-xserver-Xvfb
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/Xvfb
%{_mandir}/man1/Xvfb.1x*

%files devel
%defattr(644,root,root,755)
%{_includedir}/xorg
%{_libdir}/libxf86config.a
%{_aclocaldir}/xorg-server.m4
%{_pkgconfigdir}/xorg-server.pc

%files -n xorg-xserver-libglx
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/xorg/modules/extensions/libglx.so
