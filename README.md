# python-rent-processor



## How to setup DEV environment?
- Go to the folder where you would like to keep code and clone repo from GITHUB
and checkout the project
```
cd {your_code_directory}
git clone https://github.com/TaQba/python-rent-processor.git
cd python-rent-processor
```
- First time, build docker composer (first build or rebuild only)
```
$ docker-compose up --build
```
- Next time
```
$ docker-compose up
``` 


## How to go container?
- Go to the folder where you would like to keep code and clone repo from  GITHUB
```
cd {your_code_directory}/python-rent-processor
```
- Docker contain needs to be up and need to run some commands

```
docker ps
docker exec -it python-rent-processor bash
```
- No you should have the access to the container with Python 3.9 with some libs

## How to run Unit Test?
Unit tests are in folder /tests/*. There are only a few tests just for demo.
- Go to the container and run Shell command
```
./bin/run-single-test.sh 
```
or
```
# ./bin/run-tests.sh 
```
But this is unfinished. I haven't time to fix covaragerc :(

## How to run code check
Shell command
```
./bin/run-code-check.sh 
```


## Presentation
I had to do 4 tasks and I attached all of them in one py script /code/start.py
They can be run from one script 

```
python start.py 
```
