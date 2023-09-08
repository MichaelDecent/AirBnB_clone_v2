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
        archive_name = archive_path.split('/')[-1]
        file_name = archive_name.split('.')[0]
        sym_link = "/data/web_static/current"
        release_version = f"/data/web_static/releases/{file_name}/"

        print(f"Deploying new_version from {archive_path}")
        put(archive_path, f"/tmp/{archive_name}")
        run(f"mkdir -p {release_version}")
        run(f"tar -xzf /tmp/{archive_name} \
-C {release_version} --strip-components=1")
        run(f"rm /tmp/{archive_name}")
        run(f"rm -f {sym_link}")
        run(f"ln -s {release_version} {sym_link}")
        print(f"New Version Deployed --> {release_version}")
        return True
    except Exception as e:
        print(f"Failed to Deploy New Version --> {release_version}\n{str(e)}")
        return False
