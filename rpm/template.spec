Name:           ros-lunar-trac-ik-python
Version:        1.4.9
Release:        1%{?dist}
Summary:        ROS trac_ik_python package

Group:          Development/Libraries
License:        BSD
Source0:        %{name}-%{version}.tar.gz

Requires:       ros-lunar-rospy
Requires:       ros-lunar-tf
Requires:       ros-lunar-tf-conversions
Requires:       ros-lunar-trac-ik-lib
Requires:       swig
BuildRequires:  ros-lunar-catkin
BuildRequires:  ros-lunar-rospy
BuildRequires:  ros-lunar-tf-conversions
BuildRequires:  ros-lunar-trac-ik-lib
BuildRequires:  swig

%description
The trac_ik_python package contains a python wrapper using SWIG for trac_ik_lib

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
* Sat Jan 20 2018 Sam Pfeiffer <Sammy.Pfeiffer@student.uts.edu.au> - 1.4.9-1
- Autogenerated by Bloom

* Thu Jan 11 2018 Sam Pfeiffer <Sammy.Pfeiffer@student.uts.edu.au> - 1.4.9-0
- Autogenerated by Bloom

