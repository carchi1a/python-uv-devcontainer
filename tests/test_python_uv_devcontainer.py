from os import getenv

PYTHON_VERSION = getenv("PYTHON_VERSION", "")


def test_uv_version(host) -> None:
    assert "0.7.19" in host.check_output("uv --version")


def test_python_version(host) -> None:
    assert PYTHON_VERSION in host.check_output("python --version")


def test_venv_location(host) -> None:
    result = host.run("echo $VENV_LOCATION").stdout
    assert "/opt/.venv" in result


def test_venv_in_path(host) -> None:
    result = host.run("echo $PATH").stdout
    assert "/opt/.venv" in result