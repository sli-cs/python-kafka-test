# python-kafka-test
testing python kafka tool


## manual testing

### create topic with some partitions
```bash
$ docker-compose up
$ docker exec -it pythonkafkatest_kafka_1 bash

kafka@b72643a2d740:~$ JMX_PORT=9998 kafka-topics.sh --zookeeper=zookeeper:2181 --create --topic scores --partitions 20 --replication-factor 1

```

### run the producer
```
$ docker-compose run --rm producer bash
root@f57fe7b173f8:/code# python kafka_producer.py --brokers kafka:9092 --topic scores -n 20
```

### check offsets
```
$ JMX_PORT=9988 bin/kafka-run-class.sh kafka.tools.GetOffsetShell --broker-list localhost:9092 --topic scores

$ ./bin/kafka-consumer-groups.sh --bootstrap-server localhost:9092 --group count_errors --describe

```
