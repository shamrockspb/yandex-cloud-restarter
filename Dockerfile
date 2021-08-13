FROM python:3.9.5-slim
ARG YCR_CRON
ARG YCR_HOSTS
ENV YCR_CRON=$YCR_CRON
ENV YCR_HOSTS=$YCR_HOSTS



# set work directory
WORKDIR /app

# install dependencies
COPY requirements.txt .
RUN pip install -r requirements.txt

# copy project
COPY . .

RUN apt-get update && apt-get -y install cron && apt-get -y install curl && apt-get -y install gettext-base

RUN curl https://storage.yandexcloud.net/yandexcloud-yc/install.sh | bash



# Copy hello-cron file to the cron.d directory
COPY cron-ycr /tmp/cron-ycr
RUN envsubst < /tmp/cron-ycr 
RUN envsubst < /tmp/cron-ycr > /etc/cron.d/cron-ycr

# Give execution rights on the cron job
RUN chmod 0644 /etc/cron.d/cron-ycr

# Apply cron job
RUN cat /etc/cron.d/cron-ycr
RUN crontab /etc/cron.d/cron-ycr

# Create the log file to be able to run tail
RUN touch /var/log/cron.log

# Run the command on container startup
CMD cron && tail -f /var/log/cron.log

