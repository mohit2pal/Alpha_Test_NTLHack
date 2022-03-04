FROM python:3.9-slim-bullseye

ADD . /alpha

WORKDIR /alpha

RUN pip install --upgrade pip
RUN pip install -r requirements.txt
RUN apt install tesseract-ocr-all -y
ENV TZ=Asia/Kolkata
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone

ENTRYPOINT ["python", "server.py"]
