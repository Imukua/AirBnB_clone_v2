#!/usr/bin/python3
# Fabfile to distribute an archive to web servers
from fabric.api import env, put, run, local
import os


env.hosts = ['54.209.94.49', '54.157.148.248']


def do_deploy(archive_path):
    """
    Distributes an archive to web servers and deploys it.
    Args: archive_path :: Path to archive to be distributed
    Return: If any error: Fale
            Otherwise: True
    """
    if not os.path.isfile(archive_path):
        return False

    try:
        archive_filename = os.path.basename(archive_path)
        archive_name_without_extension = archive_filename.split('.')[0]

        put(archive_path, "/tmp/{}".format(archive_filename))
        run("mkdir -p /data/web_static/releases/{}/"
            .format(archive_name_without_extension))
        run("tar -xzf /tmp/{} -C /data/web_static/releases/{}/"
            .format(archive_filename, archive_name_without_extension))
        run("rm /tmp/{}".format(archive_filename))
        run("rm -rf /data/web_static/current")
        run("ln -s /data/web_static/releases/{}/ /data/web_static/current"
            .format(archive_name_without_extension))

        return True

    except Exception:
        return False
