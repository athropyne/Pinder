from contextlib import asynccontextmanager

import loguru
from fastapi import FastAPI

app = FastAPI()


@asynccontextmanager
async def lifespan(_app: FastAPI):
    loguru.logger.info("application started")
    yield
    loguru.logger.info("application stopped")
