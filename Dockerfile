FROM python:3-alpine

LABEL maintainer="stevenskeard@gmail.com"
LABEL name="TwitterMusicBot"
LABEL description=""
LABEL url="https://github.com/stevenskeard/twittermusicbot"

WORKDIR /usr/src/app

COPY src ./
RUN pip install --no-cache-dir -r required-modules.txt
CMD ["python", "./Controller.py"]
