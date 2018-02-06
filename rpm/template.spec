Name:           ros-lunar-trac-ik-lib
Version:        1.4.11
Release:        0%{?dist}
Summary:        ROS trac_ik_lib package

Group:          Development/Libraries
License:        BSD
Source0:        %{name}-%{version}.tar.gz

Requires:       NLopt
Requires:       NLopt-devel
Requires:       boost-devel
Requires:       ros-lunar-kdl-parser
Requires:       ros-lunar-roscpp
Requires:       ros-lunar-urdf
BuildRequires:  NLopt-devel
BuildRequires:  boost-devel
BuildRequires:  eigen3-devel
BuildRequires:  pkgconfig
BuildRequires:  ros-lunar-catkin
BuildRequires:  ros-lunar-cmake-modules
BuildRequires:  ros-lunar-kdl-parser
BuildRequires:  ros-lunar-roscpp
BuildRequires:  ros-lunar-urdf

%description
TRAC-IK is a faster, significantly more reliable drop-in replacement for KDL's
pseudoinverse Jacobian solver. The TRAC-IK library has a very similar API to
KDL's IK solver calls, except that the user passes a maximum time instead of a
maximum number of search iterations. Additionally, TRAC-IK allows for error
tolerances to be set independently for each Cartesian dimension
(x,y,z,roll,pitch.yaw).

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
* Tue Feb 06 2018 Patrick Beeson <pbeeson@traclabs.com> - 1.4.11-0
- Autogenerated by Bloom

* Sun Jan 21 2018 Patrick Beeson <pbeeson@traclabs.com> - 1.4.10-0
- Autogenerated by Bloom

* Sat Jan 20 2018 Patrick Beeson <pbeeson@traclabs.com> - 1.4.9-2
- Autogenerated by Bloom

* Sat Jan 20 2018 Patrick Beeson <pbeeson@traclabs.com> - 1.4.9-1
- Autogenerated by Bloom

* Thu Jan 11 2018 Patrick Beeson <pbeeson@traclabs.com> - 1.4.9-0
- Autogenerated by Bloom

* Tue Dec 26 2017 Patrick Beeson <pbeeson@traclabs.com> - 1.4.8-0
- Autogenerated by Bloom

* Tue Dec 26 2017 Patrick Beeson <pbeeson@traclabs.com> - 1.4.7-0
- Autogenerated by Bloom

