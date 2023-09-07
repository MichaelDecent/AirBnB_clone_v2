#!/usr/bin/python3
"""
a Fabric script (based on the file 1-pack_web_static.py)
that distributes an archive to your web servers, using the function do_deploy
"""
from fabric.api import *

env.hosts = ['54.208.65.105', '18.209.152.183']
env.user = ['ubuntu']
env.key_filename = '/home/vagrant/.ssh/id_rsa'


def do_deploy(archive_path):
    if archive_path is None:
        return False

    archive_name = archive_path.split('/')[-1]
    file_name = archive_name.split('.')[0]
    sym_link = "/data/web_static/current"
    release_version = f"/data/web_static/releases/{file_name}"
    
    try:
        print(f"Deploying new_version from {archive_path}")
        put(f"{archive_path} /tmp/{archive_name}")
        run(f"tar -xvf /tmp/{archive_name} -C /data/web_static/releases/")
        run(f"mv /data/web_static/releases/{archive_name} {release_version}")
        run(f"rm -rf /temp/{archive_name}")
        run(f"rm -rf {sym_link}")
        run(f"ln -s /data/web_static/releases/{file_name} {sym_link}")
        print("New Version Deployed!")
        return True
    except Exception as e:
        print(f"Failed to Deploy new_version --> {release_version}")
        return False
