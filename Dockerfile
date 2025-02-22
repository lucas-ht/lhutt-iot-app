FROM python:3.12-slim AS builder
WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir --upgrade -r requirements.txt

FROM gcr.io/distroless/python3
WORKDIR /app

COPY --from=builder /usr/local /usr/local
COPY . .

ENTRYPOINT [ "python", "main.py" ]

LABEL org.opencontainers.image.title="iot-app"                                          \
      org.opencontainers.image.source="https://github.com/lucas-ht/lhutt-iot-app"       \
      org.opencontainers.image.description="Test application for Inception of Things"   \
                                                                                        \
      org.opencontainers.image.authors="lucas-ht"
