# We're using Ubuntu 20.10
FROM mrismanaziz/userbot-man:latest

#
# Clone repo and prepare working directory
#
RUN git clone -b alpha https://github.com/mrismanaziz/Man-Userbot/tree/alpha /root/userbot
RUN mkdir /root/userbot/.bin
RUN pip install --upgrade pip setuptools
WORKDIR /root/userbot

#Install python requirements
RUN pip3 install -r https://raw.githubusercontent.com/mrismanaziz/Man-Userbot/alpha/requirements.txt

CMD ["python3","-m","userbot"]
