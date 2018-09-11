Name:           ros-melodic-pr2-controller-interface
Version:        1.8.18
Release:        0%{?dist}
Summary:        ROS pr2_controller_interface package

Group:          Development/Libraries
License:        BSD
URL:            http://ros.org/wiki/pr2_controller_interface
Source0:        %{name}-%{version}.tar.gz

Requires:       ros-melodic-controller-interface
Requires:       ros-melodic-pr2-mechanism-model
Requires:       ros-melodic-roscpp
BuildRequires:  ros-melodic-catkin
BuildRequires:  ros-melodic-controller-interface
BuildRequires:  ros-melodic-pr2-mechanism-model
BuildRequires:  ros-melodic-roscpp

%description
This package specifies the interface to a realtime controller. A controller that
implements this interface can be executed by the controller manager in the real
time control loop. The package basically contains the C++ controller base class
that all controllers need to inherit from.

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/melodic/setup.sh" ]; then . "/opt/ros/melodic/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_LIBDIR="lib" \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/melodic" \
        -DCMAKE_PREFIX_PATH="/opt/ros/melodic" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/melodic/setup.sh" ]; then . "/opt/ros/melodic/setup.sh"; fi
cd obj-%{_target_platform}
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/melodic

%changelog
* Tue Sep 11 2018 ROS Orphaned Package Maintainers <ros-orphaned-packages@googlegroups.com> - 1.8.18-0
- Autogenerated by Bloom

