#!/usr/bin/python3
# generates a .tgz archive from the contents of  web_static

import os.path
from datetime import datetime
from fabric.api import local


def do_pack():
    """ generates a .tgz archive from the contents of  web_static"""

    now = datetime.now()
    timestamp = now.strftime("%Y%m%d%H%M%S")
    archive_name = "versions/web_static_{}.tgz".format(timestamp)

    try:
        local("mkdir -p versions")
        local("tar -czvf {} web_static".format(archive_name))
        return archive_name
    except Exception:
        return None
