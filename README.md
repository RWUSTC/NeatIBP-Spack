# NeatIBP-Spack
This is the Spack package for <a href="https://github.com/yzhphy/NeatIBP">NeatIBP</a>

We will assume that the user has some directory path with read and
write access. In the following, we assume this path is set as the environment variable
`software_ROOT`, as detailed in the following example:

```bash
mkdir ~/neatibp-spack
mkdir ~/neatibp-install
export software_ROOT=~/neatibp-spack
export install_ROOT=~/neatibp-install

```
Note, this needs to be set again if you open a new terminal session (preferably set it automatically by adding the line to your .profile file).

## Install Spack
If Spack is not already present in the above directory, clone Spack from Github:
```bash
git clone https://github.com/spack/spack.git $software_ROOT/spack

```
We check out verison v0.19.0 of Spack (the current version):
```bash
cd $software_ROOT/spack
git checkout releases/v0.19
cd $software_ROOT

```
Spack requires a couple of standard system packages to be present. For example, on an Ubuntu machines they can be installed by the following commands (which typically require sudo privilege)

```bash
sudo apt update

```
```bash
sudo apt install build-essential ca-certificates coreutils curl environment-modules gfortran git gpg lsb-release python3 python3-distutils python3-venv unzip zip

```

To be able to use spack from the command line, run the setup script:
```bash
. $software_ROOT/spack/share/spack/setup-env.sh

```
Note, this script needs to be executed again if you open a new terminal session (preferably set it automatically by adding the line to your .profile file).

Finally, Spack needs to boostrap clingo.  This can be done by concretizing any
spec, for example
```bash
spack spec zlib

```

Note: If you experience connection timeouts due to a slow internet connection you can set in the following file the variable `connect_timeout` to a larger value.
```bash
vim $software_ROOT/spack/etc/spack/defaults/config.yaml

```

### How to uninstall Spack
Note that Spack can be uninstalled by just deleting its directory and its configuration files. Be CAREFUL to do that, since it will delete your Spack setup. Typically you do NOT want to do that now, so the code is commented out. It can be useful if your Spack installation is broken:

```bash
#cd
#rm -rf $software_ROOT/spack/
#rm -rf .spack

```

## Install NeatIBP

Once you have installed Spack, our package can be installed with just three lines of code.

Clone the NeatIBP package repository into this directory:
```bash
git clone https://github.com/RWUSTC/neatibp-spack.git $software_ROOT/neatibp-spack

```

Add the NeatIBP package repository to the Spack installation:
```bash
spack repo add $software_ROOT/neatibp-spack

```

## Installing packages

Now you are good to go to install specific packages of the repo. For example, you could do:

```bash
spack install neatibp

```

If you install your first package, this will take a bit of time since a lot of dependencies are installed, e.g. Singular and SpaSM.

To use the package you have to load it:

```bash
spack load neatibp

```
Then one should change to the default_settings.txt and modify the following variables to the installation of the dependencies. 

One can just run the script to do the substitution and delete the script by:


```bash

sh ~/spack_sub_script.sh

rm -rf ~/spack_sub_script.sh

```
Or manually do as the following:

```bash

cd $NEATIBP_INSTALL_DIR/NeatIBP

sed -i 's@/usr/local/lib@'"$SPASM_INSTALL_DIR/lib"'@' default_settings.txt

sed -i 's@/usr/bin/Singular@'"$SINGULAR_INSTALL_DIR/bin"'@' default_settings.txt

sed -i 's@$(dirname $( realpath ${BASH_SOURCE}))@'"$NEATIBP_INSTALL_DIR/NeatIBP"'@' run.sh

sed -i 's@$(dirname $( realpath ${BASH_SOURCE}))@'"$NEATIBP_INSTALL_DIR/NeatIBP"'@' monitor.sh

sed -i 's@$(dirname $( realpath ${BASH_SOURCE}))@'"$NEATIBP_INSTALL_DIR/NeatIBP"'@' continue.sh

```
One should copy the main files to some directory, for example, $install_ROOT/NeatIBP

```bash

cd $install_ROOT/NeatIBP

cp $NEATIBP_INSTALL_DIR/NeatIBP/continue.sh continue.sh

cp $NEATIBP_INSTALL_DIR/NeatIBP/run.sh run.sh

cp $NEATIBP_INSTALL_DIR/NeatIBP/monitor.sh monitor.sh

cp $NEATIBP_INSTALL_DIR/NeatIBP/default_settings.txt config.txt

mkdir outputs

```

One can test one of the examples in this folder, for example, double box,


```bash

cd $install_ROOT/NeatIBP

cp $NEATIBP_INSTALL_DIR/NeatIBP/examples/dbox/kinematics.txt kinematics.txt

cp $NEATIBP_INSTALL_DIR/NeatIBP/examples/dbox/targetIntegrals.txt targetIntegrals.txt

```

And, one can run:


```bash

./run.sh

```

After this, NeatIBP is good to go.

Please refer to the repos of NeatIBP on how to use them.

URL: https://github.com/yzhphy/NeatIBP
