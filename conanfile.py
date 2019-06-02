#!/usr/bin/env python
# -*- coding: utf-8 -*-

from conans import python_requires


base = python_requires("boost_base/2.0.0@bincrafters/testing")


class BoostStacktraceConan(base.BoostBaseConan):
    name = "boost_stacktrace"
    version = "1.70.0"

    def package_info(self):
        super(BoostStacktraceConan, self).package_info()
        self.cpp_info.defines.append(
            "BOOST_STACKTRACE_GNU_SOURCE_NOT_REQUIRED=1")
