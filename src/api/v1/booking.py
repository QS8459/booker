from fastapi import (
    APIRouter,
    Depends,
    Query,
    status
)
from src.core.service.booking import (
    BookingService,
    get_booking_service
)
from src.core.schema.booking import (
    BookingAddSchema,
    BookingResponseSchema
)
from src.core.schema.response import ResponseBaseSchema
from src.core.service.auth import get_user

booking: APIRouter = APIRouter(
    prefix='/booking',
    tags=["Booking"]
)


@booking.post(
    '/',
    status_code=status.HTTP_201_CREATED,
    response_model=BookingResponseSchema
)
async def add_booking(
        data: BookingAddSchema,
        service: BookingService = Depends(get_booking_service),
        token=Depends(get_user)
):
    return await service.add(account_id=token.id, **data.dict())


@booking.get(
    '/list/',
    status_code=status.HTTP_200_OK,
    response_model=ResponseBaseSchema
)
async def book_list(
        page: int = Query(...),
        page_size: int = Query(...),
        service: BookingService = Depends(get_booking_service),
        token=Depends(get_user)
):
    count = await service.get_count()
    data_list = await service.get_all(offset=page-1, limit=page_size)
    return ResponseBaseSchema[BookingResponseSchema](
        count=count[0],
        result=data_list
    )
