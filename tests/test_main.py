import os
import subprocess
import sys
import pytest

from portfolio_worker.__main__ import main


def test_main(monkeypatch):
    monkeypatch.setenv("PORTFOLIO_ENV", "test")

    assert main() == 0


def test_worker_execution():
    env = os.environ.copy()
    env["PORTFOLIO_ENV"] = "test"

    result = subprocess.run(
        [sys.executable, "-m", "portfolio_worker"],
        capture_output=True,
        text=True,
        check=False,
        timeout=10,
        env=env,
    )

    assert result.returncode == 0
    assert "Portfolio worker started in test environment" in result.stdout
    assert result.stderr == ""


def test_main_invalid_environment(monkeypatch):
    """Test that the main function raises ValueError for invalid environment."""
    monkeypatch.setenv("PORTFOLIO_ENV", "invalid")

    with pytest.raises(ValueError, match="Invalid PORTFOLIO_ENV"):
        main()
