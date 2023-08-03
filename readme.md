### to run the kafka enviornment
docker-compose up -d
### to run the django app
cd myproject
python manage.py runserver 
### to run the kafka 
docker-compose exec kafka bash 
### to see the kafka topics
kafka-topics --bootstrap-server localhost:9092 --list 
### to see all the contents
kafka-console-consumer --bootstrap-server localhost:9092 --topic my_topic --from-beginning 
