# tarsd-final

## Monitoramento VMs e Containers

***Para acessar métricas dos containers:***
```
curl -i -G 'http://192.168.33.11:8086/query?db=containers&pretty=true' --data-urlencode  'q=SELECT * FROM "container:<measurements>"'
```
  - Measurements podem ser obtidos com:
```
curl -G 'http://192.168.33.11:8086/query?db=containers&pretty=true' --data-urlencode  "q=SHOW MEASUREMENTS on containers"
```
***Para acessar métricas das vms:***
```
curl -i -G 'http://192.168.33.11:8086/query?db=vms&pretty=true' --data-urlencode  'q=SELECT * FROM "vm:<measurements>"'
```
  - Measurements podem ser obtidos com:
```
curl -G 'http://192.168.33.11:8086/query?db=vms&pretty=true' --data-urlencode  "q=SHOW MEASUREMENTS on vms"
```
