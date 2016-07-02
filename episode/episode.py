#!/usr/bin/python3
from glob import glob
from random import choice
try:
    from subprocess import call as run
except:
    from subprocess import run

def random_sagan(sagan_dir):
    sagan_vids = glob(sagan_dir + '*.avi')
    sagan_vid = choice(sagan_vids)
    run(['vlc', sagan_vid])

if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument('--sagan_dir',
                        default="/storage/Videos/Cosmos/Sagan/Carl Sagan's Cosmos/", help='Path to the sagan video directory!')

    args = parser.parse_args()
    random_sagan(args.sagan_dir)

