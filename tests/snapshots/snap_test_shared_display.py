# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots['test_clear_last_line 1'] = '\x1b[F\x1b[K'

snapshots['test_print_error 1'] = '\x1b[31m🔥 Error: test\x1b[0m'
