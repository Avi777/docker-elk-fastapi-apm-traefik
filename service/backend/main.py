import logging

from elasticapm.contrib.starlette import ElasticAPM, make_apm_client
from fastapi import FastAPI
from logstash_async.handler import AsynchronousLogstashHandler

app = FastAPI()

# APM client
apm = make_apm_client(
    {"SERVICE_NAME": "fastapi-apm-test", "SERVER_URL": "http://apm-server:8200"}
)
app.add_middleware(ElasticAPM, client=apm)


# logger: logstash
host = "35.84.146.99"
port = 5000

logger = logging.getLogger("fastapi-logstash-logger")
logger.setLevel(logging.DEBUG)
async_handler = AsynchronousLogstashHandler(host, port, database_path=None)
logger.addHandler(async_handler)


@app.get("/")
async def index():
    logger.info("Endpoint: Index")
    return {"app": "APM Demo"}


@app.get("/health")
async def health():
    logger.info("Endpoint: Health")
    return {"health": "OK!"}
