# Copyright 2013-2021 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *

class NeatIBP(Package):

    git      = "https://github.com/yzhphy/NeatIBP.git"

    # maintainers = ['github_user1', 'github_user2']

    version('1.0.1.2', branch='main')


    depends_on('spasm@1.2')
