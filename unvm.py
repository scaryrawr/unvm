#! /usr/bin/env python3

import argparse
import io
import json
import os
import requests
import zipfile

root_dir = os.path.join(os.environ['LOCALAPPDATA'], 'unvm')
installed_dir = os.path.join(root_dir, 'installed')

def get_manifest():
    response = requests.get('https://unofficial-builds.nodejs.org/download/release/index.json')
    if not response.ok:
        print('Could not load build manifest')
        exit(-1)

    return json.loads(response.content)

def filter_entries(manifest):
    return [item for item in manifest if 'win-arm64-zip' in item['files']]

def installed():
    if (os.path.exists(installed_dir)):
        return [folder.removeprefix('node-').removesuffix('-win-arm64') for folder in os.listdir(installed_dir)]
    
    return []

def install(version, manifest):
    if version == 'lts':
        version = next(filter(lambda item: item['lts'], manifest))['version']
    
    target = 'https://unofficial-builds.nodejs.org/download/release/' + version + '/node-' + version + '-win-arm64.zip'
    file_response = requests.get(target)
    if not file_response.ok:
        print('Failed to download nodejs')
        exit(-1)
    
    file = io.BytesIO(file_response.content)
    os.makedirs(installed_dir, exist_ok=True)
    with zipfile.ZipFile(file, 'r') as archive:
        archive.extractall(installed_dir)

    os.chdir(root_dir)
    link_path = os.path.join('.', 'node')
    if os.path.exists(link_path):
        print(version + ' installed')
        print('To use:')
        print('unvm --use ' + version)
    else:
        use(version)

def use(version):
    os.chdir(root_dir)
    link_path = os.path.join('.', 'node')
    if os.path.exists(link_path):
        os.unlink(link_path)
    os.symlink(os.path.join('.', 'installed', 'node-' + version + '-win-arm64'), os.path.join('.', 'node'))
    print('Now using node ' + version)

manifest = filter_entries(get_manifest())
available = ['lts'] + [item['version'] for item in manifest]

parser = argparse.ArgumentParser(description='Manage node installs on Windows arm64')
parser.add_argument('--install', choices=available, help='Install a specific version of node')
parser.add_argument('--available', default=False, action='store_true', help='List available node versions to install')
parser.add_argument('--use', type=str, choices=installed(), help='Switch to an installed node version')
parser.add_argument('--installed', default=False, action='store_true', help='List installed versions of node')


args = parser.parse_args()

if args.available:
    print(available)

if args.installed:
    print(installed())

if args.install:
    install(args.install, manifest)

if args.use:
    use(args.use)
