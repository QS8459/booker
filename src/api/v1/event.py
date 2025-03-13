from fastapi import (
    APIRouter,
    Depends,
    Query,
    status
)
from src.core.service.event import (
    EventService,
    get_event_service
)
from src.core.schema.event import (
    EventAddSchema,
    EventResponseSchema
)
from src.core.schema.response import ResponseBaseSchema
from src.core.service.auth import get_user
from uuid import UUID

event: APIRouter = APIRouter(
    prefix='/event',
    tags=["Event"]
)


@event.post(
    '/add/',
    status_code=status.HTTP_201_CREATED,
    response_model=EventResponseSchema
)
async def add_event(
        data: EventAddSchema,
        service: EventService = Depends(get_event_service),
        token=Depends(get_user)
):
    return await service.add(account_id=token.id, **data.dict())


@event.post(
    '/list/',
    status_code=status.HTTP_200_OK,
    response_model=ResponseBaseSchema
)
async def get_events(
        page: int = Query(...),
        page_size: int = Query(...),
        service: EventService = Depends(get_event_service),
        token=Depends(get_user)
):
    count = await service.get_count()
    data_list = await service.get_all(
        offset=page-1,
        limit=page_size
    )
    return ResponseBaseSchema(
        count=count[0],
        result=data_list
    )


@event.get(
    '/{id}/',
    status_code=status.HTTP_200_OK,
    response_model=EventResponseSchema
)
async def get_event(
        _id: UUID,
        service: EventService = Depends(get_event_service),
        token = Depends(get_user)
):
    return await service.get_by_id(id=_id)


@event.patch(
    '/{id}/',
    status_code=status.HTTP_202_ACCEPTED,
    response_model=EventResponseSchema
)
async def update_event(
        data: EventAddSchema,
        service: EventService = Depends(get_event_service),
        token=Depends(get_user)
):
    return await service.update(**data.dict())

