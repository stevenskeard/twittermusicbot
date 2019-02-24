# Use the public python alpine image for simplicity
FROM python:3-alpine

# Setup a few simple labels
LABEL maintainer="stevenskeard@gmail.com"
LABEL name="TwitterMusicBot"
LABEL description="Python based bot that monitors for a certain hashtag and parses the tweet to try to find a matching video on Youtube"
LABEL url="https://github.com/stevenskeard/twittermusicbot"

# Specify our working directory explicity
WORKDIR /usr/src/app

# Copy the python scripts
COPY src ./

# Install the required modules
RUN pip install --no-cache-dir -r required-modules.txt

# Install audio player
RUN apk add mpg123

#Configure the audio
RUN apk add alsa-utils alsa-utils-doc alsa-lib alsaconf openrc
RUN sed -e "s/audio:x:18:/audio:x:18:root/" /etc/group > /tmp/tmp-alsa-setup && mv /tmp/tmp-alsa-setup /etc/group
RUN echo "defaults.ctl.card 1\ndefaults.pcm.card 1" >> /usr/share/alsa/alsa.conf

# Start the main script
CMD ["python", "-u", "Controller.py"]
