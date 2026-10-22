import pytest

from portfolio_worker.config import get_environment


def test_default_environment(monkeypatch):
    """Test that the default environment is 'development' when PORTFOLIO_ENV is not set."""
    monkeypatch.delenv("PORTFOLIO_ENV", raising=False)

    assert get_environment() == "development"


def test_valid_environment_normalized(monkeypatch):
    """Test that valid environments are returned correctly."""
    monkeypatch.setenv("PORTFOLIO_ENV", " TEST ")
    assert get_environment() == "test"


def test_invalid_environment(monkeypatch):
    """Test that invalid environment values raise a ValueError."""
    monkeypatch.setenv("PORTFOLIO_ENV", "invalid")

    with pytest.raises(ValueError, match="Invalid PORTFOLIO_ENV"):
        get_environment()
