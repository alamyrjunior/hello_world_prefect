from prefect import flow, task

@task
def say_hello():
    print("Hello, Prefect!")

@flow(log_prints=True)
def hello():
    print("funcionaaaaaaaaaa")
    say_hello()

