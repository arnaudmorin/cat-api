FROM debian:trixie
RUN apt-get update && apt-get install -y python3-venv
COPY . /app/
RUN python3 -m venv /app/venv/
WORKDIR /app
RUN /app/venv/bin/pip install -r requirements.txt
EXPOSE 8080
ENTRYPOINT [ "/app/venv/bin/python3" ]
CMD [ "app.py" ]
