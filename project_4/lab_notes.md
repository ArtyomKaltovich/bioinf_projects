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
