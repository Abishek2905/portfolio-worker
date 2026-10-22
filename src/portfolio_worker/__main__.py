import sys

from portfolio_worker.config import get_environment


def main() -> int:
    current_env = get_environment()
    print(f"Portfolio worker started in {current_env} environment")
    return 0


if __name__ == "__main__":
    sys.exit(main())
