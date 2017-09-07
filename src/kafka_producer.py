from pykafka import KafkaClient
import argparse
import json
import names
from random import randint
import datetime
import pytz

datetime_start = datetime.datetime(2017, 9, 1, tzinfo=pytz.utc)
datetime_end = datetime.datetime(2017, 9, 5, tzinfo=pytz.utc)

datetime_start_epoch_ms = int(datetime_start.timestamp())
datetime_end_epoch_ms = int(datetime_end.timestamp())

def generateRandomTS():
    return randint(datetime_start_epoch_ms, datetime_end_epoch_ms)

def generateScore():
    return {'username': names.get_first_name(), 'score':randint(1, 1000), 'ts': generateRandomTS()}


def main():
    parser = argparse.ArgumentParser()

    parser.add_argument('--brokers', required=True, help="the bootstrap_servers")

    parser.add_argument('--topic', required=True, help="kafka topic to push messages")

    parser.add_argument('-n', required=True, type=int, help="the number of messages to push")

    args = parser.parse_args()

    topicName = args.topic
    numMessages = args.n
    brokers = args.brokers

    print("brokers: {}, topicName: {}, {}".format(brokers, topicName, numMessages))

    client = KafkaClient(hosts=brokers)
    topic = client.topics[topicName.encode('utf-8')]
    with topic.get_sync_producer() as producer:
        for i in range(numMessages):
            score = generateScore()
            print("{} : {}".format(i, score))
            kafka_msg = producer.produce(json.dumps(score).encode('utf-8'), partition_key=score['username'][0].encode('utf-8'))

if __name__ == '__main__':
    main()