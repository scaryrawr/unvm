# Unofficial Node Version Manager

A utility around [nodejs unofficial-builds](https://unofficial-builds.nodejs.org/download/release/) for Windows on arm64.

## Options

```sh
  -h, --help            show this help message and exit
  --install             Install a specific version of node
  --available           List available node versions to install
  --use                 Switch to an installed node version
  --installed           List installed versions of node
```

## Requirements

### Windows Settings

Enable developer mode in Windows Settings.

### PIP Install

```sh
pip install requests
```

### Environment Variables

Update your environment PATH variable to include:

Path to where this was cloned (so you can type unvm anywhere):

```cmd
%USERPROFILE%\GitHub\unvm
```

For full Python install (so node can be found on path):

```cmd
%LOCALAPPDATA%\unvm\node
```

For Windows Store Python 3.10 install (so node can be found on path):

```cmd
%LOCALAPPDATA%\Packages\PythonSoftwareFoundation.Python.3.10_qbz5n2kfra8p0\LocalCache\Local\unvm\node
```
