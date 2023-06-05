Steps to run on mac: 
    Prerequisite - Install Python and Java
    Install the following libraries
    transformers, tensorflow, tweepy, configparser, kafka, json
    To run the code through the terminal use below command
    python -u “path”



To setup Kafka run the following commands in terminal:
    cd kafka_2.13-3.1.0 
    Zookeeper: bin/zookeeper-server-start.sh config/zookeeper.properties
    bin/kafka-server-start.sh config/server.properties
    bin/kafka-topics.sh --create --topic assignment3 --bootstrap-server localhost:9092
    bin/kafka-console-producer.sh --topic assignment3 --bootstrap-server localhost:9092
    bin/kafka-console-consumer.sh --topic assignment3 --from-beginning --bootstrap-server localhost:9092


To setup ELK Stack download the following:
Elasticsearch - 7.8.0
Kibana - 7.8.0
Logstash - 8.1.2

Run the following commands in terminal:

In Elasticsearch folder: 
    cd elasticsearch-7.8.0
    bin/elasticsearch

In Kibana folder: 
    cd kibana-7.8.0-darwin-x86_64
    bin/kibana

In Logstash folder: 
Logstash requires .conf file to specify the input and the outputs below :

    input {
    kafka {
        bootstrap_servers => ["localhost:9092"]
        topics => ["assignment3"]
    }
    }

`    output {
    elasticsearch {
        hosts => ["localhost:9200"]
        index => "assignment3"
    }
    } `

    The .conf file must be placed in logstash directory

    cd logstash-8.1.2
    bin/logstash -f logstash-kafka.conf


Run the python file using command : python3 SentimentAnalysis.py
Arguments are configured in config.ini and is present in the same directory with "SentimentAnalysis.py"  
