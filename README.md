# Archived (I personally use fnm)

Check out [fnm](https://github.com/Schniz/fnm) (I didn't make it, I just use it 😅). It works on Linux, macOS, and Windows.

Their builds don't include arm64 by default, but you can install it from source using cargo:

```powershell
cargo install fnm
```

Then you can manage node versions using fnm:

```powershell
fnm install v20.15.1
fnm use v20.15.1 # may error and recommend updating your powershell profile
```

It's pretty much a drop in replacement for [nvm](https://github.com/nvm-sh/nvm) *nix version. (The Windows version of [nvm](https://github.com/coreybutler/nvm-windows) has slightly different commands vs nvm on *nix, so fnm being the same on both is really nice.).

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

Enable developer mode in Windows Settings. Current node version is set using symbolic links which require either admin or developer mode.

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
