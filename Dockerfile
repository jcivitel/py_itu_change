FROM python:3.12-alpine AS builder

RUN apk add --no-cache libgcc mariadb-connector-c pkgconf mariadb-dev \
    postgresql-dev

WORKDIR /opt/py_itu_change/
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

COPY . /opt/py_itu_change/

FROM builder AS install
WORKDIR /opt/py_itu_change
ENV VIRTUAL_ENV=/opt/py_itu_change/venv

RUN python -m venv $VIRTUAL_ENV

ENV PATH="$VIRTUAL_ENV/bin:$PATH"

RUN pip install --no-cache-dir -r /opt/py_itu_change/requirements.txt

FROM install

ENV FILTER_DATE="2025-01-01"

CMD ["sh", "-c", "python py_itu_change.py $FILTER_DATE"]