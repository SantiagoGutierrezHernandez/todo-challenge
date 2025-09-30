FROM python:3.13-slim

WORKDIR /mnt

COPY . /mnt
RUN pip install -r ./requirements.txt
RUN chmod +x ./bootstrap.sh

EXPOSE 8000
EXPOSE 3002

CMD ["/mnt/bootstrap.sh"]