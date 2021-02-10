from cla_check import cla, lp
import pytest

from unittest import mock


@pytest.fixture(autouse=True)
def fake_lp():
    class FakeLpObject:
        display_name = "Launchpad User"

    fake_user = FakeLpObject()

    def query_cla_participants():
        return [fake_user]

    def query_person(email):
        return fake_user if email == "lp-user@email.com" else None

    with mock.patch("cla_check.cla.lp", autospec=lp) as lp_mock:
        lp_mock.query_cla_participants.side_effect = query_cla_participants
        lp_mock.query_person.side_effect = query_person
        yield lp_mock


def test_canonical(capsys):
    assert cla.check_email(email="somebody@canonical.com") is True

    assert "somebody@canonical.com has corporate agreement" in capsys.readouterr().out


def test_mozilla(capsys):
    assert cla.check_email(email="somebody@mozilla.com") is True

    assert "somebody@mozilla.com has corporate agreement" in capsys.readouterr().out


def test_invalid_participant(capsys):
    assert cla.check_email(email="not-lp-user@email.com") is False

    assert "not-lp-user@email.com has NOT signed the CLA" in capsys.readouterr().out


def test_valid_participant(capsys):
    assert cla.check_email(email="lp-user@email.com") is True

    assert (
        "lp-user@email.com (Launchpad User) has signed the CLA"
        in capsys.readouterr().out
    )
