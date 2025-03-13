from fastapi import (
    Request,
    Response,
    status
)
from fastapi.responses import JSONResponse
from src.conf.log import logger


async def log(request: Request, call_next):
    try:
        logger.debug("Middleware")
        response = await call_next(request)
    except Exception as e:
        logger.error(f"Exception happened while handling request \n{e}")
        return JSONResponse(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            content={
                "detail": "Something Went Wrong"
            }
        )
    return response
