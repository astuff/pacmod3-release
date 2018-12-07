Name:           ros-melodic-pacmod3
Version:        1.2.1
Release:        0%{?dist}
Summary:        ROS pacmod3 package

Group:          Development/Libraries
License:        MIT
URL:            http://wiki.ros.org/pacmod3
Source0:        %{name}-%{version}.tar.gz

Requires:       ros-melodic-can-msgs
Requires:       ros-melodic-pacmod-msgs
Requires:       ros-melodic-roscpp
Requires:       ros-melodic-std-msgs
BuildRequires:  ros-melodic-can-msgs
BuildRequires:  ros-melodic-catkin
BuildRequires:  ros-melodic-pacmod-msgs
BuildRequires:  ros-melodic-roscpp
BuildRequires:  ros-melodic-std-msgs

%description
AutonomouStuff PACMod v3 Driver Package

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
* Fri Dec 07 2018 AutonomouStuff Software Team <software@autonomoustuff.com> - 1.2.1-0
- Autogenerated by Bloom

* Mon Nov 19 2018 AutonomouStuff Software Team <software@autonomoustuff.com> - 1.2.0-0
- Autogenerated by Bloom

* Fri Aug 31 2018 AutonomouStuff Software Team <software@autonomoustuff.com> - 1.1.1-0
- Autogenerated by Bloom

* Wed Aug 15 2018 AutonomouStuff Software Team <software@autonomoustuff.com> - 1.1.0-0
- Autogenerated by Bloom

