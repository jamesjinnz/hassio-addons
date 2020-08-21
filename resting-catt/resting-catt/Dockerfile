FROM arm32v7/python:3

WORKDIR /usr/src/app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 9898

CMD [ "python3", "resting-catt" ]
