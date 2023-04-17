# Copyright 2013-2021 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *

class Neatibp(AutotoolsPackage):

    git      = "https://github.com/yzhphy/NeatIBP.git"

    # maintainers = ['github_user1', 'github_user2']

    version('1.0.1.2', branch='main')


    depends_on('spasm@1.2')
    depends_on('singular@snapshot_22_03')
    
    def setup_run_environment(self, env):
        spec = self.spec
        env.set('SINGULAR_INSTALL_DIR', spec['singular'].prefix)
        env.set('NEATIBP_INSTALL_DIR', self.prefix)
        env.set('SPASM_INSTALL_DIR', spec['spasm'].prefix)
