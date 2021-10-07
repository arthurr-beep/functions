# Backend Programming Task

A Sample Code that Implements fibonacci, factorial and ackerman functions.

## EndPoints

| route                                          | response | verb |
| ---------------------------------------------- | -------- | ---- |
| /functions/fibonacci/number                    | int      | GET  |
| /functions/factorial/number                    | int      | GET  |
| /functions/ackerman/first_number/second_number | int      | GET  |

## Tech Stack Used

- Python
- Flask
- Docker
- Redis
- Nginx
- Prometheus
- Prometheus/StatsD-Exporter

## Requirements

- Docker Installed
- Python >=3.6

## Running The Application

```
$ docker-compose -f docker-compose-dev.yml build

$ docker-compose -f docker-compose-dev.yml up -d
```

## Testing the Endpoints

```
grab the docker container IP:81 and test out the endpoints

```

## Running Unit Tests

```
$ docker-compose -f docker-compose-dev.yml run functions python manage.py test
```

## Checking Promethues Metrics

```
navigate to docker-machine-ip:9090/graph

search with any of the exported tags
- request_latency_seconds
- request_count

docker-machine-ip:9090/targets #to see targets

```
