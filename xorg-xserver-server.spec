# TODO
# - consider XSELINUX by default
# - Xvfb initscript runs Xvfb as root! add user there!
#
# Conditional build:
%bcond_with	dbus		# D-BUS support for configuration (if no udev)
%bcond_with	hal		# HAL support for configuration (if no udev)
%bcond_without	udev		# UDEV support for configuration
%bcond_without	dri2		# DRI2 extension
%bcond_without	dri3		# DRI3 extension
%bcond_without	record		# RECORD extension
%bcond_with	xcsecurity	# XC-SECURITY extension (deprecated)
%bcond_with	xf86bigfont	# XF86BigFont extension
%bcond_with	xselinux	# SELinux extension
%bcond_without	xnest		# Xnest DDX (Xnest server)
%bcond_without	xvfb		# Xvfb DDX (Xvfb server)
%bcond_without	xephyr		# kdrive Xephyr server
%bcond_without	glamor		# glamor dix module
%bcond_without	systemtap	# systemtap/dtrace probes
%bcond_without	libunwind	# use libunwind for backtracing
%bcond_without	systemd		# systemd
#
# ABI versions, see hw/xfree86/common/xf86Module.h
%define	xorg_xserver_server_ansic_abi		0.4
%define	xorg_xserver_server_extension_abi	10.0
%define	xorg_xserver_server_videodrv_abi	25.2
%define	xorg_xserver_server_xinput_abi		24.4

%define	pixman_ver	0.30.0

%ifarch x32
%undefine	with_libunwind
%endif

Summary:	X.org server
Summary(pl.UTF-8):	Serwer X.org
Name:		xorg-xserver-server
Version:	21.1.20
Release:	1
License:	MIT
Group:		X11/Servers
Source0:	https://xorg.freedesktop.org/releases/individual/xserver/xorg-server-%{version}.tar.xz
# Source0-md5:	3778c462b6f199c29d64705d337e9dc7
Source1:	10-quirks.conf
Source2:	xserver.pamd
Source10:	%{name}-Xvfb.init
Source11:	%{name}-Xvfb.sysconfig
Source12:	xvfb-run.sh
Patch0:		python3.patch
Patch1:		%{name}-xwrapper-pam.patch
Patch4:		%{name}-builtin-SHA1.patch
Patch6:		110_nvidia_slowdow_fix.patch
URL:		https://xorg.freedesktop.org/
BuildRequires:	Mesa-dri-devel >= 7.8.1
%{?with_dri2:BuildRequires:	Mesa-dri-devel >= 9.2.0}
%{?with_glamor:BuildRequires:	Mesa-libgbm-devel >= 17.1.0}
BuildRequires:	OpenGL-devel >= 3.0
# for glx headers
BuildRequires:	OpenGL-GLX-devel >= 1.3
%{?with_xselinux:BuildRequires:	audit-libs-devel}
BuildRequires:	autoconf >= 2.60
BuildRequires:	automake
BuildRequires:	cpp
BuildRequires:	docbook-dtd43-xml
#BuildRequires:	doxygen >= 1.6.1
%if %{with hal} || %{with dbus}
BuildRequires:	dbus-devel >= 1.0
%endif
%{?with_hal:BuildRequires:	hal-devel}
BuildRequires:	libbsd-devel
BuildRequires:	libdrm-devel >= 2.4.89
%if %{with glamor}
BuildRequires:	libepoxy-devel >= 1.5.4
%endif
%{?with_xselinux:BuildRequires:	libselinux-devel >= 2.0.86}
BuildRequires:	libtirpc-devel
BuildRequires:	libtool >= 2:2.2
%{?with_libunwind:BuildRequires:	libunwind-devel}
BuildRequires:	libxcb-devel >= 1.9.3
BuildRequires:	pam-devel
BuildRequires:	perl-base
BuildRequires:	pixman-devel >= %{pixman_ver}
BuildRequires:	pkgconfig >= 1:0.19
BuildRequires:	pkgconfig(gl) >= 1.2
%{?with_systemtap:BuildRequires:	systemtap-sdt-devel}
%{?with_systemd:BuildRequires:	systemd-devel >= 1:209}
BuildRequires:	tar >= 1:1.22
BuildRequires:	udev-devel >= 1:143
BuildRequires:	xcb-util-devel
BuildRequires:	xcb-util-image-devel
BuildRequires:	xcb-util-keysyms-devel
BuildRequires:	xcb-util-renderutil-devel
BuildRequires:	xcb-util-wm-devel
BuildRequires:	xmlto >= 0.0.20
BuildRequires:	xorg-app-mkfontscale
BuildRequires:	xorg-app-xkbcomp
BuildRequires:	xorg-font-font-util >= 1.1
BuildRequires:	xorg-lib-libX11-devel >= 1.6
BuildRequires:	xorg-lib-libXau-devel
BuildRequires:	xorg-lib-libXdamage-devel
BuildRequires:	xorg-lib-libXdmcp-devel
BuildRequires:	xorg-lib-libXext-devel >= 1.0.99.4
BuildRequires:	xorg-lib-libXfixes-devel
BuildRequires:	xorg-lib-libXfont2-devel >= 2.0.0
BuildRequires:	xorg-lib-libXi-devel >= 1.2.99.1
BuildRequires:	xorg-lib-libXrender-devel
BuildRequires:	xorg-lib-libXres-devel
BuildRequires:	xorg-lib-libXtst-devel >= 1.0.99.2
BuildRequires:	xorg-lib-libXv-devel
BuildRequires:	xorg-lib-libXxf86dga-devel
BuildRequires:	xorg-lib-libXxf86vm-devel
BuildRequires:	xorg-lib-libfontenc-devel
BuildRequires:	xorg-lib-libpciaccess-devel >= 0.12.901
BuildRequires:	xorg-lib-libxcvt-devel
BuildRequires:	xorg-lib-libxkbfile-devel
BuildRequires:	xorg-lib-libxshmfence-devel >= 1.1
BuildRequires:	xorg-lib-xtrans-devel >= 1.3.5
BuildRequires:	xorg-proto-bigreqsproto-devel >= 1.1.0
BuildRequires:	xorg-proto-compositeproto-devel >= 0.4
BuildRequires:	xorg-proto-damageproto-devel >= 1.1
%{?with_dri2:BuildRequires:	xorg-proto-dri2proto-devel >= 2.8}
BuildRequires:	xorg-proto-dri3proto-devel >= 1.2
BuildRequires:	xorg-proto-fixesproto-devel >= 6.0
BuildRequires:	xorg-proto-fontcacheproto-devel
BuildRequires:	xorg-proto-fontsproto-devel >= 2.1.3
BuildRequires:	xorg-proto-glproto-devel >= 1.4.17
BuildRequires:	xorg-proto-inputproto-devel >= 2.3.99.1
BuildRequires:	xorg-proto-kbproto-devel >= 1.0.3
BuildRequires:	xorg-proto-presentproto-devel >= 1.2
BuildRequires:	xorg-proto-printproto-devel
BuildRequires:	xorg-proto-randrproto-devel >= 1.6.0
%{?with_record:BuildRequires:	xorg-proto-recordproto-devel >= 1.13.99.1}
BuildRequires:	xorg-proto-renderproto-devel >= 0.11
BuildRequires:	xorg-proto-resourceproto-devel >= 1.2.0
BuildRequires:	xorg-proto-scrnsaverproto-devel >= 1.1
BuildRequires:	xorg-proto-videoproto-devel
BuildRequires:	xorg-proto-xcmiscproto-devel >= 1.2.0
BuildRequires:	xorg-proto-xextproto-devel >= 1:7.3.0
%{?with_xf86bigfont:BuildRequires:	xorg-proto-xf86bigfontproto-devel >= 1.2.0}
BuildRequires:	xorg-proto-xf86dgaproto-devel >= 2.0.99.1
BuildRequires:	xorg-proto-xf86driproto-devel >= 2.1.0
BuildRequires:	xorg-proto-xf86miscproto-devel
BuildRequires:	xorg-proto-xf86vidmodeproto-devel >= 2.2.99.1
BuildRequires:	xorg-proto-xineramaproto-devel
BuildRequires:	xorg-proto-xproto-devel >= 7.0.31
BuildRequires:	xorg-sgml-doctools >= 1.8
BuildRequires:	xorg-util-util-macros >= 1.14
BuildRequires:	xz
%{?with_glamor:Requires:	Mesa-libgbm >= 17.1.0}
Requires:	libdrm >= 2.4.89
%{?with_glamor:Requires:	libepoxy >= 1.5.4}
Requires:	pixman >= %{pixman_ver}
Requires:	sed >= 4.0
Requires:	udev-libs >= 1:143
Requires:	xkeyboard-config
# for rgb.txt
Requires:	xorg-app-rgb >= 0.99.3
Requires:	xorg-app-xkbcomp
Requires:	xorg-lib-libXfont2 >= 2.0.0
Requires:	xorg-lib-libpciaccess >= 0.12.901
Requires:	xorg-lib-libxshmfence >= 1.1
# for protocol.txt
Requires:	xorg-xserver-common = %{version}-%{release}
Suggests:	%{name}-tools = %{version}-%{release}
Suggests:	dbus-x11 >= 1.0
%{?with_hal:Suggests:	hal}
Suggests:	udev-acl >= 1:143
%{?with_udev:Suggests:	udev-core >= 1:143}
Suggests:	xkeyboard-config
Suggests:	xorg-driver-input-libinput
# Usual desktop setups need least one video driver to run, see xorg.log which one exactly
Suggests:	xorg-driver-video
Provides:	xorg-driver-video-modesetting
Provides:	xorg-xserver-libdri = %{version}-%{release}
Provides:	xorg-xserver-module(dri)
Provides:	xorg-xserver-server(ansic-abi) = %{xorg_xserver_server_ansic_abi}
Provides:	xorg-xserver-server(extension-abi) = %{xorg_xserver_server_extension_abi}
Provides:	xorg-xserver-server(videodrv-abi) = %{xorg_xserver_server_videodrv_abi}
Provides:	xorg-xserver-server(xinput-abi) = %{xorg_xserver_server_xinput_abi}
Obsoletes:	X11-Xserver < 1:7.0.0
Obsoletes:	X11-driver-i2c < 1:7.0.0
Obsoletes:	X11-modules < 1:7.0.0
Obsoletes:	X11-setup < 1:7.0.0
Obsoletes:	XFree86-Xserver < 1:7.0.0
Obsoletes:	XFree86-modules < 1:7.0.0
Obsoletes:	XFree86-setup < 1:7.0.0
Obsoletes:	Xserver < 7.0
%{?with_glamor:Obsoletes:	glamor < 0.6.1}
Obsoletes:	xorg-xserver-libdri < 1.12.99
Obsoletes:	xorg-xserver-server-xorgcfg < 1.5.99
Obsoletes:	xorg-driver-video-modesetting < 0.9.1
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		tirpc_cflags	$(pkg-config --cflags libtirpc)
%define		tirpc_libs	$(pkg-config --libs libtirpc)

# dtrace script expects CPP to be cpp, not "gcc -E", so force it regardless of rpm version
# (autotools-based rpm<4.19 used to have "gcc -E", cmake builds for 4.19+ switched to cpp)
%define		__cpp	cpp

%description
Xorg server is a generally used X server which uses display hardware.
It requires proper driver for your display hardware.

%description -l pl.UTF-8
Serwer Xorg to podstawowy serwer X wyświetlający obraz na karcie
graficznej. Do działania wymaga odpowiedniego sterownika.

%package tools
Summary:	Tools to calculate modelines for X.org server
Summary(pl.UTF-8):	Narzędzia do liczenia opisów trybów graficznych (modeline) dla serwera X.org
Group:		X11/Applications
# for cvt
Requires:	xorg-lib-libxcvt-tools
Conflicts:	xorg-xserver-server < 1.20.11-4

%description tools
Tools to calculate modelines for X.org server (using Coordinated Video
Timing or Generalized Timing Formula).

%description tools -l pl.UTF-8
Narzędzia do liczenia opisów trybów graficznych (modeline) dla serwera
X.org (przy użyciu algorytmów Coordinated Video Timing lub
Generalizaed Timing Formula).

%package devel
Summary:	Header files for X.org server
Summary(pl.UTF-8):	Pliki nagłówkowe dla serwera X.org
Group:		X11/Development/Libraries
Requires:	Mesa-dri-devel >= 7.8.0
Requires:	libdrm-devel >= 2.4.89
Requires:	pixman-devel >= %{pixman_ver}
Requires:	xorg-lib-libXfont2-devel >= 2.0.0
Requires:	xorg-lib-libpciaccess-devel >= 0.12.901
Requires:	xorg-lib-libxkbfile-devel
%{?with_dri2:Requires:	xorg-proto-dri2proto-devel >= 2.8}
%{?with_dri3:Requires:	xorg-proto-dri3proto-devel >= 1.0}
Requires:	xorg-proto-dri3proto-devel >= 1.0
Requires:	xorg-proto-fontsproto-devel >= 2.1.3
Requires:	xorg-proto-glproto-devel >= 1.4.17
Requires:	xorg-proto-inputproto-devel >= 2.3.99.1
Requires:	xorg-proto-kbproto-devel >= 1.0.3
Requires:	xorg-proto-presentproto-devel >= 1.2
Requires:	xorg-proto-randrproto-devel >= 1.6.0
Requires:	xorg-proto-renderproto-devel >= 0.11
Requires:	xorg-proto-resourceproto-devel >= 1.2.0
Requires:	xorg-proto-scrnsaverproto-devel >= 1.1
Requires:	xorg-proto-videoproto-devel
Requires:	xorg-proto-xextproto-devel >= 1:7.3.0
Requires:	xorg-proto-xf86driproto-devel >= 2.1.0
Requires:	xorg-proto-xineramaproto-devel
Requires:	xorg-proto-xproto-devel >= 7.0.31
Obsoletes:	X11-Xserver-devel < 1:7.0.0
Obsoletes:	XFree86-Xserver-devel < 1:7.0.0
%{?with_glamor:Obsoletes:	glamor-devel < 0.6.1}

%description devel
Header files for X.org server.

%description devel -l pl.UTF-8
Pliki nagłówkowe dla serwera X.org.

%package source
Summary:	X.org server source code
Summary(pl.UTF-8):	Pliki źródłowe dla serwera X.org
Group:		X11/Development/Libraries

%description source
X.org server source code.

%description source -l pl.UTF-8
Pliki źródłowe dla serwera X.org.

%package -n xorg-xserver-libglx
Summary:	GLX extension library for X.org server
Summary(pl.UTF-8):	Biblioteka rozszerzenia GLX dla serwera X.org
Group:		X11/Servers
Requires:	%{name} = %{version}-%{release}
Requires:	OpenGL >= 1.2
# Mesa version glapi tables in glx/ dir come from
Provides:	xorg-xserver-libglx(glapi) = 7.1.0
Provides:	xorg-xserver-module(glx)
Obsoletes:	X11-OpenGL-core < 1:7.0.0
Obsoletes:	XFree86-OpenGL-core < 1:7.0.0

%description -n xorg-xserver-libglx
GLX extension library for X.org server.

%description -n xorg-xserver-libglx -l pl.UTF-8
Biblioteka rozszerzenia GLX dla serwera X.org.

%package -n xorg-xserver-Xephyr
Summary:	Xephyr - nested X server
Summary(pl.UTF-8):	Xephyr - zagnieżdżony serwer X
Group:		X11/Servers
Requires:	OpenGL >= 3.0
%{?with_glamor:Requires:	libepoxy >= 1.5.4}
Requires:	libxcb >= 1.9.3
Requires:	pixman >= %{pixman_ver}
Requires:	xorg-lib-libXfont2 >= 2.0.0

%description -n xorg-xserver-Xephyr
Xephyr is a kdrive server that outputs to a window on a pre-existing
'host' X display. Think Xnest but with support for modern extensions
like composite, damage and randr.

Unlike Xnest which is an X proxy, i.e. limited to the capabilities of
the host X server, Xephyr is a real X server which uses the host X
server window as "framebuffer" via fast SHM XImages.

It also has support for 'visually' debugging what the server is
painting.

%description -n xorg-xserver-Xephyr -l pl.UTF-8
Xephyr jest serwerem opartym na kdrive wyświetlającym w oknie na
istniejącym ekranie X. Można o nim myśleć jako o Xnest ze wsparciem do
wspólczesnych rozszerzeń jak composite, damage i randr.

%package -n xorg-xserver-Xnest
Summary:	Xnest - nested X server
Summary(pl.UTF-8):	Xnest - zagnieżdżony serwer X
Group:		X11/Servers
Requires:	pixman >= %{pixman_ver}
Requires:	xorg-lib-libXext >= 1.0.99.4
Requires:	xorg-lib-libXfont2 >= 2.0.0
Obsoletes:	X11-Xnest < 1:7.0.0
Obsoletes:	XFree86-Xnest < 1:7.0.0
Obsoletes:	Xserver-Xnest < 7.0

%description -n xorg-xserver-Xnest
Xnest is an X Window System server which runs in an X window. Xnest is
a 'nested' window server, actually a client of the real X server,
which manages windows and graphics requests for Xnest, while Xnest
manages the windows and graphics requests for its own clients.

%description -n xorg-xserver-Xnest -l pl.UTF-8
Xnest jest serwerem X uruchamianym w okienku innego serwera X. Xnest
zachowuje się jak klient X w stosunku do prawdziwego serwera X, a jak
serwer X dla własnych klientów.

%description -n xorg-xserver-Xnest -l ru.UTF-8
Xnest - это сервер X Window System, который работает в окне X. На
самом деле это клиент реального X-сервера, который управляет окнами и
графическими запросами для Xnest в то время, как Xnest управляет
окнами и графическими запросами для своих собственных клиентов.

%description -n xorg-xserver-Xnest -l uk.UTF-8
Xnest - це сервер X Window System, який працює у вікні X. Фактично це
клієнт реального X-сервера, який керує вікнами та графічними запитами
для Xnest в той час, як Xnest керує вікнами та графічними запитами для
своїх власних клієнтів.

%package -n xorg-xserver-Xvfb
Summary:	Xvfb - virtual framebuffer X server
Summary(pl.UTF-8):	Xvfb - serwer X z wirtualnym framebufferem
Group:		X11/Servers
Requires:	OpenGL >= 1.2.1
Requires:	mktemp
Requires:	pixman >= %{pixman_ver}
Requires:	util-linux
Requires:	which
Requires:	xkeyboard-config
Requires:	xorg-app-xauth
Requires:	xorg-app-xkbcomp
Requires:	xorg-lib-libXfont2 >= 2.0.0
Obsoletes:	X11-Xvfb < 1:7.0.0
Obsoletes:	XFree86-Xvfb < 1:7.0.0

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

%description -n xorg-xserver-Xvfb -l pl.UTF-8
Xvfb (X Virtual Frame Buffer) jest serwerem X, który można uruchamiać
na maszynach bez urządzeń wyświetlających ani fizycznych urządzeń
wejściowych. Xvfb emuluje prosty framebuffer w pamięci. Zwykle jest
używany do testowania serwerów X, może też być używany do testowania
klientów X w rzadko używanych konfiguracjach ekranu. Można też użyć
Xvfb do uruchomienia aplikacji, które w rzeczywistości nie wymagają
serwera X, ale odmawiają uruchomienia bez niego.

%package -n xorg-xserver-Xvfb-init
Summary:	Init scripts for Xvfb
Summary(pl.UTF-8):	Skrypty startowe dla Xvfb
Group:		X11/Servers
Requires:	xorg-xserver-Xvfb = %{version}-%{release}

%description -n xorg-xserver-Xvfb-init
This package contains init scripts for Xvfb and registers Xvfb as
system service.

%description -n xorg-xserver-Xvfb-init -l pl.UTF-8
Ten pakiet zawiera skrypty startowe dla Xvfb oraz rejestruje Xvfb jako
usługę systemową.

%package -n xorg-xserver-common
Summary:	Common files for various X servers
Summary(pl.UTF-8):	Pliki wspólne dla serwerów X
Group:		X11/Servers
Conflicts:	xorg-xserver-server < 1.20.11-2

%description -n xorg-xserver-common
Common files for various X servers.

%description -n xorg-xserver-common -l pl.UTF-8
Pliki wspólne dla serwerów X.

%prep
%setup -q -n xorg-server-%{version}
%patch -P0 -p1
%patch -P1 -p1
%patch -P4 -p1
%patch -P6 -p1

# xserver uses pixman-1 API/ABI so put that explictly here
sed -i -e 's#<pixman\.h#<pixman-1/pixman.h#g' ./fb/fb.h ./include/miscstruct.h ./render/picture.h

# support __filemansuffix__ with "x" suffix (per FHS 2.3)
%{__sed} -i -e 's,\.so man__filemansuffix__/,.so man5/,' hw/xfree86/man/*.man

%{__sed} -i -e '1s|#!/usr/bin/python$|#!%{__python3}|' config/fdi2iclass.py

%build
API=$(awk '/#define ABI_ANSIC_VERSION/ { split($0,A,/[(,)]/); printf("%d.%d",A[2], A[3]); }' hw/xfree86/common/xf86Module.h)
if [ "$API" != "%{xorg_xserver_server_ansic_abi}" ]; then
	echo "Set %%define xorg_xserver_server_ansic_abi to $API and rerun."
	exit 1
fi

API=$(awk '/#define ABI_EXTENSION_VERSION/ { split($0,A,/[(,)]/); printf("%d.%d",A[2], A[3]); }' hw/xfree86/common/xf86Module.h)
if [ "$API" != "%{xorg_xserver_server_extension_abi}" ]; then
	echo "Set %%define xorg_xserver_server_extension_abi to $API and rerun."
	exit 1
fi

API=$(awk '/#define ABI_VIDEODRV_VERSION/ { split($0,A,/[(,)]/); printf("%d.%d",A[2], A[3]); }' hw/xfree86/common/xf86Module.h)
if [ "$API" != "%{xorg_xserver_server_videodrv_abi}" ]; then
	echo "Set %%define xorg_xserver_server_videodrv_abi to $API and rerun."
	exit 1
fi
API=$(awk '/#define ABI_XINPUT_VERSION/ { split($0,A,/[(,)]/); printf("%d.%d",A[2], A[3]); }' hw/xfree86/common/xf86Module.h)
if [ "$API" != "%{xorg_xserver_server_xinput_abi}" ]; then
	echo "Set %%define xorg_xserver_server_xinput_abi to $API and rerun."
	exit 1
fi

%{__libtoolize}
%{__aclocal} -I m4
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	CPPFLAGS="%{rpmcppflags} %{tirpc_cflags}" \
	LIBS="%{tirpc_libs}" \
	--libexecdir=%{_libdir}/xorg \
	--with-default-font-path="%{_fontsdir}/misc,%{_fontsdir}/TTF,%{_fontsdir}/OTF,%{_fontsdir}/Type1,%{_fontsdir}/100dpi,%{_fontsdir}/75dpi" \
	--with-xkb-output=/var/lib/xkb \
	--disable-linux-acpi \
	--disable-linux-apm \
	%{?with_dbus:--enable-config-dbus} \
	--enable-config-hal%{!?with_hal:=no} \
	--enable-config-udev%{!?with_udev:=no} \
	--enable-dga \
	--enable-dri2%{!?with_dri2:=no} \
	--enable-dri3%{!?with_dri3:=no} \
	%{?with_glamor:--enable-glamor} \
	--enable-kdrive \
	%{?with_libunwind:--enable-libunwind} \
	%{?with_record:--enable-record} \
	--enable-secure-rpc \
	--enable-suid-wrapper \
	%{?with_xcsecurity:--enable-xcsecurity} \
	--enable-xephyr%{!?with_xephyr:=no} \
	%{?with_xf86bigfont:--enable-xf86bigfont} \
	--enable-xnest%{!?with_xnest:=no} \
	%{?with_xselinux:--enable-xselinux} \
	%{!?with_xvfb:--disable-xvfb} \
	%{!?with_systemtap:--without-dtrace} \
	--without-fop \
	%{__with_without systemd systemd-daemon}

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%if "%{_libdir}" != "%{_exec_prefix}/lib"
install -d $RPM_BUILD_ROOT%{_exec_prefix}/lib/xorg/modules/dri
%endif

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install -Dp %{SOURCE2} $RPM_BUILD_ROOT/etc/pam.d/xserver
install -d $RPM_BUILD_ROOT/etc/{security/console.apps,X11/xorg.conf.d}
install -d $RPM_BUILD_ROOT%{_libdir}/xorg/modules/{dri,drivers,input}
install -d $RPM_BUILD_ROOT%{_datadir}/X11/xorg.conf.d
install -p %{SOURCE12} $RPM_BUILD_ROOT%{_bindir}/xvfb-run

:> $RPM_BUILD_ROOT/etc/security/console.apps/xserver
:> $RPM_BUILD_ROOT/etc/security/blacklist.xserver

%{__rm} $RPM_BUILD_ROOT%{_libdir}/xorg/modules/{*,*/*}.la

cp -p %{SOURCE1} $RPM_BUILD_ROOT%{_datadir}/X11/xorg.conf.d/10-quirks.conf

%if %{with xvfb}
install -d $RPM_BUILD_ROOT/etc/rc.d/init.d
install -d $RPM_BUILD_ROOT/etc/sysconfig
install -p %{SOURCE10} $RPM_BUILD_ROOT/etc/rc.d/init.d/Xvfb
cp -p %{SOURCE11} $RPM_BUILD_ROOT/etc/sysconfig/Xvfb
%endif

# Xorg.wrap config
cat >$RPM_BUILD_ROOT/etc/X11/Xwrapper.config <<EOF
# allowed values: rootonly console anybody pam
allowed_users = pam

# set to yes if hardware or console access requires root rights (and Xwrapper fails to detect it)
#needs_root_rights = yes
EOF

# compatibility with old xwrapper
ln -s %{_libdir}/xorg/Xorg.wrap $RPM_BUILD_ROOT%{_bindir}/Xwrapper

# prepare source package
install -d $RPM_BUILD_ROOT%{_usrsrc}/%{name}-%{version}
cp -a * $RPM_BUILD_ROOT%{_usrsrc}/%{name}-%{version}
cd $RPM_BUILD_ROOT%{_usrsrc}/%{name}-%{version}
%{__make} distclean
find '(' -name '*~' -o -name '*.orig' ')' -print0 | xargs -0 -r -l512 rm -f
find -name '*.h' | xargs chmod a-x

%if %{with systemtap}
%{__rm} $RPM_BUILD_ROOT%{_docdir}/xorg-server/Xserver-DTrace.*
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%triggerpostun -- xorg-xserver-server < 1.5.0
if [ -f /etc/X11/xorg.conf ]; then
	sed -i -e 's/^\s*RgbPath.*$/#& # obsolete option/' /etc/X11/xorg.conf
	sed -i -e 's/^\s*Load\s*"type1".*$/#& # obsolete module/' /etc/X11/xorg.conf
%if %{without record}
	sed -i -e 's/^\s*Load\s*"record".*$/#& # module disabled in this build/' /etc/X11/xorg.conf
%endif
	sed -i -e 's/^\s*Load\s*"xtrap".*$/#& # obsolete module/' /etc/X11/xorg.conf
fi

%post -n xorg-xserver-Xvfb-init
/sbin/chkconfig --add Xvfb
%service Xvfb restart

%preun -n xorg-xserver-Xvfb-init
if [ "$1" = "0" ]; then
	%service -q Xvfb stop
	/sbin/chkconfig --del Xvfb
fi

%files
%defattr(644,root,root,755)
%doc COPYING ChangeLog README.md
%attr(755,root,root) %{_bindir}/X
%attr(755,root,root) %{_bindir}/Xorg
%attr(4755,root,root) %{_bindir}/Xwrapper
%attr(755,root,root) %{_libdir}/xorg/Xorg
%attr(4755,root,root) %{_libdir}/xorg/Xorg.wrap
%dir %{_libdir}/xorg/modules
%attr(755,root,root) %{_libdir}/xorg/modules/libexa.so
%attr(755,root,root) %{_libdir}/xorg/modules/libfbdevhw.so
%{?with_glamor:%attr(755,root,root) %{_libdir}/xorg/modules/libglamoregl.so}
%attr(755,root,root) %{_libdir}/xorg/modules/libint10.so
%attr(755,root,root) %{_libdir}/xorg/modules/libshadow.so
%attr(755,root,root) %{_libdir}/xorg/modules/libshadowfb.so
%attr(755,root,root) %{_libdir}/xorg/modules/libvgahw.so
%attr(755,root,root) %{_libdir}/xorg/modules/libwfb.so
%dir %{_libdir}/xorg/modules/dri
%dir %{_libdir}/xorg/modules/drivers
%attr(755,root,root) %{_libdir}/xorg/modules/drivers/modesetting_drv.so
%dir %{_libdir}/xorg/modules/extensions
%dir %{_libdir}/xorg/modules/input
%attr(755,root,root) %{_libdir}/xorg/modules/input/inputtest_drv.so
%if "%{_libdir}" != "%{_exec_prefix}/lib"
%dir %{_exec_prefix}/lib/xorg
%dir %{_exec_prefix}/lib/xorg/modules
%dir %{_exec_prefix}/lib/xorg/modules/dri
%endif
%dir /var/lib/xkb
/var/lib/xkb/README.compiled
%attr(640,root,root) %config(noreplace) %verify(not md5 mtime size) /etc/pam.d/xserver
%attr(640,root,root) %config(noreplace) %verify(not md5 mtime size) /etc/security/blacklist.xserver
%config(missingok) /etc/security/console.apps/xserver
%{?with_dbus:/etc/dbus-1/system.d/xorg-server.conf}
%dir /etc/X11/xorg.conf.d
%config(noreplace) %verify(not md5 mtime size) /etc/X11/Xwrapper.config
%dir %{_datadir}/X11/xorg.conf.d
# overwrite these settings with local configs in /etc/X11/xorg.conf.d
%verify(not md5 mtime size) %{_datadir}/X11/xorg.conf.d/10-quirks.conf
%{_mandir}/man1/Xorg.1*
%{_mandir}/man1/Xorg.wrap.1*
%{_mandir}/man4/exa.4*
%{_mandir}/man4/fbdevhw.4*
%{_mandir}/man4/inputtestdrv.4*
%{_mandir}/man4/modesetting.4*
%{_mandir}/man5/Xwrapper.config.5*
%{_mandir}/man5/xorg.conf.5*
%{_mandir}/man5/xorg.conf.d.5*

%files tools
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/gtf
%{_mandir}/man1/gtf.1*

%files devel
%defattr(644,root,root,755)
%doc doc/{Xinput,Xserver-spec}.html %{?with_systemtap:doc/dtrace/Xserver-DTrace.html}
%{_includedir}/xorg
%{_aclocaldir}/xorg-server.m4
%{_pkgconfigdir}/xorg-server.pc

%files source
%defattr(644,root,root,755)
# keep file perms from install time, but have default defattr to keep adapter happy
%defattr(-,root,root,755)
%{_usrsrc}/%{name}-%{version}

%files -n xorg-xserver-libglx
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/xorg/modules/extensions/libglx.so

%if %{with xephyr}
%files -n xorg-xserver-Xephyr
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/Xephyr
%{_mandir}/man1/Xephyr.1*
%endif

%if %{with xnest}
%files -n xorg-xserver-Xnest
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/Xnest
%{_mandir}/man1/Xnest.1*
%endif

%if %{with xvfb}
%files -n xorg-xserver-Xvfb
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/Xvfb
%attr(755,root,root) %{_bindir}/xvfb-run
%{_mandir}/man1/Xvfb.1*

%files -n xorg-xserver-Xvfb-init
%defattr(644,root,root,755)
%attr(754,root,root) /etc/rc.d/init.d/Xvfb
%config(noreplace) %verify(not md5 mtime size) /etc/sysconfig/Xvfb
%endif

%files -n xorg-xserver-common
%defattr(644,root,root,755)
%dir %{_libdir}/xorg
%{_libdir}/xorg/protocol.txt
%{_mandir}/man1/Xserver.1*
