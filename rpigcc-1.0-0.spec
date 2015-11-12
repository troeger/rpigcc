Name:rpigcc		
Version:1.0	
Release:0
Summary:RaspBerryPI cross compiler for Linux.
Group:Development/Building
License:GPL
URL:https://github.com/troeger/rpigcc	
Source0:https://github.com/raspberrypi/tools/archive/master.zip

BuildRequires:
Requires:	

%description
This package installs the RaspBerryPI cross compiler for Linux,
originally available at https://github.com/raspberrypi/tools.

%prep
%setup -q


%build
%configure
make %{?_smp_mflags}


%install
make install DESTDIR=%{buildroot}


%files
%doc



%changelog

