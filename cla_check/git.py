#!/usr/bin/env python3
#
# Copyright 2021 Canonical Ltd.
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License version 3 as
# published by the Free Software Foundation.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

import re
import subprocess

shortlog_email_rx = re.compile(r"^\s*\d+\s+.*<(\S+)>$", re.M)


def get_emails_for_range(commit_range: str):
    proc = subprocess.run(  # type: ignore
        ["git", "shortlog", "-se", commit_range], check=True, capture_output=True
    )

    return set(
        m.group(1) for m in shortlog_email_rx.finditer(proc.stdout.decode("utf-8"))
    )
