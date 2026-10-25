# Portfolio Worker

Python-based worker component for the Portfolio Platform.

This repository contains the independently executable Worker application. It is being developed incrementally to support background-processing responsibilities within the Portfolio Platform.

## 1. Current Implementation

The Worker currently includes:

- An installable Python package using the `src/` layout.
- A module entry point executable through `python -m portfolio_worker`.
- Environment configuration and validation.
- Automated configuration and execution tests using pytest.
- Reproducible dependency installation through `uv` and a committed lockfile.
- Python package build configuration using Hatchling.

**Not implemented yet:** Background job processing, task queues, job scheduling, external service integrations, or continuous worker execution.

The current entry point validates the environment, prints a startup message, and exits successfully.

## 2. Prerequisites

| Tool | Requirement | Purpose |
|---|---|---|
| Git | Recent supported version | Clone the repository |
| Python | 3.13 or newer | Application runtime |
| uv | Recent compatible version | Python and dependency management |

Python can be installed and managed through `uv`, so a separate system-wide installation is not required.

### Installing prerequisites

**macOS**

If Homebrew is installed:

```bash
brew install git uv
```

Then install Python:

```bash
uv python install 3.13
```

Homebrew installation instructions: https://brew.sh/

**Linux**

Install Git using your distribution's package manager.

Install uv using the official instructions:

https://docs.astral.sh/uv/getting-started/installation/

Then:

```bash
uv python install 3.13
```

**Windows**

Install Git and uv using their official installation guides:

- Git: https://git-scm.com/install/
- uv: https://docs.astral.sh/uv/getting-started/installation/

Install Python:

```powershell
uv python install 3.13
```

### Verify prerequisites

```bash
git --version
uv --version
uv python list --only-installed
```

Confirm that a compatible Python interpreter is available.

**Platform validation:** Setup and execution have been verified on macOS. Linux and Windows instructions are provided for portability but have not been independently validated.

## 3. Clone and Install

Clone the repository:

```bash
git clone https://github.com/Abishek2905/portfolio-worker.git
cd portfolio-worker
```

Install dependencies:

```bash
uv sync --locked
```

This command creates the project virtual environment if needed and installs the dependencies specified in `uv.lock`.

The project's required Python version is declared in `pyproject.toml`.

The virtual environment is managed automatically by `uv`, so manual activation is unnecessary.

## 4. Environment Configuration

The Worker uses `PORTFOLIO_ENV` to determine its runtime environment.

| Value | Description |
|---|---|
| `development` | Local development |
| `test` | Test execution |
| `production` | Production environment identifier |

If the variable is absent, the Worker defaults to `development`.

Values are normalized by removing surrounding whitespace and converting them to lowercase.

Unsupported or explicitly empty values raise `ValueError`.

### Setting the environment

On macOS or Linux:

```bash
PORTFOLIO_ENV=test uv run python -m portfolio_worker
```

On Windows PowerShell:

```powershell
$env:PORTFOLIO_ENV = "test"
uv run python -m portfolio_worker
```

### Environment example file

The repository includes `.env.example` documenting the supported configuration values.

The Worker uses `os.getenv()` and does not automatically load `.env` or `.env.example`.

Creating either file alone does not configure the running process. Supply environment variables to the process using your shell or process manager.

Local environment files are excluded from Git through `.gitignore`, while `.env.example` remains trackable.

Do not commit credentials, tokens, passwords, or other secrets.

Selecting `production` does not itself configure production infrastructure or enable production background processing.

## 5. Run the Worker

Execute the Worker:

```bash
uv run python -m portfolio_worker
```

Expected output when `PORTFOLIO_ENV` is unset:

```text
Portfolio worker started in development environment
```

Run using the test environment:

```bash
PORTFOLIO_ENV=test uv run python -m portfolio_worker
```

Expected output:

```text
Portfolio worker started in test environment
```

The Worker currently prints the selected environment and exits with status code `0` on successful execution.

It does not remain active or process jobs.

### Invalid environment

Running with an unsupported environment value results in a `ValueError`.

For example:

```bash
PORTFOLIO_ENV=invalid uv run python -m portfolio_worker
```

The command should fail with a nonzero exit status and report an invalid `PORTFOLIO_ENV`.

## 6. Automated Testing

Run the complete test suite:

```bash
uv run pytest -v
```

The current tests cover:

- Default environment selection.
- Normalization of supported environment values.
- Rejection of invalid environment values.
- Successful execution of the module entry point.
- Expected Worker startup output.
- Failure behavior when the environment is invalid.

Latest verified local result: **6 tests passed on macOS using Python 3.13.2.**

## 7. Dependency and Package Management

Application dependencies and development dependencies are declared in `pyproject.toml`.

The committed `uv.lock` file records the resolved dependency versions.

Use:

```bash
uv sync --locked
```

to reproduce the locked environment.

Hatchling is configured as the package build backend.

The Worker currently has no third-party runtime dependencies.

Future dependencies should be added only when required by implemented functionality, with the lockfile updated accordingly.

## 8. Troubleshooting

### `uv` is not found

Ensure uv is installed and accessible in your terminal's PATH.

Refer to the installation instructions in Section 2.

### Python version is incompatible

Check the installed Python interpreters:

```bash
uv python list --only-installed
```

Install Python 3.13 if needed:

```bash
uv python install 3.13
```

### Dependencies fail to install

Ensure you're in the repository root and that both `pyproject.toml` and `uv.lock` are present.

Review the error before modifying the lockfile.

### `No module named portfolio_worker`

Run dependency synchronization from the repository root:

```bash
uv sync --locked
```

Then invoke the Worker using:

```bash
uv run python -m portfolio_worker
```

### Invalid `PORTFOLIO_ENV`

Check that the environment variable is one of `development`, `test`, or `production`.

An explicitly empty value is invalid.

### Changes to `.env` have no effect

The Worker does not automatically load local `.env` files. Supply environment variables directly to the process.

### Worker exits immediately

This is the expected behavior of the current implementation.

Continuous processing and background job execution have not yet been implemented.

## 9. Repository Responsibilities

| Repository | Responsibility |
|---|---|
| `portfolio-worker` | Background-processing component |
| `portfolio-api` | Backend APIs and application logic |
| `portfolio-web` | Frontend application |
| `portfolio-platform` | Cross-repository orchestration and integration setup |

Each repository owns its component-specific configuration, dependencies, source code, and tests.

## 10. Development Roadmap

Future Worker capabilities will be introduced incrementally through the Portfolio Platform backlog.

Planned areas include background task execution and integration with other platform components.

This README documents the current executable baseline rather than functionality that has not yet been implemented.

Implementation progress and validation evidence are tracked in Jira comments, GitHub pull requests, and the existing Portfolio Platform Confluence roadmap.
