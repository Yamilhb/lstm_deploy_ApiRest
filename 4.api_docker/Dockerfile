# syntax=docker/dockerfile:1
# Esta es la versión de Dockerfile

FROM python:3.9.16

# Create a non-privileged user that the app will run under.
# See https://docs.docker.com/develop/develop-images/dockerfile_best-practices/#user
ARG UID=10001
RUN adduser \
    --disabled-password \
    --gecos "" \
    --home "/nonexistent" \
    --shell "/sbin/nologin" \
    --no-create-home \
    --uid "${UID}" \
    lstm-user

WORKDIR /opt/3.api

# Install requirements, including from Gemfury
ADD ./3.api /opt/3.api
RUN pip install --upgrade pip
#RUN --mount=type=cache,target=/root/.cache/pip \
#    --mount=type=bind,source=./3.api/requirements.txt,target=/opt/3.api/requirements.txt \
RUN pip install -r /opt/3.api/requirements.txt

RUN chmod +x /opt/3.api/run.sh
RUN chown -R lstm-user:lstm-user /opt/3.api

USER lstm-user

EXPOSE 8005

CMD ["bash", "./run.sh"]

