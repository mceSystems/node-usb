{
  'variables': {
    'use_udev%': 1,
  },
  'targets': [
    {
      # Based on https://chromium.googlesource.com/chromium/src/+/master/third_party/libusb/libusb.gyp
      'target_name': 'libusb',
      'type': 'static_library',
      'sources': [
        'libusb_config/config.h',
        'libusb.mpd/libusb/core.c',
        'libusb.mpd/libusb/descriptor.c',
        'libusb.mpd/libusb/hotplug.c',
        'libusb.mpd/libusb/hotplug.h',
        'libusb.mpd/libusb/io.c',
        'libusb.mpd/libusb/libusb.h',
        'libusb.mpd/libusb/libusbi.h',
        'libusb.mpd/libusb/strerror.c',
        'libusb.mpd/libusb/sync.c',
        'libusb.mpd/libusb/version.h',
        'libusb.mpd/libusb/version_nano.h',
      ],
      'include_dirs': [
        'libusb_config',
        'libusb.mpd/libusb',
        'libusb.mpd/libusb/os',
      ],
      'direct_dependent_settings': {
        'include_dirs': [
          'libusb.mpd/libusb',
        ],
      },
      'defines': [
        'ENABLE_LOGGING=1',
      ],
      'cflags': [
        '-w',
      ],
      'conditions': [
        [ 'OS == "linux" or OS == "android" or OS == "mac"', {
          'sources': [
            'libusb.mpd/libusb/os/poll_posix.c',
            'libusb.mpd/libusb/os/poll_posix.h',
            'libusb.mpd/libusb/os/threads_posix.c',
            'libusb.mpd/libusb/os/threads_posix.h',
          ],
          'defines': [
            'DEFAULT_VISIBILITY=',
            'HAVE_GETTIMEOFDAY=1',
            'HAVE_POLL_H=1',
            'HAVE_SYS_TIME_H=1',
            'LIBUSB_DESCRIBE="1.0.17"',
            'POLL_NFDS_TYPE=nfds_t',
            'THREADS_POSIX=1',
          ],
        }],
        [ 'OS == "linux" or OS == "android"', {
          'sources': [
            'libusb.mpd/libusb/os/linux_usbfs.c',
            'libusb.mpd/libusb/os/linux_usbfs.h',
          ],
          'defines': [
            'OS_LINUX=1',
            '_GNU_SOURCE=1',
            'USBI_TIMERFD_AVAILABLE=1',
          ],
        }],
        [ 'OS == "linux" and use_udev == 1 or OS == "android"', {
          'sources': [
            'libusb.mpd/libusb/os/linux_udev.c',
          ],
          'defines': [
            'HAVE_LIBUDEV=1',
            'USE_UDEV=1',
          ],
          'direct_dependent_settings': {
            'libraries': [
              '-ludev',
            ]
          }
        }],
        [ 'OS == "linux" and use_udev == 0', {
          'sources': [
            'libusb.mpd/libusb/os/linux_netlink.c',
          ],
          'defines': [
            'HAVE_LINUX_NETLINK_H',
          ],
          'conditions': [
            ['clang==1', {
              'cflags': [
                '-Wno-pointer-sign',
              ]
            }]
          ],
        }],
        [ 'OS == "mac"', {
          'sources': [
            'libusb.mpd/libusb/os/darwin_usb.c',
            'libusb.mpd/libusb/os/darwin_usb.h',
          ],
          'defines': [
            'OS_DARWIN=1',
          ],
        }],
        [ 'OS == "win"', {
          'sources': [
            'libusb.mpd/libusb/os/poll_windows.c',
            'libusb.mpd/libusb/os/poll_windows.h',
            'libusb.mpd/libusb/os/threads_windows.c',
            'libusb.mpd/libusb/os/threads_windows.h',
            'libusb.mpd/libusb/os/windows_common.h',
            'libusb.mpd/libusb/os/windows_usb.c',
            'libusb.mpd/libusb/os/windows_usb.h',
            'libusb.mpd/msvc/config.h',
            'libusb.mpd/msvc/inttypes.h',
            'libusb.mpd/msvc/stdint.h',
          ],
          'defines': [
            'HAVE_STRUCT_TIMESPEC',
          ],
          'include_dirs!': [
            'libusb_config',
          ],
          'include_dirs': [
            'libusb.mpd/msvc',
          ],
          'msvs_disabled_warnings': [ 4267 ],
        }],
      ],
    },
  ]
}
