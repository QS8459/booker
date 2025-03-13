from fastapi import (
    APIRouter,
    Depends,
    Query,
    status
)
from src.core.service.stadium import (
    StadiumService,
    get_stadium_service
)
from src.core.service.auth import get_user
from src.core.schema.stadium import (
    StadiumAddSchema,
    StadiumResponseSchema
)
from src.core.schema.response import ResponseBaseSchema
from src.conf.log import logger

stadium: APIRouter = APIRouter(prefix="/stadium", tags=['Staduim'])


@stadium.get('/', status_code=status.HTTP_200_OK)
async def stadium_home(
        service: StadiumService = Depends(get_stadium_service)
):
    return "Hello From the staduim"


@stadium.post(
    '/add/',
    status_code=status.HTTP_201_CREATED,
    response_model= StadiumResponseSchema
)
async def add_stadium(
        data: StadiumAddSchema,
        service: StadiumService = Depends(get_stadium_service),
        token=Depends(get_user)
):
    return await service.add(owner_id=token.id, **data.dict())


@stadium.get(
    '/list/',
    status_code=status.HTTP_200_OK,
    response_model=ResponseBaseSchema
)
async def stadiums(
        u_lat: float = Query(...),
        u_long: float = Query(...),
        page: int = Query(...),
        page_size: int = Query(...),
        service: StadiumService = Depends(get_stadium_service)
):
    count = await service.get_count()
    data_list = await service.get_by_distance(
        u_lat=u_lat,
        u_long=u_long,
        page=page,
        page_size=page_size
    )

    return ResponseBaseSchema[StadiumResponseSchema](
        count=count[0],
        result=data_list
    )

# @stadium.put(
#     '/book/',
#     status_code=status.HTTP_200_OK,
# )
# async def book(
#         data:
# )