# curie-acc2570-demo

Disposable repository for the Curie v0.9.0 release acceptance run (issue 2570).
It backs the `acme-demo` workload in the `sre-demo` namespace.

## Checks

Dependencies are bundled in `.wheels/`, so the checks need no package registry.
Run exactly this from the repository root:

```
python -m venv /workspace/.venv
/workspace/.venv/bin/pip install --disable-pip-version-check --no-index --find-links /workspace/.wheels pytest==8.3.5
cd /workspace && /workspace/.venv/bin/python -m pytest -q
```
