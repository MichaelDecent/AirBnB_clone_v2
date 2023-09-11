#!/usr/bin/python3
"""
 a Fabric script (based on the file 3-deploy_web_static.py)
 that deletes out-of-date archives, using the function do_clean
"""

from fabric.api import *
from os.path import exists
from os import getenv, environ
from datetime import datetime

env.hosts = ['54.208.65.105', '18.209.152.183']
env.user = 'ubuntu'
env.key_filename = '/home/vagrant/.ssh/id_rsa'


def do_clean(number=0):
    """Deletes out-of-date archives"""
    number = int(number)
    number = 1 if number <= 1 else number

    run_locally = getenv("run_locally", None)
    if run_locally is None:
        with lcd("versions"):
            local(f"$(ls -t | tail -n +{1 + number} | sudo xargs rm)")
        with lcd("/data/web_static/releases"):
            local(f"$(ls -t | tail -n +{1 + number} \
| grep -v 'test' | sudo xargs rm -rf)")
        environ['run_locally'] = "True"
        print("Deleted outdated archives locally")

    with cd("/data/web_static/releases"):
        sudo(f"$(ls -t | tail -n +{1 + number} \
| grep -v 'test' | xargs rm -rf)")

    print("Outdated archives completely deleted!")
