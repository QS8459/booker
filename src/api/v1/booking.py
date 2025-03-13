from fastapi import (
    APIRouter,
    Depends,
    status
)
from src.core.service.booking import (
    BookingService,
    get_booking_service
)

booking: APIRouter = APIRouter(
    prefix='/booking',
    tags=["Event"]
)

