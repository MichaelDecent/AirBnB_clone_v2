#!/usr/bin/python3
"""
a Fabric script (based on the file 1-pack_web_static.py)
that distributes an archive to your web servers, using the function do_deploy
"""


from fabric.api import *
from os.path import exists

env.hosts = ['54.208.65.105', '18.209.152.183']
env.user = 'ubuntu'
env.key_filename = '/home/vagrant/.ssh/id_rsa'


def do_deploy(archive_path):
    """Deploys the web static to the server"""
    if not exists(archive_path):
        return False

    try:
        archive_name = archive_path.split("/")[-1]
        folder_name = archive_name.split(".")[0]
        releaseVersion = "/data/web_static/releases/{}/".format(folder_name)
        symLink = "/data/web_static/current"

        print("Deploying new version from {}...".format(folder_name))
        put(archive_path, "/tmp/{}".format(archive_name))
        run("mkdir -p {}".format(releaseVersion))
        run("tar -xzf /tmp/{} -C {} --strip-components=1".format(
            archive_name, releaseVersion))
        run("rm /tmp/{}".format(archive_name))
        run("rm -f {}".format(symLink))
        run("ln -s {} {}".format(releaseVersion, symLink))
        print("New version deployed -> {}".format(releaseVersion))
        return True
    except Exception:
        print("Failed to deploy new version -> {}".format(releaseVersion))
        return False
