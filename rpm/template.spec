Name:           ros-indigo-trac-ik-kinematics-plugin
Version:        1.4.9
Release:        1%{?dist}
Summary:        ROS trac_ik_kinematics_plugin package

Group:          Development/Libraries
License:        BSD
Source0:        %{name}-%{version}.tar.gz

Requires:       ros-indigo-moveit-core
Requires:       ros-indigo-pluginlib
Requires:       ros-indigo-roscpp
Requires:       ros-indigo-tf-conversions
Requires:       ros-indigo-trac-ik-lib
BuildRequires:  ros-indigo-catkin
BuildRequires:  ros-indigo-moveit-core
BuildRequires:  ros-indigo-pluginlib
BuildRequires:  ros-indigo-roscpp
BuildRequires:  ros-indigo-tf-conversions
BuildRequires:  ros-indigo-trac-ik-lib

%description
A MoveIt! Kinematics plugin using TRAC-IK

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/indigo/setup.sh" ]; then . "/opt/ros/indigo/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_LIBDIR="lib" \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/indigo" \
        -DCMAKE_PREFIX_PATH="/opt/ros/indigo" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/indigo/setup.sh" ]; then . "/opt/ros/indigo/setup.sh"; fi
cd obj-%{_target_platform}
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/indigo

%changelog
* Sat Jan 20 2018 Patrick Beeson <pbeeson@traclabs.com> - 1.4.9-1
- Autogenerated by Bloom

* Thu Jan 11 2018 Patrick Beeson <pbeeson@traclabs.com> - 1.4.9-0
- Autogenerated by Bloom

* Thu Dec 21 2017 Patrick Beeson <pbeeson@traclabs.com> - 1.4.7-0
- Autogenerated by Bloom

* Wed Dec 21 2016 Patrick Beeson <pbeeson@traclabs.com> - 1.4.5-0
- Autogenerated by Bloom

* Tue Jun 14 2016 Patrick Beeson <pbeeson@traclabs.com> - 1.4.3-0
- Autogenerated by Bloom

* Tue Jun 14 2016 Patrick Beeson <pbeeson@traclabs.com> - 1.4.2-0
- Autogenerated by Bloom

