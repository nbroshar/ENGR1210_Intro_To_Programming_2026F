# check_setup.py
# Run once before the Week 16 capstone:   python check_setup.py
# Reports whether all four quality tools are installed.
import importlib.util
import shutil


def have_module(name):
    return importlib.util.find_spec(name) is not None


def have_cli(name):
    return shutil.which(name) is not None


checks = [
    ("pytest", have_module("pytest")),
    ("pytest-cov", have_module("pytest_cov")),
    ("radon", have_module("radon") or have_cli("radon")),
    ("ruff", have_cli("ruff") or have_module("ruff")),
]

print("Week 16 setup check")
print("-" * 32)
all_ok = True
for name, ok in checks:
    print(f"  {'OK     ' if ok else 'MISSING'}  {name}")
    all_ok = all_ok and ok
print("-" * 32)
if all_ok:
    print("All set -- you're ready for the capstone.")
else:
    print("Missing tools. Run:  pip install -r requirements.txt")
