ARG BUILD_FROM
FROM $BUILD_FROM

# Install packages
RUN apt-get update && \
  apt-get install -y jq tzdata python3 python3-dev python3-pip python3-six python3-pyasn1 \
  libportaudio2 alsa-utils && apt-get clean -y && rm -rf /var/lib/apt/lists/*
RUN pip3 install --no-cache-dir --upgrade pip six google-assistant-library google-auth \
    requests_oauthlib cherrypy flask flask-jsonpify flask-restful grpcio google-assistant-grpc \
    google-auth-oauthlib

# Copy data
COPY run.sh /
COPY *.py /

RUN chmod a+x /run.sh

ENTRYPOINT [ "/run.sh" ]
