FROM python:3.15

RUN adduser bbs
USER bbs

WORKDIR /home/bbs

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY bbs bbs

ENTRYPOINT [ "python3", "-m", "bbs" ]