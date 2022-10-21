<div align="center">

![image](https://user-images.githubusercontent.com/75628046/196457254-08f40047-2a69-49b6-bb61-a7203645c9a0.png) 
</div>
<div align="center">
  <p><h1>Observability Lab</p> 
<p align="center"> 📊 Lab com conceitos simples de observabilidade</p>

<h2> 🛠 Rodar a aplicação

```bash
# Clone este repositório
$ git clone <https://github.com/srebrasil/observability_lab.git>

# Acesse a pasta no terminal/cmd
$ cd observability_lab

# Assumindo que o docker já está instalado, instale o plugin para o Loki
$ docker plugin install grafana/loki-docker-driver:latest --alias loki --grant-all-permissions

# Execute a aplicação
$ docker-compose --profile all up

# Os endereços das aplicações no próximo tópico 
```
<h2> 🛠 Endereços das Aplicações

[Frontend](http://localhost:4000/api/v1/frontend) | 
[Fast Backend ](http://localhost:4001/api/v1/calc/sum/1/2) |
[Medium Backend ](http://localhost:4002/api/v1/calc/sum/1/2) |
[Slow Backend ](http://localhost:4003/api/v1/calc/sum/1/2)
<br>
<h2> 🛠 Endereços de Observability

[Prometheus](http://localhost:9090/) |
[Jaeger](http://localhost:16686/) |
[Grafana](http://localhost:3000/)
<br>

<p> 🔒 Senha do Grafana
<br>

`
user: admin | 
password: admin
`
<br>

<h2> 🛠 Tecnologias

[Docker](https://www.docker.com/) | [Prometheus](https://prometheus.io/) | [Jaeger](https://www.jaegertracing.io/) | [Python](https://www.python.org/) | [Grafana](https://grafana.com/) | [OpenTelemetry](https://opentelemetry.io/) | [Loki](https://grafana.com/oss/loki/)

<br>

  <h2>Contribuições de:</h2>
<div>
<a href="https://github.com/srebrasil/observability_lab/graphs/contributors">
  <img src="https://contrib.rocks/image?repo=srebrasil/observability_lab" />
</a>
  </div>

Lista de contribuições montada por [contrib.rocks](https://contrib.rocks).

</div>
