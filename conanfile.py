#!/usr/bin/env python
# -*- coding: utf-8 -*-

from conans import python_requires


base = python_requires("boost_base/1.69.0@bincrafters/testing")

class BoostStacktraceConan(base.BoostBaseConan):
    name = "boost_stacktrace"
    url = "https://github.com/bincrafters/conan-boost_stacktrace"
    lib_short_names = ["stacktrace"]
    options = {"shared": [True, False]}
    default_options = "shared=False"
    b2_requires = [
        "boost_array",
        "boost_config",
        "boost_container_hash",
        "boost_core",
        "boost_static_assert",
        "boost_type_traits",
        "boost_winapi"
    ]

    def package_info_additional(self):
        self.cpp_info.defines.append("BOOST_STACKTRACE_GNU_SOURCE_NOT_REQUIRED=1")
