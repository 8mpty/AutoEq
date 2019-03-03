# -*- coding: utf-8 -*-

import os
import sys
import json
sys.path.insert(1, os.path.realpath(os.path.join(sys.path[0], os.pardir)))
DIR_PATH = os.path.abspath(os.path.join(__file__, os.pardir))


def main():
    with open(os.path.join(DIR_PATH, 'names.txt'), 'r') as f:
        old = f.read().split('\n')

    with open(os.path.join(DIR_PATH, 'links.json'), 'r') as f:
        new = json.loads(f.read())

    for name in list(new.keys()):
        if name in old:
            del new[name]

    print()
    print('\n'.join(new.keys()))


if __name__ == '__main__':
    main()
