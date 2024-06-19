FROM alpine as base
ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1 \
    LITESTAR_HOST=0.0.0.0 \
    VIRTUAL_ENV=/opt/venv \
    PATH="/opt/venv/bin:$PATH"

WORKDIR /app

RUN apk update && \
    apk upgrade && \
    apk add --no-cache python3

FROM base as builder

ADD --chmod=755 https://astral.sh/uv/install.sh /install.sh
RUN /install.sh && rm /install.sh

COPY ./pyproject.toml ./requirements.txt ./
RUN /root/.cargo/bin/uv venv /opt/venv && \
    /root/.cargo/bin/uv pip install --no-cache -r requirements.txt

FROM base as app

COPY --from=builder /opt/venv /opt/venv

COPY . .

EXPOSE 8000

CMD litestar run
