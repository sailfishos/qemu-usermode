# Target architectures to build emulators of
%define target_list aarch64 arm mipsel

Name:       qemu-usermode
Summary:    Universal CPU emulator
Version:    2.6.2
Release:    1
Group:      System/Emulators/PC
License:    GPLv2
ExclusiveArch:  %{ix86}
URL:        https://launchpad.net/qemu-linaro/
Source0:    qemu-%{version}.tar.xz
Source1:    qemu-binfmt-conf.sh
Patch0001:      0001-XXX-dont-dump-core-on-sigabort.patch
Patch0002:      0002-qemu-0.9.0.cvs-binfmt.patch
Patch0003:      0003-qemu-cvs-alsa_bitfield.patch
Patch0004:      0004-qemu-cvs-alsa_ioctl.patch
Patch0005:      0005-qemu-cvs-alsa_mmap.patch
Patch0006:      0006-qemu-cvs-gettimeofday.patch
Patch0007:      0007-qemu-cvs-ioctl_debug.patch
Patch0008:      0008-qemu-cvs-ioctl_nodirection.patch
Patch0009:      0009-block-vmdk-Support-creation-of-SCSI.patch
Patch0010:      0010-linux-user-add-binfmt-wrapper-for-a.patch
Patch0011:      0011-PPC-KVM-Disable-mmu-notifier-check.patch
Patch0012:      0012-linux-user-fix-segfault-deadlock.patch
Patch0013:      0013-linux-user-binfmt-support-host-bina.patch
Patch0014:      0014-linux-user-Ignore-broken-loop-ioctl.patch
Patch0015:      0015-linux-user-lock-tcg.patch
Patch0016:      0016-linux-user-Run-multi-threaded-code-.patch
Patch0017:      0017-linux-user-lock-tb-flushing-too.patch
Patch0018:      0018-linux-user-Fake-proc-cpuinfo.patch
Patch0019:      0019-linux-user-implement-FS_IOC_GETFLAG.patch
Patch0020:      0020-linux-user-implement-FS_IOC_SETFLAG.patch
Patch0021:      0021-linux-user-XXX-disable-fiemap.patch
Patch0022:      0022-slirp-nooutgoing.patch
Patch0023:      0023-vnc-password-file-and-incoming-conn.patch
Patch0024:      0024-linux-user-add-more-blk-ioctls.patch
Patch0025:      0025-linux-user-use-target_ulong.patch
Patch0026:      0026-block-Add-support-for-DictZip-enabl.patch
Patch0027:      0027-block-Add-tar-container-format.patch
Patch0028:      0028-Legacy-Patch-kvm-qemu-preXX-dictzip.patch
Patch0029:      0029-console-add-question-mark-escape-op.patch
Patch0030:      0030-Make-char-muxer-more-robust-wrt-sma.patch
Patch0031:      0031-linux-user-lseek-explicitly-cast-no.patch
Patch0032:      0032-virtfs-proxy-helper-Provide-__u64-f.patch
Patch0033:      0033-configure-Enable-PIE-for-ppc-and-pp.patch
Patch0034:      0034-Raise-soft-address-space-limit-to-h.patch
Patch0035:      0035-increase-x86_64-physical-bits-to-42.patch
Patch0036:      0036-vnc-provide-fake-color-map.patch
Patch0037:      0037-vga-Raise-VRAM-to-16-MiB-for-pc-0.1.patch
Patch0038:      0038-i8254-Fix-migration-from-SLE11-SP2.patch
Patch0039:      0039-acpi_piix4-Fix-migration-from-SLE11.patch
Patch0040:      0040-qtest-Increase-socket-timeout-to-ac.patch
Patch0041:      0041-dictzip-Fix-on-big-endian-systems.patch
Patch0042:      0042-Fix-tigervnc-long-press-issue.patch
Patch0043:      0043-xen_disk-Add-suse-specific-flush-di.patch
Patch0044:      0044-Split-large-discard-requests-from-b.patch
Patch0045:      0045-fix-xen-hvm-direct-kernel-boot.patch
Patch0046:      0046-xen-introduce-dummy-system-device.patch
Patch0047:      0047-xen-write-information-about-support.patch
Patch0048:      0048-xen-add-pvUSB-backend.patch
Patch0049:      0049-xen-move-xen_sysdev-to-xen_backend..patch
Patch0050:      0050-vnc-add-configurable-keyboard-delay.patch
Patch0051:      0051-xen-SUSE-xenlinux-unplug-for-emulat.patch
Patch0052:      0052-configure-add-echo_version-helper.patch
Patch0053:      0053-configure-support-vte-2.91.patch
Patch0054:      0054-scsi-esp-fix-migration.patch
Patch0055:      0055-hw-arm-virt-mark-the-PCIe-host-cont.patch
Patch0056:      0056-xen-when-removing-a-backend-don-t-r.patch
Patch0057:      0057-xen-drain-submit-queue-in-xen-usb-b.patch
Patch0058:      0058-qcow2-avoid-extra-flushes-in-qcow2.patch
Patch0059:      0059-qemu-bridge-helper-reduce-security-.patch
Patch0060:      0060-xen-use-a-common-function-for-pv-an.patch
Patch0061:      0061-xen_platform-unplug-also-SCSI-disks.patch
Patch0062:      0062-virtio-check-vring-descriptor-buffe.patch
Patch0063:      0063-net-vmxnet3-check-for-device_active.patch
Patch0064:      0064-net-vmxnet-initialise-local-tx-desc.patch
Patch0065:      0065-scsi-pvscsi-avoid-infinite-loop-whi.patch
Patch0066:      0066-ARM-KVM-Enable-in-kernel-timers-wit.patch
Patch0067:      0067-hw-net-Fix-a-heap-overflow-in-xlnx..patch
Patch0068:      0068-vmsvga-correct-bitmap-and-pixmap-si.patch
Patch0069:      0069-usb-xhci-fix-memory-leak-in-usb_xhc.patch
Patch0070:      0070-virtio-add-check-for-descriptor-s-m.patch
Patch0071:      0071-net-mcf-limit-buffer-descriptor-cou.patch
Patch0072:      0072-usb-ehci-fix-memory-leak-in-ehci_pr.patch
Patch0073:      0073-xhci-limit-the-number-of-link-trbs-.patch
Patch0074:      0074-9pfs-allocate-space-for-guest-origi.patch
Patch0075:      0075-9pfs-fix-memory-leak-in-v9fs_link.patch
Patch0076:      0076-9pfs-fix-potential-host-memory-leak.patch
Patch0077:      0077-9pfs-fix-memory-leak-in-v9fs_write.patch
Patch0078:      0078-char-serial-check-divider-value-aga.patch
Patch0079:      0079-net-pcnet-check-rx-tx-descriptor-ri.patch
Patch0080:      0080-net-eepro100-fix-memory-leak-in-dev.patch
Patch0081:      0081-net-rocker-set-limit-to-DMA-buffer-.patch
Patch0082:      0082-net-rtl8139-limit-processing-of-rin.patch
Patch0083:      0083-audio-intel-hda-check-stream-entry-.patch
Patch0084:      0084-virtio-gpu-fix-memory-leak-in-virti.patch
Patch0085:      0085-9pfs-fix-integer-overflow-issue-in-.patch
Patch0086:      0086-dma-rc4030-limit-interval-timer-rel.patch
Patch0087:      0087-net-imx-limit-buffer-descriptor-cou.patch
Patch0088:      0088-target-i386-Implement-CPUID-0xB-Ext.patch
Patch0089:      0089-target-i386-present-virtual-L3-cach.patch
Patch0090:      0090-migration-fix-inability-to-save-VM-.patch
Patch0091:      0091-ui-gtk-Fix-a-runtime-warning-on-vte.patch
Patch0092:      0092-gtk-don-t-leak-the-GtkBorder-with-V.patch
Patch0093:      0093-xen-fix-ioreq-handling.patch
Patch0094:      0094-macio-Use-blk_drain-instead-of-blk_.patch
Patch0095:      0095-rbd-Switch-rbd_start_aio-to-byte-ba.patch
Patch0096:      0096-virtio-blk-Release-s-rq-queue-at-sy.patch
Patch0097:      0097-virtio-blk-Remove-stale-comment-abo.patch
Patch0098:      0098-block-reintroduce-bdrv_flush_all.patch
Patch0099:      0099-qemu-use-bdrv_flush_all-for-vm_stop.patch
Patch0100:      0100-block-backend-remove-blk_flush_all.patch
Patch0101:      0101-char-fix-missing-return-in-error-pa.patch
Patch0102:      0102-rbd-shift-byte-count-as-a-64-bit-va.patch
Patch0103:      0103-mirror-use-bdrv_drained_begin-bdrv_.patch
Patch0104:      0104-block-curl-Use-BDRV_SECTOR_SIZE.patch
Patch0105:      0105-block-curl-Fix-return-value-from-cu.patch
Patch0106:      0106-block-curl-Remember-all-sockets.patch
Patch0107:      0107-block-curl-Do-not-wait-for-data-bey.patch
Patch0108:      0108-virtio-allow-per-device-class-legac.patch
Patch0109:      0109-virtio-net-mark-VIRTIO_NET_F_GSO-as.patch
Patch0110:      0110-vhost-adapt-vhost_verify_ring_mappi.patch
Patch0111:      0111-ivshmem-Fix-64-bit-memory-bar-confi.patch
Patch0112:      0112-intel_iommu-fix-incorrect-device-in.patch
Patch0113:      0113-9pfs-fix-information-leak-in-xattr-.patch
Patch0114:      0114-9pfs-fix-memory-leak-in-v9fs_xattrc.patch
Patch0115:      0115-net-mcf-check-receive-buffer-size-r.patch
Patch0116:      0116-virtio-gpu-fix-memory-leak-in-updat.patch
Patch0117:      0117-virtio-gpu-fix-information-leak-in-.patch
Patch0118:      0118-9pfs-adjust-the-order-of-resource-c.patch
Patch0119:      0119-9pfs-add-cleanup-operation-in-FileO.patch
Patch0120:      0120-9pfs-add-cleanup-operation-for-hand.patch
Patch0121:      0121-9pfs-add-cleanup-operation-for-prox.patch
Patch0122:      0122-virtio-gpu-call-cleanup-mapping-fun.patch
Patch0123:      0123-string-input-visitor-Fix-uint64-par.patch
Patch0124:      0124-test-string-input-visitor-Add-int-t.patch
Patch0125:      0125-test-string-input-visitor-Add-uint6.patch
Patch0126:      0126-tests-Add-QOM-property-unit-tests.patch
Patch0127:      0127-tests-Add-scsi-disk-test.patch
Patch0128:      0128-usb-ehci-fix-memory-leak-in-ehci_in.patch
Patch0129:      0129-usbredir-free-vm_change_state_handl.patch
Patch0130:      0130-virtio-gpu-fix-information-leak-in-.patch
Patch0131:      0131-display-cirrus-check-vga-bits-per-p.patch
Patch0132:      0132-display-cirrus-ignore-source-pitch-.patch
Patch0133:      0133-virtio-gpu-check-early-scanout-id.patch
Patch0134:      0134-virtio-gpu-check-max_outputs-value.patch
Patch0135:      0135-virtio-gpu-check-max_outputs-only.patch
Patch0136:      0136-virtio-gpu-use-VIRTIO_GPU_MAX_SCANO.patch
Patch0137:      0137-display-virtio-gpu-3d-check-virgl-c.patch
Patch0138:      0138-watchdog-6300esb-add-exit-function.patch
Patch0139:      0139-virtio-gpu-3d-fix-memory-leak-in-re.patch
Patch0140:      0140-virtio-gpu-fix-memory-leak-in-resou.patch
Patch0141:      0141-audio-es1370-add-exit-function.patch
Patch0142:      0142-audio-ac97-add-exit-function.patch
Patch0143:      0143-sd-sdhci-check-data-length-during-d.patch
Patch0144:      0144-virtio-fix-vq-inuse-recalc-after-mi.patch
Patch0145:      0145-s390x-kvm-fix-small-race-reboot-vs..patch
Patch0146:      0146-cirrus-handle-negative-pitch-in-cir.patch
Patch0147:      0147-cirrus-fix-blit-address-mask-handli.patch
Patch0148:      0148-cirrus-fix-oob-access-issue-CVE-201.patch
Patch0149:      0149-megasas-fix-guest-triggered-memory-.patch
Patch0150:      0150-cirrus-fix-patterncopy-checks.patch
Patch0151:      0151-cirrus-add-blit_is_unsafe-call-to-c.patch
Patch0152:      0152-usb-ccid-check-ccid-apdu-length.patch
Patch0153:      0153-virtio-gpu-fix-resource-leak-in-vir.patch
Patch0154:      0154-i386-Allow-cpuid-bit-override.patch
Patch0155:      0155-9pfs-fix-crash-when-fsdev-is-missin.patch
Patch0156:      0156-9pfs-move-pdus-to-V9fsState.patch
Patch0157:      0157-9pfs-fix-off-by-one-error-in-PDU-fr.patch
Patch0158:      0158-9pfs-local-move-xattr-security-ops-.patch
Patch0159:      0159-9pfs-remove-side-effects-in-local_i.patch
Patch0160:      0160-9p-introduce-the-V9fsDir-type.patch
Patch0161:      0161-9pfs-remove-side-effects-in-local_o.patch
Patch0162:      0162-9pfs-introduce-relative_openat_nofo.patch
Patch0163:      0163-9pfs-local-keep-a-file-descriptor-o.patch
Patch0164:      0164-9pfs-local-open-opendir-don-t-follo.patch
Patch0165:      0165-9pfs-local-lgetxattr-don-t-follow-s.patch
Patch0166:      0166-9pfs-local-llistxattr-don-t-follow-.patch
Patch0167:      0167-9pfs-local-lsetxattr-don-t-follow-s.patch
Patch0168:      0168-9pfs-local-lremovexattr-don-t-follo.patch
Patch0169:      0169-9pfs-local-unlinkat-don-t-follow-sy.patch
Patch0170:      0170-9pfs-local-remove-don-t-follow-syml.patch
Patch0171:      0171-9pfs-local-utimensat-don-t-follow-s.patch
Patch0172:      0172-9pfs-local-statfs-don-t-follow-syml.patch
Patch0173:      0173-9pfs-local-truncate-don-t-follow-sy.patch
Patch0174:      0174-9pfs-local-readlink-don-t-follow-sy.patch
Patch0175:      0175-9pfs-local-lstat-don-t-follow-symli.patch
Patch0176:      0176-9pfs-local-renameat-don-t-follow-sy.patch
Patch0177:      0177-9pfs-local-rename-use-renameat.patch
Patch0178:      0178-9pfs-local-improve-error-handling-i.patch
Patch0179:      0179-9pfs-local-link-don-t-follow-symlin.patch
Patch0180:      0180-9pfs-local-chmod-don-t-follow-symli.patch
Patch0181:      0181-9pfs-local-chown-don-t-follow-symli.patch
Patch0182:      0182-9pfs-local-symlink-don-t-follow-sym.patch
Patch0183:      0183-9pfs-local-mknod-don-t-follow-symli.patch
Patch0184:      0184-9pfs-local-mkdir-don-t-follow-symli.patch
Patch0185:      0185-9pfs-local-open2-don-t-follow-symli.patch
Patch0186:      0186-9pfs-local-drop-unused-code.patch
Patch0187:      0187-9pfs-fix-bogus-fd-check-in-local_re.patch
Patch0188:      0188-9pfs-fix-fd-leak-in-local_opendir.patch
Patch0189:      0189-9pfs-fail-local_statfs-earlier.patch
Patch0190:      0190-9pfs-don-t-use-AT_EMPTY_PATH-in-loc.patch
Patch0191:      0191-9pfs-fix-O_PATH-build-break-with-ol.patch
Patch0192:      0192-9pfs-fix-vulnerability-in-openat_di.patch
Patch0193:      0193-9pfs-don-t-try-to-flush-self-and-av.patch
Patch0194:      0194-9pfs-fix-file-descriptor-leak.patch
Patch0195:      0195-9pfs-xattr-fix-memory-leak-in-v9fs_.patch
Patch0196:      0196-9pfs-introduce-v9fs_path_sprintf-he.patch
Patch0197:      0197-9pfs-local-set-the-path-of-the-expo.patch
Patch0198:      0198-xhci-apply-limits-to-loops.patch
Patch0199:      0199-sd-sdhci-check-transfer-mode-regist.patch
Patch0200:      0200-usb-ohci-limit-the-number-of-link-e.patch
Patch0201:      0201-cirrus-vnc-zap-bitblit-support-from.patch
Patch0202:      0202-tcg-i386-Check-the-size-of-instruct.patch
Patch0203:      0203-fix-cirrus_vga-fix-OOB-read-case-qe.patch
Patch0204:      0204-cirrus-stop-passing-around-dst-poin.patch
Patch0205:      0205-cirrus-stop-passing-around-src-poin.patch
Patch0206:      0206-cirrus-fix-off-by-one-in-cirrus_bit.patch
Patch0207:      0207-vmw_pvscsi-check-message-ring-page-.patch
Patch0208:      0208-xhci-guard-xhci_kick_epctx-against-.patch
Patch0209:      0209-usb-ehci-fix-memory-leak-in-ehci.patch
Patch0210:      0210-ide-core-add-cleanup-function.patch
Patch0211:      0211-ide-ahci-call-cleanup-function-in-a.patch
Patch0212:      0212-usb-ohci-fix-error-return-code-in-s.patch
Patch0213:      0213-input-limit-kbd-queue-depth.patch
Patch0214:      0214-audio-release-capture-buffers.patch
Patch0215:      0215-scsi-avoid-an-off-by-one-error-in-m.patch
Patch0216:      0216-9pfs-local-forbid-client-access-to-.patch
Patch0217:      0217-9pfs-local-fix-unlink-of-alien-file.patch
Patch0218:      0218-serial-fix-memory-leak-in-serial-ex.patch
Patch0219:      0219-megasas-do-not-read-DCMD-opcode-mor.patch
Patch0220:      0220-megasas-always-store-SCSIRequest-in.patch
Patch0221:      0221-9pfs-local-remove-use-correct-path-.patch
Patch0222:      0222-block-Allow-BDRV_REQ_FUA-through-bl.patch
Patch0223:      0223-block-Switch-blk_read_unthrottled-t.patch
Patch0224:      0224-block-Switch-blk_-write_zeroes-to-b.patch
Patch0225:      0225-block-Introduce-byte-based-aio-read.patch
Patch0226:      0226-ide-Switch-to-byte-based-aio-block-.patch
Patch0227:      0227-dma-helpers-change-interface-to-byt.patch
Patch0228:      0228-dma-helpers-change-BlockBackend-to-.patch
Patch0229:      0229-scsi-disk-introduce-a-common-base-c.patch
Patch0230:      0230-scsi-disk-introduce-dma_readv-and-d.patch
Patch0231:      0231-scsi-disk-add-need_fua_emulation-to.patch
Patch0232:      0232-scsi-disk-introduce-scsi_disk_req_c.patch
Patch0233:      0233-scsi-block-always-use-SG_IO.patch
Patch0234:      0234-scsi-block-fix-direction-of-BYTCHK-.patch
Patch0235:      0235-input-Decrement-queue-count-on-kbd-.patch
Patch0236:      0236-hid-Reset-kbd-modifiers-on-reset.patch
Patch0237:      0237-vnc-Set-default-kbd-delay-to-10ms.patch
Patch0238:      0238-xen-disk-don-t-leak-stack-data-via-.patch
Patch0239:      0239-IDE-Do-not-flush-empty-CDROM-drives.patch
Patch0240:      0240-nbd-Fully-initialize-client-in-case.patch
Patch0241:      0241-nbd-Fix-regression-on-resiliency-to.patch
Patch0242:      0242-qemu-nbd-Ignore-SIGPIPE.patch
Patch0243:      0243-usb-redir-fix-stack-overflow-in-usb.patch
Patch0244:      0244-multiboot-validate-multiboot-header.patch
Patch0245:      0245-slirp-check-len-against-dhcp-option.patch
Patch0246:      0246-exec-use-qemu_ram_ptr_length-to-acc.patch
Patch0247:      0247-vga-stop-passing-pointers-to-vga_dr.patch
Patch0248:      0248-io-monitor-encoutput-buffer-size-fr.patch
Patch0249:      0249-cirrus-fix-oob-access-in-mode4and5-.patch
Patch0250:      0250-9pfs-use-g_malloc0-to-allocate-spac.patch
Patch0251:      0251-scsi-disk-fix-reads-from-scsi-disk-.patch
Patch0252:      0252-xen-mapcache-store-dma-information-.patch
Patch0253:      0253-exec-Add-lock-parameter-to-qemu_ram.patch
Patch0254:      0254-i386-kvm-MSR_IA32_SPEC_CTRL-and-MSR.patch
Patch0255:      glibc-2_26-fixes.patch
BuildRequires:  pkgconfig(ext2fs)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(zlib)
BuildRequires:  bison
BuildRequires:  curl-devel
BuildRequires:  zlib-static
BuildRequires:  glibc-static
BuildRequires:  python-devel
BuildRequires:  glib2-static
BuildRequires:  pcre-static
BuildRequires:  pixman-devel
Requires: %{name}-common = %{version}

%description
QEMU is an extremely well-performing CPU emulator that allows you to choose between simulating an entire system and running userspace binaries for different architectures under your native operating system. It currently emulates x86, ARM, PowerPC and SPARC CPUs as well as PC and PowerMac systems.


%prep
%setup -q -n qemu-%{version}

%patch0001 -p1
%patch0002 -p1
%patch0003 -p1
%patch0004 -p1
%patch0005 -p1
%patch0006 -p1
%patch0007 -p1
%patch0008 -p1
%patch0009 -p1
%patch0010 -p1
%patch0011 -p1
%patch0012 -p1
%patch0013 -p1
%patch0014 -p1
%patch0015 -p1
%patch0016 -p1
%patch0017 -p1
%patch0018 -p1
%patch0019 -p1
%patch0020 -p1
%patch0021 -p1
%patch0022 -p1
%patch0023 -p1
%patch0024 -p1
%patch0025 -p1
%patch0026 -p1
%patch0027 -p1
%patch0028 -p1
%patch0029 -p1
%patch0030 -p1
%patch0031 -p1
%patch0032 -p1
%patch0033 -p1
%patch0034 -p1
%patch0035 -p1
%patch0036 -p1
%patch0037 -p1
%patch0038 -p1
%patch0039 -p1
%patch0040 -p1
%patch0041 -p1
%patch0042 -p1
%patch0043 -p1
%patch0044 -p1
%patch0045 -p1
%patch0046 -p1
%patch0047 -p1
%patch0048 -p1
%patch0049 -p1
%patch0050 -p1
%patch0051 -p1
%patch0052 -p1
%patch0053 -p1
%patch0054 -p1
%patch0055 -p1
%patch0056 -p1
%patch0057 -p1
%patch0058 -p1
%patch0059 -p1
%patch0060 -p1
%patch0061 -p1
%patch0062 -p1
%patch0063 -p1
%patch0064 -p1
%patch0065 -p1
%patch0066 -p1
%patch0067 -p1
%patch0068 -p1
%patch0069 -p1
%patch0070 -p1
%patch0071 -p1
%patch0072 -p1
%patch0073 -p1
%patch0074 -p1
%patch0075 -p1
%patch0076 -p1
%patch0077 -p1
%patch0078 -p1
%patch0079 -p1
%patch0080 -p1
%patch0081 -p1
%patch0082 -p1
%patch0083 -p1
%patch0084 -p1
%patch0085 -p1
%patch0086 -p1
%patch0087 -p1
%patch0088 -p1
%patch0089 -p1
%patch0090 -p1
%patch0091 -p1
%patch0092 -p1
%patch0093 -p1
%patch0094 -p1
%patch0095 -p1
%patch0096 -p1
%patch0097 -p1
%patch0098 -p1
%patch0099 -p1
%patch0100 -p1
%patch0101 -p1
%patch0102 -p1
%patch0103 -p1
%patch0104 -p1
%patch0105 -p1
%patch0106 -p1
%patch0107 -p1
%patch0108 -p1
%patch0109 -p1
%patch0110 -p1
%patch0111 -p1
%patch0112 -p1
%patch0113 -p1
%patch0114 -p1
%patch0115 -p1
%patch0116 -p1
%patch0117 -p1
%patch0118 -p1
%patch0119 -p1
%patch0120 -p1
%patch0121 -p1
%patch0122 -p1
%patch0123 -p1
%patch0124 -p1
%patch0125 -p1
%patch0126 -p1
%patch0127 -p1
%patch0128 -p1
%patch0129 -p1
%patch0130 -p1
%patch0131 -p1
%patch0132 -p1
%patch0133 -p1
%patch0134 -p1
%patch0135 -p1
%patch0136 -p1
%patch0137 -p1
%patch0138 -p1
%patch0139 -p1
%patch0140 -p1
%patch0141 -p1
%patch0142 -p1
%patch0143 -p1
%patch0144 -p1
%patch0145 -p1
%patch0146 -p1
%patch0147 -p1
%patch0148 -p1
%patch0149 -p1
%patch0150 -p1
%patch0151 -p1
%patch0152 -p1
%patch0153 -p1
%patch0154 -p1
%patch0155 -p1
%patch0156 -p1
%patch0157 -p1
%patch0158 -p1
%patch0159 -p1
%patch0160 -p1
%patch0161 -p1
%patch0162 -p1
%patch0163 -p1
%patch0164 -p1
%patch0165 -p1
%patch0166 -p1
%patch0167 -p1
%patch0168 -p1
%patch0169 -p1
%patch0170 -p1
%patch0171 -p1
%patch0172 -p1
%patch0173 -p1
%patch0174 -p1
%patch0175 -p1
%patch0176 -p1
%patch0177 -p1
%patch0178 -p1
%patch0179 -p1
%patch0180 -p1
%patch0181 -p1
%patch0182 -p1
%patch0183 -p1
%patch0184 -p1
%patch0185 -p1
%patch0186 -p1
%patch0187 -p1
%patch0188 -p1
%patch0189 -p1
%patch0190 -p1
%patch0191 -p1
%patch0192 -p1
%patch0193 -p1
%patch0194 -p1
%patch0195 -p1
%patch0196 -p1
%patch0197 -p1
%patch0198 -p1
%patch0199 -p1
%patch0200 -p1
%patch0201 -p1
%patch0202 -p1
%patch0203 -p1
%patch0204 -p1
%patch0205 -p1
%patch0206 -p1
%patch0207 -p1
%patch0208 -p1
%patch0209 -p1
%patch0210 -p1
%patch0211 -p1
%patch0212 -p1
%patch0213 -p1
%patch0214 -p1
%patch0215 -p1
%patch0216 -p1
%patch0217 -p1
%patch0218 -p1
%patch0219 -p1
%patch0220 -p1
%patch0221 -p1
%patch0222 -p1
%patch0223 -p1
%patch0224 -p1
%patch0225 -p1
%patch0226 -p1
%patch0227 -p1
%patch0228 -p1
%patch0229 -p1
%patch0230 -p1
%patch0231 -p1
%patch0232 -p1
%patch0233 -p1
%patch0234 -p1
%patch0235 -p1
%patch0236 -p1
%patch0237 -p1
%patch0238 -p1
%patch0239 -p1
%patch0240 -p1
%patch0241 -p1
%patch0242 -p1
%patch0243 -p1
%patch0244 -p1
%patch0245 -p1
%patch0246 -p1
%patch0247 -p1
%patch0248 -p1
%patch0249 -p1
%patch0250 -p1
%patch0251 -p1
%patch0252 -p1
%patch0253 -p1
%patch0254 -p1
# glibc-2_26-fixes.patch
%patch0255 -p1

%build
CFLAGS=`echo $CFLAGS | sed 's|-fno-omit-frame-pointer||g'` ; export CFLAGS ;
CFLAGS=`echo $CFLAGS | sed 's|-O2|-O|g'` ; export CFLAGS ;

CONFIGURE_FLAGS=" \
    --prefix=/usr \
    --sysconfdir=%_sysconfdir \
    --interp-prefix=/usr/share/qemu/qemu-i386 \
    --enable-linux-user \
    --target-list=$((for target in %{target_list}; do echo -n ${target}-linux-user,; done) | sed -e 's/,$//') \
    --disable-blobs \
    --disable-cocoa \
    --disable-curses \
    --disable-fdt \
    --disable-gtk \
    --disable-guest-agent \
    --disable-linux-aio \
    --disable-sdl \
    --disable-smartcard \
    --disable-stack-protector \
    --disable-strip \
    --disable-system \
    --disable-vnc \
    --disable-vte \
    --disable-werror \
"
#    --disable-tools \
#    --extra-cflags=\"%{optflags}\" \

for mode in static dynamic; do
    mkdir build-$mode
    cd build-$mode
    if [ $mode = static ]; then
        ../configure --static $CONFIGURE_FLAGS
    else
        ../configure $CONFIGURE_FLAGS
    fi
    make %{?jobs:-j%jobs}
    cd ..
done

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/sbin
install -m 755 %{SOURCE1} $RPM_BUILD_ROOT/usr/sbin

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

%files
%defattr(-,root,root,-)
%{_bindir}/qemu-*-dynamic
%{_sbindir}/qemu-binfmt-conf.sh

%package common
Summary:  Universal CPU emulator (common utilities)
Group:      System/Emulators/PC

%description common
This package provides common qemu utilities.

%files common
%defattr(-,root,root,-)
%{_bindir}/qemu-img
%{_bindir}/qemu-io
%{_bindir}/qemu-nbd
%{_bindir}/ivshmem-client
%{_bindir}/ivshmem-server
%{_bindir}/qemu-aarch64-binfmt
%{_bindir}/qemu-arm-binfmt
%{_bindir}/qemu-mipsel-binfmt

%package static
Summary:  Universal CPU emulator (static userspace emulators)
Group:      System/Emulators/PC
Requires: %{name}-common = %{version}

%description static
This package provides static builds of userspace CPU emulators.

%files static
%defattr(-,root,root,-)
%{_bindir}/qemu-*-static
