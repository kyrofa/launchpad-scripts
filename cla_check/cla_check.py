#!/usr/bin/env python3
#
# Copyright 2021 Canonical Ltd.
#
# This program is free software: you can term.REDistribute it and/or modify
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

import argparse
import sys

from . import cla


def cla_check_main():
    parser = argparse.ArgumentParser(description="")
    parser.add_argument("email_address", help="Email address to verify")

    opts = parser.parse_args()
    if not cla.check_email(email=opts.email_address):
        sys.exit(1)
