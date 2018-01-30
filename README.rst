PINKEYS cli
=======================

Share all your keys on a single platform.  PINKEYS is a directory that provides an easy way to create, share and use your everything keys.
We are the Internets only key directory where you can add your PGP, SSH and all sort of public keys for you to share with everyone.

As Global directory service the service needs a companion tool. Users and developers alike provide the backbone of enhancing the capabilities of a platform.

You can find more information about PINKEYS here. 

`Create an account at PINKEYS <https://www.pinkeys.com>`_
`CLI User Guide <https://docs.pinkeys.com/#/en/apps/cli>`_.

-----

Usage:

The PinKey CLI is an Open Source project created to help system administrator extract privacy keys from our users. It is also a project to show developers how to program against our privacy platform API.
Usage

pinkeys --help


usage: pinkeys.py [-h] [--user USER] [--key-type KEY_TYPE]
                  [--key-file KEY_FILE]

Retrieve public key from the pinkeys.com

optional arguments:
  -h, --help            show this help message and exit
  --user USER, -u USER  The www.pinkey.com username (default: )
  --key-type KEY_TYPE   Type of public key to extract (default: ssh)
  --key-file KEY_FILE, -k KEY_FILE
                        Output file to write the public key (default: )

Example:

pinkeys -u jdoe

blabla_some_public_key_output_spilledhere

---

`Contribute to our open project <https://github.com/orgs/pinkeys/pinkeys-cli>`_.
