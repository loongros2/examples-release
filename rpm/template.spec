%bcond_without tests
%bcond_without weak_deps

%global __os_install_post %(echo '%{__os_install_post}' | sed -e 's!/usr/lib[^[:space:]]*/brp-python-bytecompile[[:space:]].*$!!g')
%global __provides_exclude_from ^/opt/ros/iron/.*$
%global __requires_exclude_from ^/opt/ros/iron/.*$

Name:           ros-iron-examples-rclpy-minimal-action-client
Version:        0.18.2
Release:        1%{?dist}%{?release_suffix}
Summary:        ROS examples_rclpy_minimal_action_client package

License:        Apache License 2.0
Source0:        %{name}-%{version}.tar.gz

Requires:       ros-iron-action-msgs
Requires:       ros-iron-example-interfaces
Requires:       ros-iron-rclpy
Requires:       ros-iron-ros-workspace
BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  ros-iron-ros-workspace
Provides:       %{name}-devel = %{version}-%{release}
Provides:       %{name}-doc = %{version}-%{release}
Provides:       %{name}-runtime = %{version}-%{release}

%if 0%{?with_tests}
BuildRequires:  python%{python3_pkgversion}-pytest
BuildRequires:  ros-iron-ament-copyright
BuildRequires:  ros-iron-ament-flake8
BuildRequires:  ros-iron-ament-pep257
%endif

%description
Examples of minimal action clients using rclpy.

%prep
%autosetup -p1

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree and source it.  It will set things like
# CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/iron/setup.sh" ]; then . "/opt/ros/iron/setup.sh"; fi
%py3_build

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree and source it.  It will set things like
# CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/iron/setup.sh" ]; then . "/opt/ros/iron/setup.sh"; fi
%py3_install -- --prefix "/opt/ros/iron"

%if 0%{?with_tests}
%check
# Look for a directory with a name indicating that it contains tests
TEST_TARGET=$(ls -d * | grep -m1 "\(test\|tests\)" ||:)
if [ -n "$TEST_TARGET" ] && %__python3 -m pytest --version; then
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree and source it.  It will set things like
# CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/iron/setup.sh" ]; then . "/opt/ros/iron/setup.sh"; fi
%__python3 -m pytest $TEST_TARGET || echo "RPM TESTS FAILED"
else echo "RPM TESTS SKIPPED"; fi
%endif

%files
/opt/ros/iron

%changelog
* Fri Nov 08 2024 Aditya Pande <aditya.pande@openrobotics.org> - 0.18.2-1
- Autogenerated by Bloom

* Thu Jul 11 2024 Aditya Pande <aditya.pande@openrobotics.org> - 0.18.1-1
- Autogenerated by Bloom

* Thu Apr 20 2023 Aditya Pande <aditya.pande@openrobotics.org> - 0.18.0-2
- Autogenerated by Bloom

* Tue Apr 11 2023 Aditya Pande <aditya.pande@openrobotics.org> - 0.18.0-1
- Autogenerated by Bloom

* Tue Mar 21 2023 Aditya Pande <aditya.pande@openrobotics.org> - 0.17.1-3
- Autogenerated by Bloom

