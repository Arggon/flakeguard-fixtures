"""Synthetic fixture tests. The flake is injected deliberately, not a product bug."""
import os

import pytest


def _run_number():
    return int(os.environ.get("GITHUB_RUN_NUMBER", "2"))


def test_injected_flake_by_run_parity():
    """Fails on odd workflow run numbers and passes on even ones (same commit)."""
    run = _run_number()
    assert run % 2 == 0, f"injected synthetic flake: odd workflow run number {run}"


def test_stable_addition():
    assert 1 + 1 == 2


def test_stable_string():
    assert "flake".upper() == "FLAKE"


def test_always_broken():
    assert False, "intentionally broken fixture test"


@pytest.mark.skip(reason="skipped fixture test")
def test_skipped():
    assert True
