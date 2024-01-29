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

# fix for sb2 (sb2 needs to hook open, openat):
Patch0: 0001-Revert-linux-user-Use-safe_syscall-for-open-and-open.patch
Patch1: 0002-Revert-linux-user-Use-safe_syscall-for-execve-syscal.patch
Patch2: 0003-Revert-linux-user-Use-safe_syscall-wrapper-for-send-.patch
Patch3: 0004-Revert-linux-user-Use-safe_syscall-wrapper-for-accep.patch
Patch4: 0005-Revert-linux-user-Use-safe_syscall-wrapper-for-conne.patch
Patch5: 0006-Revert-linux-user-Use-direct-syscall-for-utimensat.patch
# For obs getting stuck in getrandom
Patch7: 0008-crypto-check-if-getrandom-is-available-properly.patch
# fix openat syscall (breaks e.g. bc build)
Patch8: 0009-make-sure-mode-is-passed-to-openat-if-O_TMPFILE-is-s.patch
# make sure utimensat from glibc is being used (see sb2 fixes above)
Patch9: 0010-Revert-util-drop-old-utimensat-compat-code.patch
# one more revert for sb2
Patch10: 0011-Revert-linux-user-Use-safe_syscall-wrapper-for-fcntl.patch
# fix f_flags in statfs64
Patch11: 0012-linux-user-Support-f_flags-in-statfs64-when-availabl.patch
# fix build failures
Patch12: 0013-linux-user-Force-avx1-and-avx2-off-since-they-cause-.patch
# fix qemu-user start issues due to running on 64 bit kernel
Patch13: 0014-linux-user-disable-commpage.patch
# fix assert which breaks ustr tests
Patch14: 0015-linux-user-fix-guest-address-space-assert.patch
# Use glibc statx function instead of statx syscall to allow sb2 to hook the call
Patch15: 0016-linux-user-Use-glibc-statx-function-instead-of-statx.patch

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
