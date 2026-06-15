# Pendulum

## Setup

Clone the simulation repository and run the sync step below.

1. Clone the repo:

```bash
git clone https://github.com/Danglee1107/pendulum-simulation.git
```

2. Change into the project directory:

```bash
cd pendulum-simulation
```

3. Run the sync command:

```bash
uv sync
```

4. Sync dependencies

`uv sync` reads the project's `uv.lock` file and downloads the libraries required to run the project.

Run `uv sync` inside an activated virtual environment. Example (PowerShell on Windows):

```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
uv sync
```

Example (bash / POSIX):

```bash
python -m venv .venv
source .venv/bin/activate
uv sync
```

Verify the `uv` CLI is available before running sync:

```bash
uv --version
```

If `uv` is not installed, follow your project's `uv` installation instructions (install method depends on the `uv` tool you use). If you meant `uvicorn` for a FastAPI app instead, install requirements and run:

```bash
pip install -r requirements.txt
uvicorn main:app --reload
```

If you'd like, I can add a small helper script (`scripts/sync.ps1` / `scripts/sync.sh`) to automate these steps.
