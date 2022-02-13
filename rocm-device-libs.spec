# bitcode has no debuginfo
%global debug_package %{nil}

%global upstreamname ROCm-Device-Libs

Name:           rocm-device-libs
Version:        5.0.0
Release:        1%{?dist}
Summary:        AMD ROCm LLVM bit code libraries

Url:            https://github.com/RadeonOpenCompute/ROCm-Device-Libs
License:        NCSA
Source0:        https://github.com/RadeonOpenCompute/%{upstreamname}/archive/refs/tags/rocm-%{version}.tar.gz#/%{upstreamname}-%{version}.tar.gz
# Upstream is working on a solution:
Patch0:         0001-Use-FHS-compliant-install.patch

BuildRequires:  cmake
BuildRequires:  clang-devel
BuildRequires:  llvm-devel
BuildRequires:  zlib-devel

#Only the following architectures are supported:
ExclusiveArch:  x86_64 aarch64

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
%cmake . -DCMAKE_BUILD_TYPE="RELEASE"
%cmake_build

%install
%cmake_install

%files
%license LICENSE
%doc README.md doc/*.md
%{_libdir}/cmake/AMDDeviceLibs
%{_libdir}/amdgcn

%changelog
* Fri Feb 11 2022 Jeremy Newton <alexjnewt at hotmail dot com> - 5.0.0-1
- Update to 5.0.0

* Mon Jan 17 2022 Jeremy Newton <alexjnewt at hotmail dot com> - 4.5.2-1
- Initial package
