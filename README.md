# Example Repository for Custom Python Component

This is an example repository showing how you can use a custom Git repository for passing your own code into Keboola's Custom Python Component (CPC).

As the main source file in this repo is located right in the root directory, importing other source files works as expected both when developing locally and when ran using CPC.

This example uses [Astral's](https://astral.sh/) brilliant [uv tool](https://docs.astral.sh/uv/#installation) for package management, so for running this code locally follow these steps:

```sh
# 💜 create virtual environment and install dependencies
uv sync
# 🚀 run
uv run main.py
```

**Note:** The `keboola.component` package is listed in the [pyproject.toml](pyproject.toml) file just as a dev dependency, because CPC already includes it. When  adding more dependencies to your project:
- Use `uv add` for adding runtime dependencies (these will be installed when running the project via CPC).
- Use `uv add --dev` for adding development dependencies (these won't be installed in CPC).
