FROM python:3
USER root

RUN apt-get update
RUN apt-get -y install locales && \
    localedef -f UTF-8 -i ja_JP ja_JP.UTF-8
ENV LANG ja_JP.UTF-8
ENV LANGUAGE ja_JP:ja
ENV LC_ALL ja_JP.UTF-8
ENV TX JST-9
ENV TERM xterm

WORKDIR /app
ADD ./discord_bot /app

RUN apt-get install -y vim less
RUN pip install --upgrade pip
RUN pip install --upgrade setuptools
RUN pip install discord.py[voice]
RUN pip install python-dotenv
RUN apt update
RUN apt install -y ffmpeg

CMD python /app/call.py