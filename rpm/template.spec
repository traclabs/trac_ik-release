Name:           ros-lunar-trac-ik-kinematics-plugin
Version:        1.4.7
Release:        0%{?dist}
Summary:        ROS trac_ik_kinematics_plugin package

Group:          Development/Libraries
License:        BSD
Source0:        %{name}-%{version}.tar.gz

Requires:       ros-lunar-moveit-core
Requires:       ros-lunar-pluginlib
Requires:       ros-lunar-roscpp
Requires:       ros-lunar-tf-conversions
Requires:       ros-lunar-trac-ik-lib
BuildRequires:  ros-lunar-catkin
BuildRequires:  ros-lunar-moveit-core
BuildRequires:  ros-lunar-pluginlib
BuildRequires:  ros-lunar-roscpp
BuildRequires:  ros-lunar-tf-conversions
BuildRequires:  ros-lunar-trac-ik-lib

%description
A MoveIt! Kinematics plugin using TRAC-IK

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/lunar/setup.sh" ]; then . "/opt/ros/lunar/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_LIBDIR="lib" \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/lunar" \
        -DCMAKE_PREFIX_PATH="/opt/ros/lunar" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/lunar/setup.sh" ]; then . "/opt/ros/lunar/setup.sh"; fi
cd obj-%{_target_platform}
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/lunar

%changelog
* Tue Dec 26 2017 Patrick Beeson <pbeeson@traclabs.com> - 1.4.7-0
- Autogenerated by Bloom

