FROM ubuntu


RUN apt -qq -y update \
	&& apt -qq -y upgrade
RUN apt -y install python3
RUN apt -y install python3-pip

WORKDIR /usr/src/app
COPY requirements.txt .
RUN pip3 install -r requirements.txt
COPY . .

ENV FLASK_APP=App.py

RUN python3 -m flask run --host=127.0.0.1 &
RUN python3 test.py
RUN pkill python3 -m flask run --host=0.0.0.0

EXPOSE 5000

CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0"]
