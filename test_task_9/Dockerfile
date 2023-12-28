FROM python:3.10

ENV WORKDIR /opt/app/
ENV USER bank_system

WORKDIR $WORKDIR

RUN apt-get update && apt-get install -y netcat-traditional

COPY requirements.txt requirements.txt

RUN pip install --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

COPY . .

RUN groupadd -r $USER && \
    useradd -d $WORKDIR -r -g $USER $USER && \
    chown $USER:$USER -R $WORKDIR && \
    chmod +x docker-entrypoint.sh

USER $USER

ENTRYPOINT ["sh", "-c", "./docker-entrypoint.sh"]
