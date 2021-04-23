# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot

snapshots = Snapshot()

snapshots["test_clear_last_line 1"] = "\x1b[F\x1b[K"

snapshots["test_in_color 1"] = [
    "\x1b[30mtest\x1b[0m",
    "\x1b[31mtest\x1b[0m",
    "\x1b[32mtest\x1b[0m",
    "\x1b[33mtest\x1b[0m",
    "\x1b[34mtest\x1b[0m",
    "\x1b[35mtest\x1b[0m",
    "\x1b[36mtest\x1b[0m",
    "\x1b[37mtest\x1b[0m",
]

snapshots["test_print_error 1"] = "\x1b[31m🔥 test\x1b[0m"
