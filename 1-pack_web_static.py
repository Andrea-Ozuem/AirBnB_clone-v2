#!/usr/bin/python3
''' Script to br run for remote server'''

from datetime import datetime
from fabric.api import local
import os


def do_pack():
    '''generates a .tgz archive from the contents of folder'''
    try:
        local('mkdir -p versions')
        form = '%Y%m%d%H%M%S'
        tarfile = ('versions/web_static_{}.tgz'
                   .format(datetime.now().strftime('%Y%m%d%H%M%S')))
        res = local("tar -cvzf {} web_static/".format(tarfile))
        print('web_static packed: {} -> {} Bytes'.format(tarfile,
              os.stat(tarfile).st_size))
        return tarfile
    except Exception:
        return None
