FROM python:3-alpine

LABEL maintainer="stevenskeard@gmail.com"
LABEL name="TwitterMusicBot"
LABEL description="Python based bot that monitors for a certain hashtag and parses the tweet to try to find a matching video on Youtube "
LABEL url="https://github.com/stevenskeard/twittermusicbot"

WORKDIR /usr/src/app

COPY src ./
RUN pip install --no-cache-dir -r required-modules.txt
CMD ["python", "./Controller.py"]
