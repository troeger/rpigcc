Name:rpigcc		
Version:1.0	
Release:0
Summary:RaspBerryPI cross compiler for Linux.
Group:Development/Building
License:GPL
URL:https://github.com/troeger/rpigcc	
Source0:https://github.com/raspberrypi/tools/archive/master.zip
AutoReqProv: no

%global __os_install_post %{nil}

%description
This package installs the RaspBerryPI cross compiler for Linux,
originally available at https://github.com/raspberrypi/tools.

%prep
%setup -q -c

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/lib/rpigcc/
cp -rp %{_builddir}/tools-master/arm-bcm2708/gcc-linaro-arm-linux-gnueabihf-raspbian-x64/* %{buildroot}/usr/lib/rpigcc/
rm -rf %{buildroot}/usr/lib/rpigcc/share/doc
mkdir -p %{buildroot}%{_bindir}/
ln -s /usr/lib/rpigcc/bin/arm-linux-gnueabihf-addr2line  %{buildroot}%{_bindir}/
ln -s /usr/lib/rpigcc/bin/arm-linux-gnueabihf-ar %{buildroot}%{_bindir}/
ln -s /usr/lib/rpigcc/bin/arm-linux-gnueabihf-as %{buildroot}%{_bindir}/
ln -s /usr/lib/rpigcc/bin/arm-linux-gnueabihf-c++ %{buildroot}%{_bindir}/
ln -s /usr/lib/rpigcc/bin/arm-linux-gnueabihf-c++filt %{buildroot}%{_bindir}/
ln -s /usr/lib/rpigcc/bin/arm-linux-gnueabihf-cpp %{buildroot}%{_bindir}/
ln -s /usr/lib/rpigcc/bin/arm-linux-gnueabihf-ct-ng.config %{buildroot}%{_bindir}/
ln -s /usr/lib/rpigcc/bin/arm-linux-gnueabihf-dwp %{buildroot}%{_bindir}/
ln -s /usr/lib/rpigcc/bin/arm-linux-gnueabihf-elfedit %{buildroot}%{_bindir}/
ln -s /usr/lib/rpigcc/bin/arm-linux-gnueabihf-g++ %{buildroot}%{_bindir}/
ln -s /usr/lib/rpigcc/bin/arm-linux-gnueabihf-gcc %{buildroot}%{_bindir}/
ln -s /usr/lib/rpigcc/bin/arm-linux-gnueabihf-gcc-4.8.3 %{buildroot}%{_bindir}/
ln -s /usr/lib/rpigcc/bin/arm-linux-gnueabihf-gcc-ar %{buildroot}%{_bindir}/
ln -s /usr/lib/rpigcc/bin/arm-linux-gnueabihf-gcc-nm %{buildroot}%{_bindir}/
ln -s /usr/lib/rpigcc/bin/arm-linux-gnueabihf-gcc-ranlib %{buildroot}%{_bindir}/
ln -s /usr/lib/rpigcc/bin/arm-linux-gnueabihf-gcov %{buildroot}%{_bindir}/
ln -s /usr/lib/rpigcc/bin/arm-linux-gnueabihf-gdb %{buildroot}%{_bindir}/
ln -s /usr/lib/rpigcc/bin/arm-linux-gnueabihf-gfortran %{buildroot}%{_bindir}/
ln -s /usr/lib/rpigcc/bin/arm-linux-gnueabihf-gprof %{buildroot}%{_bindir}/
ln -s /usr/lib/rpigcc/bin/arm-linux-gnueabihf-ld %{buildroot}%{_bindir}/
ln -s /usr/lib/rpigcc/bin/arm-linux-gnueabihf-ld.bfd %{buildroot}%{_bindir}/
ln -s /usr/lib/rpigcc/bin/arm-linux-gnueabihf-ld.gold %{buildroot}%{_bindir}/
ln -s /usr/lib/rpigcc/bin/arm-linux-gnueabihf-ldd %{buildroot}%{_bindir}/
ln -s /usr/lib/rpigcc/bin/arm-linux-gnueabihf-nm %{buildroot}%{_bindir}/
ln -s /usr/lib/rpigcc/bin/arm-linux-gnueabihf-objcopy %{buildroot}%{_bindir}/
ln -s /usr/lib/rpigcc/bin/arm-linux-gnueabihf-objdump %{buildroot}%{_bindir}/
ln -s /usr/lib/rpigcc/bin/arm-linux-gnueabihf-pkg-config %{buildroot}%{_bindir}/
ln -s /usr/lib/rpigcc/bin/arm-linux-gnueabihf-pkg-config-real %{buildroot}%{_bindir}/
ln -s /usr/lib/rpigcc/bin/arm-linux-gnueabihf-ranlib %{buildroot}%{_bindir}/
ln -s /usr/lib/rpigcc/bin/arm-linux-gnueabihf-readelf %{buildroot}%{_bindir}/
ln -s /usr/lib/rpigcc/bin/arm-linux-gnueabihf-size %{buildroot}%{_bindir}/
ln -s /usr/lib/rpigcc/bin/arm-linux-gnueabihf-strings %{buildroot}%{_bindir}/
ln -s /usr/lib/rpigcc/bin/arm-linux-gnueabihf-strip %{buildroot}%{_bindir}/

%files
/usr/lib/rpigcc/
%{_bindir}/*

