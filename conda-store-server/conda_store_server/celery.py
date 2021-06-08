from celery import Celery

CELERY_TASK_LIST = [
    'conda_store_server.tasks',
]

app = Celery(
    'conda_store_server',
    backend='db+sqlite:///celery.sqlite',
    broker='sqla+sqlite:///celery.sqlite',
    include=CELERY_TASK_LIST,
)

if __name__ == "__main__":
    app.start()
