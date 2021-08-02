# APM Server for fastAPI

* `server` - Contains composition of ELK stack + Traefik proxy
* `service` - Contains fastAPI configured with APM-server

## Usage

### Server: In Remote server

1. Setup traefik configurations

```yml
# server/traefik/traefik.yml
http:
  routers:
    es-router:
      rule: "Host(`es.example.com`)"
      entryPoints: es
      service: elasticsearch
    # add tls middleware
```

2. Run 

```shell
docker-compose up -d
```

### Service: Locally or in application server

1. Configure `main.py` with APM client and logstash configs

2. Run 

```
docker-compose up -d
```

## Load Testing

```shell
boom http://localhost:8000/ -c 100 -n 1000

boom http://localhost:8000/ -c 100 -d 10   

boom http://localhost:8000/health -c 10 -n 100 
```


## References

[1] [deviantony/docker-elk](https://github.com/deviantony/docker-elk)
[2] [elasticsearch-py/examples/fastapi-apm](https://github.com/elastic/elasticsearch-py/tree/master/examples/fastapi-apm)