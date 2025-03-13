FROM python:3.11-alpine

WORKDIR /app

COPY . .

COPY requirements.txt /app

RUN pip install --no-cache -r  requirements.txt
ENV BK_APP_TITLE="BOOKER"
ENV BK_APP_VERSION="0.0.1"
ENV BK_APP_DESCRIPTION="BOOKER application for booking seats in the stadium"
ENV BK_SECRET_KEY="booker"
ENV BK_TOKEN_CRYPT_ALGORITHM="HS256"
ENV BK_TOKEN_EXP_TIME_MIN=30
ENV BK_DB_URL="sqlite+aiosqlite:///booker.db"
#RUN mkdir alembic
#RUN alembic init alembic

RUN chmod -x script.sh

#RUN #alembic revision --autogenerate -m "INIT" &&\
#    alembic upgrade head

EXPOSE 5000
