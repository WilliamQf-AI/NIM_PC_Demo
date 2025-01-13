from conan import ConanFile
from conan.errors import ConanInvalidConfiguration
from conan.tools.cmake import CMake, CMakeToolchain, cmake_layout
from conan.tools.files import get, copy, collect_libs
from conan.tools.scm import Git
from conan.tools.build import check_min_cppstd
import os
import re


class NebaseConan(ConanFile):
    name = "nim_demo"
    author = "Dylan <2894220@gmail.com>"
    url = "https://github.com/netease-kit/NIM_PC_Demo.git"
    description = "nim_demo"
    settings = "os", "compiler", "build_type", "arch"
    options = {"shared": [True, False], "fPIC": [True, False]}
    default_options = {
        "shared": False,
        "fPIC": True,
        "nim:with_nrtc": True
    }
    generators = "CMakeDeps", "cmake_paths", "cmake_find_package", "cmake"
    exports_sources = "*", "!build"

    def requirements(self):
        self.requires("libjpeg/9c")
        self.requires("openssl/3.3.2")
        self.requires("jsoncpp/1.9.5")
        self.requires("libuv/1.49.0")
        self.requires("libyuv/1892")
        self.requires("sqlite3/3.36.0")
        self.requires("tinyxml/2.6.2")
        self.requires("nim/10.7.1@yunxin/stable")
        self.requires("nertc/4.1.1@yunxin/stable")
        self.requires("libcef/3.2623.1401@yunxin/stable")
        self.requires("ne_live_player/1.6.9@yunxin/stable")
        self.requires("image_ole/4.2.0@yunxin/stable")
        self.requires("ne_transfer/0.1.0@yunxin/stable")

    def imports(self):
        script_path = os.path.split(os.path.realpath(__file__))[0]
        binary_path = os.path.join(script_path, "bin")
        self.copy("*.*", binary_path, "bin", "libcef")
        self.copy("*.*", binary_path, "bin", "nim")
        self.copy("*.*", binary_path, "bin", "nertc")
        self.copy("*.*", binary_path, "bin", "ne_live_player")
        self.copy("*.*", binary_path, "bin", "image_ole")
        self.copy("*.*", binary_path, "bin", "ne_transfer")
