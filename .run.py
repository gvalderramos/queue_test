import os
import webbrowser
import sys
import typer
import pathlib
import shutil
import subprocess

from urllib.request import pathname2url
from contextlib import contextmanager

app = typer.Typer()
RCC_EXEC = {
    "None": "",
    "PySide": "pyside-rcc",
    "PySide2": "pyside2-rcc",
    "PySide6": "pyside6-rcc",
    "PyQt4": "pyrcc4",
    "PyQt5": "pyrcc5"
}
UIC_EXEC = {
    "None": "",
    "PySide": "pyside-uic",
    "PySide2": "pyside2-uic",
    "PySide6": "pyside6-uic",
    "PyQt4": "pyuic4",
    "PyQt5": "pyuic5"
}
QT_WRAPPER = {
    "None": "",
    "qtpy": "qtpy",
    "Qt.py": "Qt"
}


def _delete_path(path: pathlib.Path):
    if path.exists():
        if path.is_dir():
            shutil.rmtree(path)
        else:
            path.unlink()


def _open_browser(path: str):
    webbrowser.open(f"file://{pathname2url(os.path.abspath(path))}")


@contextmanager
def _set_directory(path: pathlib.Path):
    origin = pathlib.Path().absolute()
    try:
        os.chdir(path)
        yield
    finally:
        os.chdir(origin)


@app.command(help="remove build artifacts")
def clean_build():
    _delete_path(pathlib.Path("build"))
    _delete_path(pathlib.Path("dist"))
    _delete_path(pathlib.Path(".eggs"))
    for p in pathlib.Path("src").rglob("*.egg-info"):
        _delete_path(p)
    for p in pathlib.Path("src").rglob("*.egg"):
        _delete_path(p)


@app.command(help="remove Python file artifacts")
def clean_pyc():
    for p in pathlib.Path("src").rglob("*.pyc"):
        _delete_path(p)

    for p in pathlib.Path("src").rglob("*.pyo"):
        _delete_path(p)

    for p in pathlib.Path("src").rglob("*~"):
        _delete_path(p)

    for p in pathlib.Path("src").rglob("__pycache__"):
        _delete_path(p)


@app.command(help="remove test and coverage artifacts")
def clean_test():
    _delete_path(pathlib.Path(".coverage"))
    _delete_path(pathlib.Path("htmlcov"))
    _delete_path(pathlib.Path(".pytest_cache"))


@app.command(help="remove all build, test, coverage and Python artifacts")
def clean():
    clean_build()
    clean_pyc()
    clean_test()


@app.command(help="check style")
def lint():
    subprocess.run("flake8 src/queue_test tests", shell=True)


@app.command(help="format the python source and test folder")
def format():
    subprocess.run("black src/queue_test tests", shell=True)


@app.command(help="run tests with pytest")
def test():
    subprocess.run("pytest", shell=True)


@app.command(help="check code coverage quickly with the default Python")
def coverage():
    subprocess.run("coverage run --source queue_test -m pytest", shell=True)
    subprocess.run("coverage report -m", shell=True)
    subprocess.run("coverage html", shell=True)
    _open_browser("htmlcov/index.html")


@app.command(help="generate Sphinx HTML documentation, including API docs")
def docs():
    _delete_path(pathlib.Path("docs", "queue_test.rst"))
    _delete_path(pathlib.Path("docs", "modules.rst"))
    subprocess.run("sphinx-apidoc -o docs/ src/queue_test", shell=True)
    make_cmd = "make.bat" if sys.platform in ["win32", "cygwin"] else "make"
    with _set_directory(pathlib.Path("docs")):
        subprocess.run(f"{make_cmd} clean", shell=True)
        subprocess.run(f"{make_cmd} html", shell=True)
    _open_browser("docs/_build/html/index.html")


@app.command(help="install the package to the active Python's site-packages")
def install():
    clean()
    subprocess.run("pip install .", shell=True)

if __name__ == "__main__":
    app()
