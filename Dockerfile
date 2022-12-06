# Nelson Dane

# Build from alpine to keep the image small
FROM alpine:latest
# Set default timezone
ENV TZ=America/New_York

# Install python, pip, and tzdata
RUN apk add --no-cache py3-pip tzdata

# Grab dependencies
WORKDIR /app
COPY ./requirements.txt .

# Install dependencies
RUN pip install -r requirements.txt

# Get needed files
COPY ./replies.py .
COPY ./cashapp.py .

CMD ["python3","cashapp.py"]

