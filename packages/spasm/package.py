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
    depends_on('autoconf', type='build')

    phases = ['automake', 'configure', 'build', 'install']

    force_autoreconf = True

    def configure(self, spec, prefix):
        configure_script = Executable("./configure")
        configure(*self)

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
