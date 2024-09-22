from prefect import flow
from prefect.runner.storage import GitRepository



if __name__ == "__main__":
    flow.from_source(
        source=GitRepository(
        url="https://github.com/alamyrjunior/hello_world_prefect.git",
    ),
    entrypoint="hello.py:hello",
    ).deploy(
        name="github-deploy",
        work_pool_name="local",
        build=False
    )
