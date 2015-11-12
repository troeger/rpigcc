rpm: rpigcc-1.0-0.spec
	mkdir -p ~/rpmbuild/{BUILD,BUILDROOT,RPMS,SOURCES,SPECS,SRPMS}
	wget -nc https://github.com/raspberrypi/tools/archive/master.zip
	cp -n master.zip ~/rpmbuild/SOURCES
	rpmbuild -ba rpigcc-1.0-0.spec
	cp ~/rpmbuild/RPMS/x86_64/rpigcc-1.0-0.x86_64.rpm .


