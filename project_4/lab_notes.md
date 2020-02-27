* 23.02.2020 - download data
* 24.02.2020 - trying to install repeatmodeler

    $ yaourt -S anaconda

fails as there are not free space, clean it and using python-conda

    $ yaourt -S python-conda
    
fails. Updating them with pip gave nothing.
The reason was yaourt can't overwrite files created by pip. Google suggest 
using --overwrite flag

    $ yaourt -S python-conda --overwrite paths
    $ yaourt --overwrite paths -S python-conda
    $ yaourt -S --overwrite paths python-conda

all failed.

    $ yaourt -S python-conda --force
    
works!

    $ conda install -c bioconda repeatmodeler

fails as no conda environment. Create it, trying to activate it fails due to
lack of user writes and config files. When I was trying to fix it - sudo was 
broken due to recursive chmod. Fixing it with logout/login by the way 
ctrl+alt+f1 doesn't work as expected in arch linux.

That's all, folks!

* 24.02.2020 - still trying to install repeatmodeler
 
- removing python-conda and install miniconda3 it fails with
        
        
    Traceback (most recent call last):
      File "/usr/condabin/conda", line 12, in <module>
        from conda.cli import main
          ModuleNotFoundError: No module named 'conda'

- installing conda with pip, it still fails
- the problem was with command suggested by conda
    
    
    $ sudo ln -s /opt/miniconda3/etc/profile.d/conda.sh /etc/profile.d/conda.sh

- the one should use
    
    
    $ echo "[ -f /opt/miniconda3/etc/profile.d/conda.sh ] && source /opt/miniconda3/etc/profile.d/conda.sh" >> ~/.bashrc
    
- It's alive! But still does work, as can't satisfy dependencies
    
- creating new conda's environment
- still fails
- updating python packages with 
    
    
    $ sudo pip install -U $(pip freeze | awk '{split($0, a, "=="); print a[1]}')
    ERROR: Cannot uninstall 'pep517'. It is a distutils installed project and thus we cannot accurately determine which files belong to it which would lead to only a partial uninstall.
    
- fixed with
    
    
    $ sudo pip install --ignore-installed pep517
    
- still fails
    
    
    Collecting xgboost
      Using cached xgboost-1.0.1-py3-none-manylinux1_x86_64.whl (109.7 MB)
    ERROR: Could not find a version that satisfies the requirement zippD (from versions: none)
    ERROR: No matching distribution found for zippD
    
    $ sudo pip uninstall xgboost

- still failing
    
    $ sudo pip install zipp
    
fails with
     
        ERROR: Could not find a version that satisfies the requirement urllib3D (from versions: none)
        ERROR: No matching distribution found for urllib3D
    
- trying on virtual machines - both failed
- trying to install directly by unpacking tar archive from official site - failed as no perl packages
- cpan failed to install them    
- installing with pacman
- repeatmodeler needs repeatmasker
- conda installation failed
- installing it from aur - yaourt is deprecated
- installing yay - package is outdated
- changing pckbuild - fails on integrity check
- disable integrity check
    
    
    install: cannot stat 'license.txt': No such file or directory
    ==> ERROR: A failure occurred in package()

- editing pkgbuild - installation stuck
