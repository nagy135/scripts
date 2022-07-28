#!/bin/python

import sys
import re
from typing import List, Union
from enum import Enum

N=16

class Modes(Enum):
    ADD = 'add',
    REMOVE = 'remove',
    PRETTIFY = 'prettify',
    NONE = None,

def usage():
    print("Usage: floorball_list [OPTION]")
    print("Manages list of floorball members")
    print("")
    print("Options:")
    print("  -h, --help                 show this message and quit")
    print("  -p, --prettify             just reformat table to fixed form")
    print("  -a, --add    [name]        add new member to game")
    print("  -r, --remove [index]       remove member by his index")

def print_table(mems: List[str], head: Union[str, None]):
    if head is not None:
        print(head)
    for i in range(N):
        index = str(i+1).rjust(2, ' ')
        if i >= len(mems):
            print(f'{index}.')
            continue
        member = mems[i].strip()
        member_parts = member.split()
        if len(member_parts) == 2:
            member = f'{member_parts[0].capitalize()} {member_parts[1][0].upper()}.'
        print(f'{index}. {member}')

if len(sys.argv) < 2:
    usage()
    sys.exit(1)

if '-h' in sys.argv or '--help' in sys.argv:
    usage()
    sys.exit(0)

MODE: Modes = Modes.NONE
if '-a' in sys.argv or '--add' in sys.argv:
    MODE = Modes.ADD
elif '-r' in sys.argv or '--remove' in sys.argv:
    MODE = Modes.REMOVE
elif '-p' in sys.argv or '--prettify' in sys.argv:
    MODE = Modes.PRETTIFY

if MODE == Modes.NONE:
    print('No mode chosen!')
    usage()
    sys.exit(1)

ARG: Union[str, None] = None
if MODE in [Modes.REMOVE, Modes.ADD]:
    if len(sys.argv) < 3:
        print('Provide argument!')
        usage()
        sys.exit(1)
    else:
        ARG = sys.argv[2]

members: List[str] = []
header: Union[str, None] = None
for i, line in enumerate(sys.stdin):
    line = line.strip()
    if i == 0:
        first_line_re = re.compile(r'^\s*\d')
        if first_line_re.match(line) is None:
            header = line
            continue
    parts = line.split('.', 1)
    if len(parts) < 2 or parts[1] == '':
        continue
    members.append(parts[1])

if MODE == Modes.REMOVE:
    if ARG is not None:
        members.pop(int(ARG) - 1)
elif MODE == Modes.ADD:
    if ARG is not None:
        members.append(ARG)

print_table(members, header)
