import threading

import uvicorn
from fastapi import FastAPI
from fastapi.responses import ORJSONResponse

from src.api.orders import router as orders_router
from src.api.users import router as users_router
from src.core.config import queue_config, settings
from src.queue.consumer import consumer


def create_app():
    app = FastAPI(
        title=settings.app_title,
        docs_url="/docs",
        openapi_url="/docs.json",
        default_response_class=ORJSONResponse,
    )
    app.include_router(orders_router)
    app.include_router(users_router)
    return app


app = create_app()

consumer_threads = []
for queue_name in queue_config.__dict__.values():
    consumer_thread = threading.Thread(target=consumer, args=(queue_name,))
    consumer_threads.append(consumer_thread)

for consumer_thread in consumer_threads:
    consumer_thread.start()


if __name__ == "__main__":
    uvicorn.run(
        "main:app",
        host=settings.app_host,
        port=settings.app_port,
        log_level=settings.app_log_level,
    )
