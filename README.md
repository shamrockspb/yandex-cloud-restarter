# Yandex Cloud Restarter

Service for restarting Yandex Cloud compute instances.

Very basic python script checks if virtual machines from input list are working, and if not - starts them. Running as cron job, packed in Docker container.

List of possible statuses
- RUNNING
- STOPPING
- STOPPED
- STARTING

Script tries to start VM instance only if it is in STOPPED status. All other statuses are ignored.

## Usage

Set environment variables:
YCR_CRON
YCR_HOSTS


docker-compose up -d

Get status:
yc compute instance get shamrock-project-web | grep status

Start:
yc compute instance start shamrock-project-web

Stop:
yc compute instance stop shamrock-project-web



Statuses
- RUNNING
- STOPPING
- STOPPED
- STARTING


$YCR_CRON python /app/src/Main.py $YCR_HOSTS >> /var/log/cron.log 2>&1


docker-compose build --build-arg YCR_CRON="* * * * *" --build-arg YCR_HOSTS="instance1 instance2"


docker-compose up -d

docker-compose exec cron /root/yandex-cloud/bin/yc init



https://cloud.yandex.ru/docs/cli/operations/profile/profile-create

* Настроить передачу параметров из docker-compose



