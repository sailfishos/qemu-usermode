# Target architectures to build emulators of
%define target_list aarch64 arm mipsel

Name:       qemu-usermode
Summary:    Universal CPU emulator
Version:    5.1.0
Release:    1
License:    GPLv2 and BSD and MIT and CC-BY
ExclusiveArch:  %{ix86}
URL:        https://www.qemu.org/
Source0:    %{name}-%{version}.tar.xz
Source1:    qemu-binfmt-conf.sh

# For obs getting stuck in getrandom
Patch0: 0001-crypto-check-if-getrandom-is-available-properly.patch
# fix f_flags in statfs64
Patch1: 0002-linux-user-Support-f_flags-in-statfs64-when-availabl.patch
# fix build failures
Patch2: 0003-linux-user-Force-avx1-and-avx2-off-since-they-cause-.patch
# fix qemu-user start issues due to running on 64 bit kernel
Patch3: 0004-linux-user-disable-commpage.patch
# fix assert which breaks ustr tests
Patch4: 0005-linux-user-fix-guest-address-space-assert.patch
# sb2 can handle syscalls now, but not if they are not going through the c interface
Patch5: 0006-linux-user-Disable-safe_syscall-functionality-for-sb.patch

BuildRequires:  pkgconfig(ext2fs)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(zlib)
BuildRequires:  bison
BuildRequires:  flex
BuildRequires:  curl-devel
BuildRequires:  zlib-static
BuildRequires:  glibc-static
BuildRequires:  python3-devel
BuildRequires:  glib2-static
BuildRequires:  pcre-static
# Hard requirement for version >= 1.3
BuildRequires:  pixman-devel
Requires: %{name}-common = %{version}

%description
QEMU is an extremely well-performing CPU emulator that allows you to choose between simulating an entire system and running userspace binaries for different architectures under your native operating system. It currently emulates x86, ARM, PowerPC and SPARC CPUs as well as PC and PowerMac systems.


%prep
%autosetup -p1 -n qemu-usermode-%{version}/upstream

%build
CFLAGS=`echo $CFLAGS | sed 's|-fno-omit-frame-pointer||g'` ; export CFLAGS ;
CFLAGS=`echo $CFLAGS | sed 's|-O2|-O|g'` ; export CFLAGS ;

CONFIGURE_FLAGS=" \
    --prefix=/usr \
    --sysconfdir=%_sysconfdir \
    --interp-prefix=/usr/share/qemu/qemu-i386 \
    --disable-system \
    --enable-linux-user \
    --disable-werror \
    --disable-strip \
    --disable-zstd \
    --disable-linux-io-uring \
    --target-list=$((for target in %{target_list}; do echo -n ${target}-linux-user,; done) | sed -e 's/,$//')"

for mode in static dynamic; do
    mkdir -p build-$mode
    cd build-$mode
    if [ $mode = static ]; then
        ../configure --static $CONFIGURE_FLAGS --disable-tools
    else
        ../configure $CONFIGURE_FLAGS --enable-tools
    fi
    make V=1 %{?_smp_mflags}
    cd ..
done

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}%{_bindir}
mkdir -p %{buildroot}%{_sbindir}
install -m 755 %{SOURCE1} $RPM_BUILD_ROOT/%{_sbindir}

for mode in static dynamic; do
    cd build-$mode
    %make_install
    for target in %{target_list}; do
        mv %{buildroot}%{_bindir}/qemu-${target} %{buildroot}%{_bindir}/qemu-${target}-${mode}
    done
    cd ..
done

rm -f $RPM_BUILD_ROOT/usr/share/qemu/openbios-ppc
rm -f $RPM_BUILD_ROOT/usr/share/qemu/openbios-sparc32
rm -f $RPM_BUILD_ROOT/usr/share/qemu/openbios-sparc64
rm -f $RPM_BUILD_ROOT/usr/libexec/qemu-bridge-helper
rm -rf $RPM_BUILD_ROOT/etc
rm -rf $RPM_BUILD_ROOT/%{_datadir}
rm -rf $RPM_BUILD_ROOT/usr/include
rm -rf $RPM_BUILD_ROOT/usr/lib/libcacard*
rm -rf $RPM_BUILD_ROOT/usr/lib/pkgconfig/libcacard.pc
rm -rf $RPM_BUILD_ROOT/usr/bin/vscclient

# Install binfmt
%global binfmt_dir %{buildroot}%{_exec_prefix}/lib/binfmt.d
mkdir -p %{binfmt_dir}

./scripts/qemu-binfmt-conf.sh --systemd ALL --exportdir %{binfmt_dir} --qemu-path %{_bindir}
for i in %{binfmt_dir}/*; do
    mv $i $(echo $i | sed 's/.conf/-dynamic.conf/')
done

for regularfmt in %{binfmt_dir}/*; do
  staticfmt="$(echo $regularfmt | sed 's/-dynamic/-static/g')"
  cat $regularfmt | tr -d '\n' | sed "s/:$/-static:F/" > $staticfmt
done

%files
%defattr(-,root,root,-)
%{_bindir}/qemu-*-dynamic
%{_sbindir}/qemu-binfmt-conf.sh
%{_exec_prefix}/lib/binfmt.d/qemu-*-dynamic.conf

%package common
Summary:  Universal CPU emulator (common utilities)

%description common
This package provides common qemu utilities.

%files common
%defattr(-,root,root,-)
%{_bindir}/qemu-img
%{_bindir}/qemu-io
%{_bindir}/qemu-nbd
%{_bindir}/qemu-ga
%{_bindir}/ivshmem-client
%{_bindir}/ivshmem-server
%{_bindir}/qemu-edid
%{_bindir}/elf2dmp
%{_bindir}/qemu-storage-daemon

%package static
Summary:  Universal CPU emulator (static userspace emulators)
Requires: %{name}-common = %{version}

%description static
This package provides static builds of userspace CPU emulators.

%files static
%defattr(-,root,root,-)
%{_bindir}/qemu-*-static
%{_exec_prefix}/lib/binfmt.d/qemu-*-static.conf
