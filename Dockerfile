FROM python:3.9-slim

# setup directory for application
WORKDIR /app

# to keep docker cache on this layer we only copy requirements.txt
# then install dependecies
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

# copy source code
ADD . /app

EXPOSE 5000
CMD ["flask", "run"]