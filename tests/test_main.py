import subprocess
import sys

from portfolio_worker.__main__ import main


def test_main():
    assert main() == 0


def test_worker_execution():
    result = subprocess.run(
        [sys.executable, "-m", "portfolio_worker"],
        capture_output=True,
        text=True,
        check=False,
        timeout=10,
    )

    assert result.returncode == 0
    assert "Portfolio worker started" in result.stdout
    assert result.stderr == ""
