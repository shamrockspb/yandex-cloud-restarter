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

### Build using docker-compose. Two mandatory parameters should be provided:

 - YCR_CRON - crontab
 - YCR_HOSTS - list of instances separated by space

```docker-compose build --build-arg YCR_CRON="* * * * *" --build-arg YCR_HOSTS="instance1 instance2"```

### Start container

```docker-compose up -d```

### Connect to Yandex Cloud from inside container CLI()

```docker-compose exec yc-restarter /root/yandex-cloud/bin/yc init```


Oficial guide:

[Create Yandex Cloud CLI Profile](https://cloud.yandex.ru/docs/cli/operations/profile/profile-create)

