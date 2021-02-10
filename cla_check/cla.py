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


from . import lp, term


def is_corporate_cla_contributor(email: str) -> bool:
    return email.endswith("@canonical.com") or email.endswith("@mozilla.com")


def print_email_ok(*, email: str, reason: str, align_width: int):
    print(f"{term.GREEN}✓{term.RESET} {email:<{align_width}} {reason}")


def print_email_warn(*, email: str, reason: str, align_width: int):
    print(f"{term.YELLOW}‽{term.RESET} {email:<{align_width}} {reason}")


def print_email_fail(*, email: str, reason: str, align_width: int):
    print(f"{term.RED}🛇{term.RESET} {email:<{align_width}} {reason}")


def check_email(*, email: str, align_width: int = 0):
    if is_corporate_cla_contributor(email):
        print_email_ok(
            email=email, reason="has corporate agreement", align_width=align_width
        )
        return True

    contributor = lp.query_person(email=email)
    if contributor in lp.query_cla_participants():
        print_email_ok(
            email=email,
            reason=f"({contributor.display_name}) has signed the CLA",
            align_width=align_width,
        )
        return True

    if email.endswith("@users.noreply.github.com"):
        print_email_warn(
            email=email,
            reason="privacy-enabled github web edit email address",
            align_width=align_width,
        )
        return False

    print_email_fail(
        email=email, reason="has NOT signed the CLA", align_width=align_width
    )
    return False
