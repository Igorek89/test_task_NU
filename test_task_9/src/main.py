from fastapi import FastAPI
from fastapi.responses import ORJSONResponse
from src.api.v1.router import router
from src.config.config import settings


app = FastAPI(
    title=settings.app.name,
    docs_url='/api/v1/openapi',
    openapi_url='/api/v1/openapi.json',
    default_response_class=ORJSONResponse,
)

app.include_router(router)



# app.add_exception_handler(AuthJWTException, authjwt_exception_handler)
