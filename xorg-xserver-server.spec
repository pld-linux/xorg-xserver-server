# TODO: consider XSELINUX
#
# Conditional build:
%bcond_with	dbus		# D-BUS support for configuration (if no udev)
%bcond_with	hal		# HAL support for configuration (if no udev)
%bcond_without	udev		# UDEV support for configuration
%bcond_without	dri2		# DRI2 extension
%bcond_without	dmx		# DMX support
%bcond_without	record		# RECORD extension
%bcond_with	xcsecurity	# XC-SECURITY extension (deprecated)
%bcond_with	xf86bigfont	# XF86BigFont extension
%bcond_with	xselinux	# SELinux extension
#
# ABI versions, see hw/xfree86/common/xf86Module.h
%define	xorg_xserver_server_ansic_abi		0.4
%define	xorg_xserver_server_extension_abi	7.0
%define	xorg_xserver_server_font_abi		0.6
%define	xorg_xserver_server_videodrv_abi	14.1
%define	xorg_xserver_server_xinput_abi		19.1
#
%define	pixman_ver	0.28.0

Summary:	X.org server
Summary(pl.UTF-8):	Serwer X.org
Name:		xorg-xserver-server
Version:	1.14.1
Release:	1
License:	MIT
Group:		X11/Servers
Source0:	http://xorg.freedesktop.org/releases/individual/xserver/xorg-server-%{version}.tar.bz2
# Source0-md5:	6a0f1a1639ada4b9da7e9582bc79252a
Source1:	10-quirks.conf
Source2:	xserver.pamd
Source10:	%{name}-Xvfb.init
Source11:	%{name}-Xvfb.sysconfig
Patch0:		%{name}-xwrapper.patch
Patch1:		%{name}-pic-libxf86config.patch

Patch3:		%{name}-less-acpi-brokenness.patch
Patch4:		%{name}-builtin-SHA1.patch
Patch5:		%{name}-export-GetMaster.patch
Patch6:		110_nvidia_slowdow_fix.patch
Patch7:		%{name}-include-defs.patch
URL:		http://xorg.freedesktop.org/
BuildRequires:	Mesa-libGL-devel >= 7.8.1
# for glx headers
BuildRequires:	OpenGL-GLX-devel
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
BuildRequires:	libdrm-devel >= 2.4.39
%{?with_xselinux:BuildRequires:	libselinux-devel >= 2.0.86}
BuildRequires:	libtool
BuildRequires:	ncurses-devel
BuildRequires:	pam-devel
BuildRequires:	perl-base
BuildRequires:	pixman-devel >= %{pixman_ver}
BuildRequires:	pkgconfig >= 1:0.19
BuildRequires:	udev-devel >= 1:143
BuildRequires:	xmlto >= 0.0.20
BuildRequires:	xorg-app-mkfontscale
BuildRequires:	xorg-font-font-util >= 1.1
BuildRequires:	xorg-lib-libX11-devel
BuildRequires:	xorg-lib-libXau-devel
BuildRequires:	xorg-lib-libXaw-devel
BuildRequires:	xorg-lib-libXdamage-devel
BuildRequires:	xorg-lib-libXdmcp-devel
BuildRequires:	xorg-lib-libXext-devel >= 1.0.99.4
BuildRequires:	xorg-lib-libXfont-devel >= 1.4.2
BuildRequires:	xorg-lib-libXi-devel >= 1.2.99.1
BuildRequires:	xorg-lib-libXmu-devel
BuildRequires:	xorg-lib-libXpm-devel
BuildRequires:	xorg-lib-libXrender-devel
BuildRequires:	xorg-lib-libXres-devel
BuildRequires:	xorg-lib-libXt-devel >= 1.0.0
BuildRequires:	xorg-lib-libXtst-devel >= 1.0.99.2
BuildRequires:	xorg-lib-libXv-devel
BuildRequires:	xorg-lib-libXxf86dga-devel
BuildRequires:	xorg-lib-libXxf86misc-devel
BuildRequires:	xorg-lib-libXxf86vm-devel
%{?with_dmx:BuildRequires:	xorg-lib-libdmx-devel >= 1.0.99.1}
BuildRequires:	xorg-lib-libfontenc-devel
BuildRequires:	xorg-lib-libpciaccess-devel >= 0.12.901
BuildRequires:	xorg-lib-libxkbfile-devel
BuildRequires:	xorg-lib-libxkbui-devel >= 1.0.2
BuildRequires:	xorg-lib-xtrans-devel >= 1.2.2
BuildRequires:	xorg-proto-bigreqsproto-devel >= 1.1.0
BuildRequires:	xorg-proto-compositeproto-devel >= 0.4
BuildRequires:	xorg-proto-damageproto-devel >= 1.1
%{?with_dmx:BuildRequires:	xorg-proto-dmxproto-devel >= 2.2.99.1}
%{?with_dri2:BuildRequires:	xorg-proto-dri2proto-devel >= 2.8}
BuildRequires:	xorg-proto-fixesproto-devel >= 5.0
BuildRequires:	xorg-proto-fontcacheproto-devel
BuildRequires:	xorg-proto-fontsproto-devel
BuildRequires:	xorg-proto-glproto-devel >= 1.4.16
BuildRequires:	xorg-proto-inputproto-devel >= 2.2.99.1
BuildRequires:	xorg-proto-kbproto-devel >= 1.0.3
BuildRequires:	xorg-proto-printproto-devel
BuildRequires:	xorg-proto-randrproto-devel >= 1.4.0
%{?with_record:BuildRequires:	xorg-proto-recordproto-devel >= 1.13.99.1}
BuildRequires:	xorg-proto-renderproto-devel >= 0.11
BuildRequires:	xorg-proto-resourceproto-devel >= 1.2.0
BuildRequires:	xorg-proto-scrnsaverproto-devel >= 1.1
BuildRequires:	xorg-proto-videoproto-devel
BuildRequires:	xorg-proto-xcmiscproto-devel >= 1.2.0
BuildRequires:	xorg-proto-xextproto-devel >= 1:7.2.0
%{?with_xf86bigfont:BuildRequires:	xorg-proto-xf86bigfontproto-devel >= 1.2.0}
BuildRequires:	xorg-proto-xf86dgaproto-devel >= 2.0.99.1
BuildRequires:	xorg-proto-xf86driproto-devel >= 2.1.0
BuildRequires:	xorg-proto-xf86miscproto-devel
BuildRequires:	xorg-proto-xf86vidmodeproto-devel >= 2.2.99.1
BuildRequires:	xorg-proto-xineramaproto-devel
BuildRequires:	xorg-proto-xproto-devel >= 7.0.22
BuildRequires:	xorg-sgml-doctools >= 1.8
BuildRequires:	xorg-util-util-macros >= 1.14
#BR: tslib (for KDRIVE only)
Requires(triggerpostun):	sed >= 4.0
Requires:	pixman >= %{pixman_ver}
Requires:	xkeyboard-config
# for rgb.txt
Requires:	xorg-app-rgb >= 0.99.3
Requires:	xorg-app-xkbcomp
%{?with_hal:Suggests:	hal}
Suggests:	udev-acl >= 1:143
%{?with_udev:Suggests:	udev-core >= 1:143}
Suggests:	xorg-driver-input-evdev
# xserver requires fixed and cursor fonts
Requires:	xorg-font-font-alias
Requires:	xorg-font-font-cursor-misc
Requires:	xorg-font-font-misc-misc-base >= 1.0.0-0.3
Suggests:	dbus-x11 >= 1.0
Suggests:	xkeyboard-config
# Usual desktop setups need least one video driver to run, see xorg.log which one exactly
Suggests:	xorg-driver-video
Provides:	xorg-xserver-server(ansic-abi) = %{xorg_xserver_server_ansic_abi}
Provides:	xorg-xserver-server(extension-abi) = %{xorg_xserver_server_extension_abi}
Provides:	xorg-xserver-server(font-abi) = %{xorg_xserver_server_font_abi}
Provides:	xorg-xserver-server(videodrv-abi) = %{xorg_xserver_server_videodrv_abi}
Provides:	xorg-xserver-server(xinput-abi) = %{xorg_xserver_server_xinput_abi}
Provides:	xorg-xserver-module(dri)
Provides:	xorg-xserver-libdri = %{version}-%{release}
Obsoletes:	X11-Xserver < 1:7.0.0
Obsoletes:	X11-driver-i2c < 1:7.0.0
Obsoletes:	X11-modules < 1:7.0.0
Obsoletes:	X11-setup < 1:7.0.0
Obsoletes:	XFree86-Xserver < 1:7.0.0
Obsoletes:	XFree86-modules < 1:7.0.0
Obsoletes:	XFree86-setup < 1:7.0.0
Obsoletes:	Xserver
Obsoletes:	xorg-xserver-server-xorgcfg
Obsoletes:	xorg-xserver-libdri
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

# avoid self-dependencies on included modules
%define		_noautoreq	libscanpci.so libxf1bpp.so

%description
Xorg server is a generally used X server which uses display hardware.
It requires proper driver for your display hardware.

%description -l pl.UTF-8
Serwer Xorg to podstawowy serwer X wyświetlający obraz na karcie
graficznej. Do działania wymaga odpowiedniego sterownika.

%package -n xorg-xserver-Xdmx
Summary:	Xdmx - distributed multi-head X server
Summary(pl.UTF-8):	Xdmx - rozproszony, wielomonitorowy serwer X
Group:		X11/Servers

%description -n xorg-xserver-Xdmx
Xdmx - distributed multi-head X server.

%description -n xorg-xserver-Xdmx -l pl.UTF-8
Xdmx - rozproszony, wielomonitorowy serwer X.

%package -n xorg-xserver-Xnest
Summary:	Xnest - nested X server
Summary(pl.UTF-8):	Xnest - zagnieżdżony serwer X
Group:		X11/Servers
Obsoletes:	X11-Xnest < 1:7.0.0
Obsoletes:	XFree86-Xnest < 1:7.0.0
Obsoletes:	Xserver-Xnest

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

%package -n xorg-xserver-Xephyr
Summary:	Xephyr - nested X server
Summary(pl.UTF-8):	Xephyr - zagnieżdżony serwer X
Group:		X11/Servers
Requires:	pixman >= %{pixman_ver}

%description -n xorg-xserver-Xephyr
Xephyr is a a kdrive server that outputs to a window on a pre-existing
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

%package -n xorg-xserver-Xfbdev
Summary:	Xfbdev - Linux framebuffer device X server
Summary(pl.UTF-8):	Xfbdev - serwer X dla framebuffera
Group:		X11/Servers

%description -n xorg-xserver-Xfbdev
Xfbdev is a Linux framebuffer device X server based on the kdrive X
server.

%description -n xorg-xserver-Xfbdev -l pl.UTF-8
Xfbdev jest serwerem X dla framebuffera opartym na kdrive.

%package -n xorg-xserver-Xvfb
Summary:	Xvfb - virtual framebuffer X server
Summary(pl.UTF-8):	Xvfb - serwer X z wirtualnym framebufferem
Group:		X11/Servers
# requires fixed and cursor fonts
Requires:	xorg-font-font-alias
Requires:	xorg-font-font-cursor-misc
Requires:	xorg-font-font-misc-misc-base >= 1.0.0-0.3
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
Requires:	xorg-xserver-Xvfb

%description -n xorg-xserver-Xvfb-init
This package contains init scripts for Xvfb and registers Xvfb as
system service.

%description -n xorg-xserver-Xvfb-init -l pl.UTF-8
Ten pakiet zawiera skrypty startowe dla Xvfb oraz rejestruje Xvfb jako
usługę systemową.

%package devel
Summary:	Header files for X.org server
Summary(pl.UTF-8):	Pliki nagłówkowe dla serwera X.org
Group:		X11/Development/Libraries
Requires:	libdrm-devel >= 2.4.39
Requires:	pixman-devel >= %{pixman_ver}
Requires:	xorg-lib-libpciaccess-devel >= 0.12.901
Requires:	xorg-lib-libxkbfile-devel
%{?with_dri2:Requires:	xorg-proto-dri2proto-devel >= 2.8}
Requires:	xorg-proto-fontsproto-devel
Requires:	xorg-proto-inputproto-devel >= 2.2.99.1
Requires:	xorg-proto-kbproto-devel >= 1.0.3
Requires:	xorg-proto-randrproto-devel >= 1.4.0
Requires:	xorg-proto-renderproto-devel >= 0.11
Requires:	xorg-proto-resourceproto-devel >= 1.2.0
Requires:	xorg-proto-scrnsaverproto-devel >= 1.1
Requires:	xorg-proto-videoproto-devel
Requires:	xorg-proto-xextproto-devel >= 1:7.2.0
Requires:	xorg-proto-xf86driproto-devel >= 2.1.0
Requires:	xorg-proto-xineramaproto-devel
Requires:	xorg-proto-xproto-devel >= 7.0.22
Obsoletes:	X11-Xserver-devel < 1:7.0.0
Obsoletes:	XFree86-Xserver-devel < 1:7.0.0

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
# Mesa version glapi tables in glx/ dir come from
Provides:	xorg-xserver-libglx(glapi) = 7.1.0
Provides:	xorg-xserver-module(glx)
Obsoletes:	X11-OpenGL-core < 1:7.0.0
Obsoletes:	XFree86-OpenGL-core < 1:7.0.0

%description -n xorg-xserver-libglx
GLX extension library for X.org server.

%description -n xorg-xserver-libglx -l pl.UTF-8
Biblioteka rozszerzenia GLX dla serwera X.org.

%prep
%setup -q -n xorg-server-%{version}
%patch0 -p0
%patch1 -p1

%patch3 -p1
%patch4 -p1
%patch5 -p1
%patch6 -p1

#unfortunately breaks build
#patch7 -p1

# xserver uses pixman-1 API/ABI so put that explictly here
sed -i -e 's#<pixman\.h#<pixman-1/pixman.h#g' ./fb/fb.h ./include/miscstruct.h ./render/picture.h

%build
API=$(awk '/#define ABI_ANSIC_VERSION/ { split($0,A,/[(,)]/); printf("%d.%d",A[2], A[3]); }' hw/xfree86/common/xf86Module.h)
if [ $API != %{xorg_xserver_server_ansic_abi} ]; then
	echo "Set %%define xorg_xserver_server_ansic_abi to $API and rerun."
	exit 1
fi

API=$(awk '/#define ABI_EXTENSION_VERSION/ { split($0,A,/[(,)]/); printf("%d.%d",A[2], A[3]); }' hw/xfree86/common/xf86Module.h)
if [ $API != %{xorg_xserver_server_extension_abi} ]; then
	echo "Set %%define xorg_xserver_server_extension_abi to $API and rerun."
	exit 1
fi

API=$(awk '/#define ABI_FONT_VERSION/ { split($0,A,/[(,)]/); printf("%d.%d",A[2], A[3]); }' hw/xfree86/common/xf86Module.h)
if [ $API != %{xorg_xserver_server_font_abi} ]; then
	echo "Set %%define xorg_xserver_server_font_abi to $API and rerun."
	exit 1
fi
API=$(awk '/#define ABI_VIDEODRV_VERSION/ { split($0,A,/[(,)]/); printf("%d.%d",A[2], A[3]); }' hw/xfree86/common/xf86Module.h)
if [ $API != %{xorg_xserver_server_videodrv_abi} ]; then
	echo "Set %%define xorg_xserver_server_videodrv_abi to $API and rerun."
	exit 1
fi
API=$(awk '/#define ABI_XINPUT_VERSION/ { split($0,A,/[(,)]/); printf("%d.%d",A[2], A[3]); }' hw/xfree86/common/xf86Module.h)
if [ $API != %{xorg_xserver_server_xinput_abi} ]; then
	echo "Set %%define xorg_xserver_server_xinput_abi to $API and rerun."
	exit 1
fi

%{__libtoolize}
%{__aclocal} -I m4
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--with-os-name="PLD/Linux" \
	--with-os-vendor="PLD/Team" \
	--without-fop \
	%{?with_dbus:--enable-config-dbus} \
	--enable-config-hal%{!?with_hal:=no} \
	--enable-config-udev%{!?with_udev:=no} \
	--enable-aiglx \
	--enable-dga \
	%{?with_dmx:--enable-dmx} \
	--enable-glx-tls \
	--enable-install-libxf86config \
	%{?with_record:--enable-record} \
	--enable-kdrive \
	%{?with_xcsecurity:--enable-xcsecurity} \
	--enable-xephyr \
	%{?with_xf86bigfont:--enable-xf86bigfont} \
	--enable-xfbdev \
	%{?with_xselinux:--enable-xselinux} \
	--enable-glx-tls \
	--disable-xfake \
	--enable-secure-rpc \
	--%{?with_dri2:en}%{!?with_dri2:dis}able-dri2 \
	--with-default-font-path="%{_fontsdir}/misc,%{_fontsdir}/TTF,%{_fontsdir}/OTF,%{_fontsdir}/Type1,%{_fontsdir}/100dpi,%{_fontsdir}/75dpi" \
	--with-xkb-output=/var/lib/xkb

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT


[ -e $RPM_BUILD_ROOT%{_mandir}/man5/xorg.conf.d.5x ] && \
	echo ".so man5/xorg.conf.5x" > $RPM_BUILD_ROOT%{_mandir}/man5/xorg.conf.d.5x || \
	exit 1

install -Dp %{SOURCE2} $RPM_BUILD_ROOT/etc/pam.d/xserver
install -d $RPM_BUILD_ROOT/etc/{security/console.apps,X11/xorg.conf.d}
install -d $RPM_BUILD_ROOT%{_libdir}/xorg/modules/{dri,drivers,input}
install -d $RPM_BUILD_ROOT%{_datadir}/X11/xorg.conf.d

:> $RPM_BUILD_ROOT/etc/security/console.apps/xserver
:> $RPM_BUILD_ROOT/etc/security/blacklist.xserver

rm -f $RPM_BUILD_ROOT%{_libdir}/xorg/modules/{*,*/*}.{la,a}

cp -p %{SOURCE1} $RPM_BUILD_ROOT%{_datadir}/X11/xorg.conf.d/10-quirks.conf

install -d $RPM_BUILD_ROOT/etc/rc.d/init.d
install -d $RPM_BUILD_ROOT/etc/sysconfig
install -p %{SOURCE10} $RPM_BUILD_ROOT/etc/rc.d/init.d/Xvfb
cp -p %{SOURCE11} $RPM_BUILD_ROOT/etc/sysconfig/Xvfb

install -d $RPM_BUILD_ROOT%{_usrsrc}/%{name}-%{version}
cp -a * $RPM_BUILD_ROOT%{_usrsrc}/%{name}-%{version}
cd $RPM_BUILD_ROOT%{_usrsrc}/%{name}-%{version}
%{__make} distclean
find '(' -name '*~' -o -name '*.orig' ')' -print0 | xargs -0 -r -l512 rm -f
find -name '*.h' | xargs chmod a-x

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
%doc COPYING ChangeLog README
%attr(755,root,root) %{_bindir}/X
%attr(755,root,root) %{_bindir}/Xorg
%attr(4755,root,root) %{_bindir}/Xwrapper
%attr(755,root,root) %{_bindir}/cvt
%attr(755,root,root) %{_bindir}/gtf
%dir %{_libdir}/xorg
%{_libdir}/xorg/protocol.txt
%dir %{_libdir}/xorg/modules
%dir %{_libdir}/xorg/modules/dri
%dir %{_libdir}/xorg/modules/drivers
%dir %{_libdir}/xorg/modules/extensions
%dir %{_libdir}/xorg/modules/input
%dir %{_libdir}/xorg/modules/multimedia
%attr(755,root,root) %{_libdir}/xorg/modules/multimedia/*.so
%attr(755,root,root) %{_libdir}/xorg/modules/lib*.so
%dir /var/lib/xkb
/var/lib/xkb/README.compiled
%attr(640,root,root) %config(noreplace) %verify(not md5 mtime size) /etc/pam.d/xserver
%attr(640,root,root) %config(noreplace) %verify(not md5 mtime size) /etc/security/blacklist.xserver
%config(missingok) /etc/security/console.apps/xserver
%{?with_dbus:/etc/dbus-1/system.d/xorg-server.conf}
%dir /etc/X11/xorg.conf.d
%dir %{_datadir}/X11/xorg.conf.d
# overwrite these settings with local configs in /etc/X11/xorg.conf.d
%verify(not md5 mtime size) %{_datadir}/X11/xorg.conf.d/*.conf
%{_mandir}/man1/Xorg.1x*
%{_mandir}/man1/Xserver.1x*
%{_mandir}/man1/cvt.1*
%{_mandir}/man1/gtf.1x*
%{_mandir}/man4/exa.4*
%{_mandir}/man4/fbdevhw.4*
%{_mandir}/man5/xorg.conf.5x*
%{_mandir}/man5/xorg.conf.d.5x

%if %{with dmx}
%files -n xorg-xserver-Xdmx
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/Xdmx
%attr(755,root,root) %{_bindir}/dmxaddinput
%attr(755,root,root) %{_bindir}/dmxaddscreen
%attr(755,root,root) %{_bindir}/dmxinfo
%attr(755,root,root) %{_bindir}/dmxreconfig
%attr(755,root,root) %{_bindir}/dmxresize
%attr(755,root,root) %{_bindir}/dmxrminput
%attr(755,root,root) %{_bindir}/dmxrmscreen
%attr(755,root,root) %{_bindir}/dmxtodmx
%attr(755,root,root) %{_bindir}/dmxwininfo
%attr(755,root,root) %{_bindir}/vdltodmx
%attr(755,root,root) %{_bindir}/xdmxconfig
%{_mandir}/man1/Xdmx.1x*
%{_mandir}/man1/dmxtodmx.1x*
%{_mandir}/man1/vdltodmx.1x*
%{_mandir}/man1/xdmxconfig.1x*
%endif

%files -n xorg-xserver-Xnest
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/Xnest
%{_mandir}/man1/Xnest.1x*

%files -n xorg-xserver-Xephyr
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/Xephyr
%{_mandir}/man1/Xephyr.1x*

%files -n xorg-xserver-Xfbdev
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/Xfbdev

%files -n xorg-xserver-Xvfb
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/Xvfb
%{_mandir}/man1/Xvfb.1x*

%files -n xorg-xserver-Xvfb-init
%defattr(644,root,root,755)
%attr(754,root,root) /etc/rc.d/init.d/Xvfb
%config(noreplace) %verify(not md5 mtime size) /etc/sysconfig/Xvfb

%files devel
%defattr(644,root,root,755)
%doc doc/{Xinput,Xserver-spec}.html
%{_includedir}/xorg
%{_libdir}/libxf86config.a
%{_libdir}/libxf86config.la
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
