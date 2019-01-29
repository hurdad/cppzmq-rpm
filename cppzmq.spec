Name:           cppzmq-devel
Version:        %{VERSION}
Release:        1
Summary:        A C++ binding for 0MQ
License:        GPL-3.0+ and LGPL-3.0+
Group:          Development/Libraries/C and C++
Url:            https://github.com/zeromq/cppzmq
Source:         cppzmq-%{version}.tar.gz
Requires:       zeromq-devel
BuildRequires:	cmake3
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
A simple C++ binding for 0MQ

%prep
%setup -q -n cppzmq-%{version}

%build

%install
install -Dpm 644 zmq.hpp %{buildroot}%{_includedir}/zmq.hpp
install -Dpm 644 zmq.hpp %{buildroot}%{_includedir}/zmq_addons.hpp

%files
%defattr(-,root,root)
%doc LICENSE README.md
%{_includedir}/zmq.hpp
%{_includedir}/zmq_addons.hpp

%changelog

