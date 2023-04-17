# Copyright 2013-2021 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *


class Spasm(Package):
    """SpaSM installation."""

    git      = "https://github.com/cbouilla/spasm.git"

    version('1.2', branch='master')

    # Overlap in functionality between gmp and mpir
    # All other dependencies must also be built with
    # one or the other
    # variant('mpir', default=False,
    #         description='Compile with the MPIR library')

    # Build dependencies
    depends_on("m4", type="build")
    depends_on("autoconf", when="@master", type="build")
    depends_on("automake", when="@master", type="build")
    depends_on("libtool", when="@master", type="build")

    phases = ['autoreconf', 'configure', 'build', 'install']

    def autoreconf(self, spec, prefix):
        # Versions of autoconf greater than 2.69 need config.guess
            autoreconf("-i")

    def configure(self, spec, prefix):
        configure_script = Executable("./configure")
        configure()

    def build(self, spec, prefix):
        make()
        if self.run_tests:
            make("check")

    def install(self, spec, prefix):
        #options = ["--prefix=%s" % prefix,
        #           "--with-gmp=%s" % spec['gmp'].prefix,
        #           "--with-mpfr=%s" % spec['mpfr'].prefix]
        #configure(*options)
        #make()
        #if self.run_tests:
        #    make("check")
        make("install")

