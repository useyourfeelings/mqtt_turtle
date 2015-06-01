# mqtt_turtle
a python mqtt benchmark tool

###install:
sudo apt-get install libev-dev
python3 setup.py build
sudo python3 setup.py install

###usage:
The sender will keep creating mqtt clients according to your settings.
Each client will send a message to the host periodically until they complete the whole task.
Please provide different ids with -n if you are running multiple instances of this program.
When all senders finish, give the receiver some ctrl-c to see the result.

###options:
receiver:
    --help
    -h xxx.xxx.xxx.xxx  host
    -p number           port

sender:
    --help
    -h xxx.xxx.xxx.xxx  host
    -p number           port
    -c number           total clients to create
    -m number           total messages to send
    -i number           messages sending interval(seconds)(defaut 10)
    -n mqtt-turtle      client id prefix(default "mqtt-turtle")
    -M goodbye world!   message content(default "mqtt-turtle message")
    -q 0, 1 or 2        message qos(default 0)
    -I number           clients creation interval(seconds)(defaut 3)
    -k number           keep alive(seconds)(default 60)
    -P number           clients to create per round(default 50)
    -t topic            topic(default "mqtt-turtle-topic")

###example:
####1.make a message receiver
mqtt_turtle_receiver -h xxx.xxx.xxx.xxx

####2.make one or more sender
mqtt_turtle_sender -h xxx.xxx.xxx.xxx -c 6000 -m 60000 -n you -t you -i 7 -P 100 -M it's you
mqtt_turtle_sender -h xxx.xxx.xxx.xxx -c 6000 -m 60000 -n me -t me -i 7 -P 100 -M it's me
mqtt_turtle_sender -h xxx.xxx.xxx.xxx -c 6000 -m 60000 -n her -t her -i 7 -P 100 -M it's her