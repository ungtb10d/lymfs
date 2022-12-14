    _complete="${PWD}/LOGS/${FUNCNAME}.completed"
    _logfile="${PWD}/LOGS/${FUNCNAME}.log"
    [ -e ${_complete} ] && { msg "${FUNCNAME}: SKIPPING";return 0; } || msg "${FUNCNAME}: Building"
    > ${_logfile}
    msg "Creating files and symlinks: "
    build "+ ln -sv /tools/bin/{bash,cat,dd,echo,ln,pwd,rm,stty} /bin" "ln -sv /tools/bin/{bash,cat,dd,echo,ln,pwd,rm,stty} /bin" ${_logfile}
    build "+ ln -sv /tools/bin/{env,install,perl} /usr/bin" "ln -sv /tools/bin/{env,install,perl} /usr/bin" ${_logfile}
    build "+ ln -sv /tools/lib/libgcc_s.so{,.1} /usr/lib" "ln -sv /tools/lib/libgcc_s.so{,.1} /usr/lib" ${_logfile}
    build "+ ln -sv /tools/lib/libstdc++.{a,so{,.6}} /usr/lib" "ln -sv /tools/lib/libstdc++.{a,so{,.6}} /usr/lib" ${_logfile}
    for lib in blkid lzma mount uuid
    do
        build "+ ln -sv /tools/lib/lib$lib.so* /usr/lib" "ln -sv /tools/lib/lib$lib.so* /usr/lib" ${_logfile}
    done
    build "+ ln -svf /tools/include/blkid    /usr/include" "ln -svf /tools/include/blkid    /usr/include" ${_logfile}
    build "+ ln -svf /tools/include/libmount /usr/include" "ln -svf /tools/include/libmount /usr/include" ${_logfile}
    build "+ ln -svf /tools/include/uuid     /usr/include" "ln -svf /tools/include/uuid     /usr/include" ${_logfile}
    build "+ install -vdm755 /usr/lib/pkgconfig" "install -vdm755 /usr/lib/pkgconfig" ${_logfile}
    for pc in blkid mount uuid
    do
        build "+ sed 's@tools@usr@g' /tools/lib/pkgconfig/${pc}.pc > /usr/lib/pkgconfig/${pc}.pc" "sed 's@tools@usr@g' /tools/lib/pkgconfig/${pc}.pc > /usr/lib/pkgconfig/${pc}.pc" ${_logfile}
    done
    build "+ ln -sv bash /bin/sh" "ln -sv bash /bin/sh" ${_logfile}

    build "+ ln -sv /proc/self/mounts /etc/mtab" "ln -sv /proc/self/mounts /etc/mtab" "${_logfile}"

    msg_line "Creating /etc/passwd: "
    cat > /etc/passwd << "EOF"
root:x:0:0:root:/root:/bin/bash
bin:x:1:1:bin:/dev/null:/bin/false
daemon:x:6:6:Daemon User:/dev/null:/bin/false
messagebus:x:18:18:D-Bus Message Daemon User:/var/run/dbus:/bin/false
systemd-bus-proxy:x:72:72:systemd Bus Proxy:/:/bin/false
systemd-journal-gateway:x:73:73:systemd Journal Gateway:/:/bin/false
systemd-journal-remote:x:74:74:systemd Journal Remote:/:/bin/false
systemd-journal-upload:x:75:75:systemd Journal Upload:/:/bin/false
systemd-network:x:76:76:systemd Network Management:/:/bin/false
systemd-resolve:x:77:77:systemd Resolver:/:/bin/false
systemd-timesync:x:78:78:systemd Time Synchronization:/:/bin/false
systemd-coredump:x:79:79:systemd Core Dumper:/:/bin/false
nobody:x:99:99:Unprivileged User:/dev/null:/bin/false
EOF
    msg_success

    msg_line "Creating /etc/group: "
cat > /etc/group << "EOF"
root:x:0:
bin:x:1:daemon
sys:x:2:
kmem:x:3:
tape:x:4:
tty:x:5:
daemon:x:6:
floppy:x:7:
disk:x:8:
lp:x:9:
dialout:x:10:
audio:x:11:
video:x:12:
utmp:x:13:
usb:x:14:
cdrom:x:15:
adm:x:16:
messagebus:x:18:
systemd-journal:x:23:
input:x:24:
mail:x:34:
kvm:x:61:
systemd-bus-proxy:x:72:
systemd-journal-gateway:x:73:
systemd-journal-remote:x:74:
systemd-journal-upload:x:75:
systemd-network:x:76:
systemd-resolve:x:77:
systemd-timesync:x:78:
systemd-coredump:x:79:
nogroup:x:99:
users:x:999:
EOF
    msg_success

    build "+ touch /var/log/{btmp,lastlog,faillog,wtmp}" "touch /var/log/{btmp,lastlog,faillog,wtmp}" ${_logfile}

    build "+ chgrp -v utmp /var/log/lastlog" "chgrp -v utmp /var/log/lastlog" ${_logfile}
    build "+ chmod -v 664 /var/log/lastlog" "chmod -v 664 /var/log/lastlog" ${_logfile}
    build "+ chmod -v 600 /var/log/btmp" "chmod -v 600 /var/log/btmp" ${_logfile}
    touch ${_complete}
