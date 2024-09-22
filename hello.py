from prefect import flow, task

@task
def say_hello():
    print("Hello, Prefect!")

@flow(log_prints=True)
def hello():
    say_hello()

if __name__ == '__main__':
    hello()
