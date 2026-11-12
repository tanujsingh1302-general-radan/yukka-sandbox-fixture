# yukka-sandbox-fixture

A tiny, **dependency-free** Python project for the Yukka Stage 2 sandbox checkpoint.

- `calc/`: a few pure functions.
- `tests/`: `unittest` tests. Run them with `python -m unittest -v`; pytest is not needed, and the sandbox image has no pytest.
- `probe.py`: a network-isolation probe. Inside the AUDIT sandbox, every line must be `PASS`, and the script exits 0 only if nothing could connect or resolve.

```
python -m unittest -v
python probe.py
```

On a normal machine with network access, `probe.py` prints `FAIL` for anything reachable and exits 1. That is the expected result outside the sandbox.

## Push it to your own GitHub repo

Create an **empty, public** repo, e.g. `yukka-sandbox-fixture`, under your account (no README or license, so the first push is clean). It has to be public because the hardened clone runs without credentials.

Copy this folder **out of the Yukka repo** first, so you don't nest one git repo inside another. Then, from the copy:

```
git init -b main
git add -A
git commit -m "sandbox fixture"
git remote add origin https://github.com/<your-user>/yukka-sandbox-fixture.git
git push -u origin main
```

Put exactly that repo URL into `YUKKA_SBX_TRUSTED_REPOS`.
