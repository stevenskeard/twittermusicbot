FROM python:3-alpine

LABEL maintainer="stevenskeard@gmail.com"
LABEL name="TwitterMusicBot"
LABEL description="Python based bot that monitors for a certain hashtag and parses the tweet to try to find a matching video on Youtube "
LABEL url="https://github.com/stevenskeard/twittermusicbot"

WORKDIR /usr/src/app

COPY src ./
RUN pip install --no-cache-dir -r required-modules.txt
RUN apk add alsa-utils alsa-utils-doc alsa-lib alsaconf
RUN sed -e "s/audio:x:18:/audio:x:18:root/" /etc/group > /tmp/tmp-alsa-setup && mv /tmp/tmp-alsa-setup /etc/group
RUN echo "defaults.ctl.card 1\ndefaults.pcm.card 1" >> /usr/share/alsa/alsa.conf
RUN rc-service alsa start && rc-update add alsa
CMD ["python", "./Controller.py"]
