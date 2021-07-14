FROM python


RUN python3 -m pip install -U pip

RUN pip install azure-storage-blob

ARG DEBIAN_FRONTEND=noninteractive
ENV TZ=America/Bogota

RUN apt-get update \
    && apt-get install -y python3-tk \        
    && apt-get autoremove \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*



WORKDIR /var/www
