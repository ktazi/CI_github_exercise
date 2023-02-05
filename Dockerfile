FROM ubuntu


RUN apt -qq -y update \
	&& apt -qq -y upgrade
RUN apt -y install python3.7
RUN apt -y install python3-pip

RUN which python3.7
RUN which pip3

RUN ln -s /usr/bin/python3.7 /usr/bin/python
RUN ln -s /usr/bin/pip3 /usr/bin/pip
RUN python --version
RUN which pip

WORKDIR /usr/src/app
COPY requirements.txt .
RUN pip3 install -r requirements.txt
COPY . .
EXPOSE 5000
CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0"]
