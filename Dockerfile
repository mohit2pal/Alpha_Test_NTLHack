FROM python:3.9-slim-bullseye

ADD . /alpha

WORKDIR /alpha

RUN apt-get update
RUN apt-get install ffmpeg libsm6 libxext6  -y
RUN apt-get install tesseract-ocr-all -y
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
ENV TZ=Asia/Kolkata
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone

ENTRYPOINT ["python", "server.py"]
