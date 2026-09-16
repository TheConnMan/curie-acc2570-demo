# curie-acc2570-demo

Disposable repository for the Curie v0.9.0 release acceptance run (issue 2570).
It backs the `acme-demo` workload in the `sre-demo` namespace.

## Checks

```
python -m venv /workspace/.venv
/workspace/.venv/bin/pip install -e .
/workspace/.venv/bin/python -m pytest -q
```
