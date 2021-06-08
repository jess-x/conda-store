from conda_store_server.celery import app


@app.task(
    max_retries=5,
)
def task_build_conda_environment(message="World"):
    pass


@app.task
def task_delete_conda_environment(build_id):
    pass
