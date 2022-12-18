# bitcode has no debuginfo
%global debug_package %{nil}

%global llvm_maj_ver 14
%global upstreamname ROCm-Device-Libs

# This might be needed because EL9 llvm is built with clang:
%if 0%{?epel} > 8
%global toolchain clang
%endif

Name:           rocm-device-libs
Version:        5.2.3
Release:        1%{?dist}
Summary:        AMD ROCm LLVM bit code libraries

Url:            https://github.com/RadeonOpenCompute/ROCm-Device-Libs
License:        NCSA
Source0:        https://github.com/RadeonOpenCompute/%{upstreamname}/archive/refs/tags/rocm-%{version}.tar.gz#/%{upstreamname}-%{version}.tar.gz
# Upstream is working on a solution, patch is adapted from debian:
#https://salsa.debian.org/rocm-team/rocm-device-libs/-/blob/master/debian/patches/cmake-amdgcn-bitcode.patch
Patch0:         0001-Use-FHS-compliant-install.patch

BuildRequires:  cmake
BuildRequires:  clang-devel
BuildRequires:  clang(major) = %{llvm_maj_ver}
BuildRequires:  llvm-devel(major) = %{llvm_maj_ver}
BuildRequires:  ncurses-devel
BuildRequires:  zlib-devel
Requires:       clang(major) = %{llvm_maj_ver}

#Only the following architectures are useful for ROCm packages:
ExclusiveArch:  x86_64 aarch64 ppc64le

%description
This package contains a set of AMD specific device-side language runtime
libraries in the form of bit code. Specifically:
 - Open Compute library controls
 - Open Compute Math library
 - Open Compute Kernel library
 - OpenCL built-in library
 - HIP built-in library
 - Heterogeneous Compute built-in library

%prep
%autosetup -p1 -n %{upstreamname}-rocm-%{version}

%build
%cmake -DCMAKE_BUILD_TYPE="RELEASE"
%cmake_build

%install
%cmake_install

%files
%license LICENSE.TXT
%doc README.md doc/*.md
# No need to install this twice:
%exclude %{_docdir}/ROCm-Device-Libs/rocm-device-libs/LICENSE.TXT
%{_libdir}/cmake/AMDDeviceLibs
%{_libdir}/amdgcn

%changelog
* Thu Nov 24 2022 Jeremy Newton <alexjnewt at hotmail dot com> - 5.2.3-1
- Update to ROCm version 5.2.3
- Synchronize with spec file from fedora 36

* Thu May 26 2022 Jeremy Newton <alexjnewt at hotmail dot com> - 5.0.2-1
- Initial EPEL8 package
