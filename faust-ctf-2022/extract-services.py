#!/usr/bin/env python3

"""
Decrypt and extract the services tar, and stream the data to the install handlers
(tar x or sh)
"""

import sys
from pathlib import Path
import os
import subprocess
from tarfile import TarFile, TarInfo
import tarfile
import logging
from tqdm import tqdm

logger = logging.getLogger(__name__)

def open_tar(fname: Path):
    pwd = input("Decryption Password: ").strip()

    logger.info("Calling gpg to decrypt %s", fname)
    gpg = subprocess.Popen(["gpg",
        "--decrypt",
        "--batch", "--pinentry-mode", "loopback",
        "--passphrase", pwd, fname],
        stdin=subprocess.DEVNULL, stdout=subprocess.PIPE)
    f = gpg.stdout
    tar = tarfile.open(mode = "r|xz", fileobj=f)
    return tar

def handle(tar: TarFile, member: TarInfo):
    no_pbar = False
    if member.name.endswith("dist_root.tar"):
        command = ["tar", "-ix", "--no-same-owner"]
    elif member.name == "docker.tar":
        command = ["tar", "-ix"]
    elif member.name.endswith("install.sh"):
        command = ["sh", "-v"]
        no_pbar = True
    else:
        logger.warning("ignoring unknown path %s in tar", member.name)
        return
    logger.info("running '%s' on '%s'", " ".join(command), member.name)
    stream = tar.extractfile(member)
    p = subprocess.Popen(command, stdin=subprocess.PIPE)
    desc = None if sys.stdout.isatty() else "\n"
    with tqdm(total=member.size, unit="B", unit_scale=True,
              mininterval=1, disable=no_pbar, desc=desc) as pbar:
        while True:
            data = stream.read(1024*1024)
            if not data: break
            try:
                p.stdin.write(data)
                pbar.update(len(data))
            except os.error:
                logger.exception("writing to command failed")
                break
    p.stdin.close()
    p.wait()
    if p.returncode != 0:
        logger.error("command failed with status %d", p.returncode)

def run(fname: str):
    tar = open_tar(fname)
    for member in iter(tar.next, None):
        handle(tar, member)
    logger.info("calling systemctl to reload and start all services")
    subprocess.call("systemctl restart docker".split())
    subprocess.call("systemctl daemon-reload".split())
    subprocess.call("systemctl enable --now faustctf.target".split())

if __name__ == "__main__":
    if len(sys.argv) == 2:
        input_file = Path(sys.argv[1])
    else:
        exit(f"usage: {sys.argv[0]} <encrypted services file>")

    input_file = input_file.resolve()
    os.chdir("/")

    run(input_file)
