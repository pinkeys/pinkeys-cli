# PINKEYS-cli

## Project Definition

This cli allows you to retrieve and share your public keys (e.g., PGP, ssh, etc...) stored in the PINKEYS platform.

## What is PINKEYS

PINKEYS is a privacy key directory that provides an easy way to create, share and use your everything keys (e.g., PGP, SSH and all sort of privacy keys).

As a directory service, PINKEYS needs a companion tool to access it. Users and developers are our feedback loop to keep enhancing the capabilities of a platform.

## Goals

A portable CLI to allow computer professionals to pull and share their public keys (e.g., SSH, PGP, etc...) with others or download them to systems that require them. This repo allows our community to enhance the platform openly.

## Usage

The PINKEYS cli is an Open Source project created to help computer users extract privacy keys from our public keys directory. It is also a project to show developers how to program against our privacy platform API.


## Installation

``` bash
# pip install pinkeys
```

### CLI Usage

``` bash
# pinkeys --help


usage: pinkeys.py [-h] [--user USER] [--key-type KEY_TYPE]
                  [--key-file KEY_FILE]

Retrieve public key from the pinkeys.com

optional arguments:
  -h, --help            show this help message and exit
  --user USER, -u USER  The www.pinkey.com username (default: )
  --key-type KEY_TYPE   Type of public key to extract (default: ssh)
  --key-file KEY_FILE, -k KEY_FILE
                        Output file to write the public key (default: )

# pinkeys -u jdoe
blabla_some_public_key_output_spilledhere
```

## Create an account

[Create an account at PINKEYS](https://www.pinkeys.com)

[CLI User Guide](https://docs.pinkeys.com/#/en/apps/cli)


## Dev Build

```bash
python3 -m venv venv
. vent/bin/activate
pip3 install -f requirements.txt
python3 pinkeys
```