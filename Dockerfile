FROM python:3
WORKDIR /app
COPY ./finVizulizer ./finVizulizer
# install FreeTDS and dependencies
RUN apt-get update \
 && apt-get install unixodbc -y \
 && apt-get install unixodbc-dev -y \
 && apt-get install freetds-dev -y \
 && apt-get install freetds-bin -y \
 && apt-get install tdsodbc -y \
 && apt-get install --reinstall build-essential -y
# populate "ocbcinst.ini" as this is where ODBC driver config sits
RUN echo "[FreeTDS]\n\
Description = FreeTDS Driver\n\
Driver = /usr/lib/x86_64-linux-gnu/odbc/libtdsodbc.so\n\
Setup = /usr/lib/x86_64-linux-gnu/odbc/libtdsS.so" >> /etc/odbcinst.ini
#Pip command without proxy setting
RUN pip3 install poetry

#Use this one if you have proxy setting
COPY pyproject.toml ./
RUN poetry config virtualenvs.create false
RUN poetry install --no-dev

# CMD ["ls", "-all", "finVizulizer"]
CMD ["python3", "finVizulizer/main.py"]