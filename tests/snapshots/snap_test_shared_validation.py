# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots['test___is_each_word_available 1'] = [
    "Error: 'e' is already used in a spell"
]

snapshots['test___is_each_word_available 2'] = [
    "Error: 'add' is a reserved word"
]

snapshots['test___print_validation_errors 1'] = '''\x1b[33mError: 'add' is a reserved word
Error: 'example' is already used in a spell
\x1b[0m'''
