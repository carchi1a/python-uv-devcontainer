import pathlib
import subprocess
from os import getenv

import pytest
import testinfra

IMAGE_NAME = getenv("IMAGE_NAME", "")

# scope='session' uses the same container for all the tests;
# scope='function' uses a new container per test function.
@pytest.fixture(scope="session")
def host(request):
    # run a container
    docker_id = (
        subprocess.check_output(
            [
                "docker",
                "run",
                "-d",
                "-i",
                IMAGE_NAME,
            ]
        )
        .decode()
        .strip()
    )
    # return a testinfra connection to the container
    yield testinfra.get_host("docker://" + docker_id)
    # at the end of the test suite, destroy the container
    subprocess.check_call(["docker", "rm", "-f", docker_id])