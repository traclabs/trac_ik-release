%bcond_without weak_deps

%global __os_install_post %(echo '%{__os_install_post}' | sed -e 's!/usr/lib[^[:space:]]*/brp-python-bytecompile[[:space:]].*$!!g')
%global __provides_exclude_from ^/opt/ros/noetic/.*$
%global __requires_exclude_from ^/opt/ros/noetic/.*$

Name:           ros-noetic-trac-ik-examples
Version:        1.6.1
Release:        2%{?dist}%{?release_suffix}
Summary:        ROS trac_ik_examples package

License:        BSD
Source0:        %{name}-%{version}.tar.gz

Requires:       boost-devel
Requires:       boost-python3-devel
Requires:       orocos-kdl
Requires:       ros-noetic-trac-ik-lib
Requires:       ros-noetic-xacro
BuildRequires:  boost-devel
BuildRequires:  boost-python3-devel
BuildRequires:  orocos-kdl-devel
BuildRequires:  ros-noetic-catkin
BuildRequires:  ros-noetic-trac-ik-lib
Provides:       %{name}-devel = %{version}-%{release}
Provides:       %{name}-doc = %{version}-%{release}
Provides:       %{name}-runtime = %{version}-%{release}

%description
This package contains the source code for testing and comparing trac_ik

%prep
%autosetup

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/noetic/setup.sh" ]; then . "/opt/ros/noetic/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake3 \
    -UINCLUDE_INSTALL_DIR \
    -ULIB_INSTALL_DIR \
    -USYSCONF_INSTALL_DIR \
    -USHARE_INSTALL_PREFIX \
    -ULIB_SUFFIX \
    -DCMAKE_INSTALL_PREFIX="/opt/ros/noetic" \
    -DCMAKE_PREFIX_PATH="/opt/ros/noetic" \
    -DSETUPTOOLS_DEB_LAYOUT=OFF \
    -DCATKIN_BUILD_BINARY_PACKAGE="1" \
    ..

%make_build

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/noetic/setup.sh" ]; then . "/opt/ros/noetic/setup.sh"; fi
%make_install -C obj-%{_target_platform}

%files
/opt/ros/noetic

%changelog
* Fri Mar 05 2021 TRACLabs Robotics <robotics@traclabs.com> - 1.6.1-2
- Autogenerated by Bloom

* Fri Mar 05 2021 TRACLabs Robotics <robotics@traclabs.com> - 1.6.1-1
- Autogenerated by Bloom

