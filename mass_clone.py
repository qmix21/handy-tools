#!/usr/bin/env python
from github import Github
from git import Repo
import argparse
import sys
import os.path
from os import path

def clone_repos(token, prefix="", directory=""):
    try:
        g = Github(token)
        for repo in g.get_user().get_repos():
            if prefix:
                if repo.name.startswith(prefix):
                    if directory and not path.exists(directory + "/" + repo.name):
                        Repo.clone_from(repo.ssh_url, (directory + "/" + repo.name))
                    else:
                        print(repo.name + " Already Exists: ")
            else:
                print('No Prefix Provided')
                sys.exit()

    except Exception as e:
        print(e)


parser = argparse.ArgumentParser(description='Github Repo Cloner')
parser.add_argument('--token', help='Github Private Token')
parser.add_argument('--prefix', help='Prefix of repos to clone')
parser.add_argument('--directory', help='Directory to clone repos')
args = parser.parse_args()

if not args.token:
    "Missing Token"
    sys.exit()
clone_repos(args.token, args.prefix, args.directory)
