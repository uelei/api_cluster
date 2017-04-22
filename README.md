[![CircleCI](https://circleci.com/gh/uelei/api_cluster.svg?style=svg)](https://circleci.com/gh/uelei/api_cluster)
# api_cluster

## Pre Install
The API was build using ubuntu 16.10 and python version 3.5.2


## Install

All dependencies are on requirements.txt to install just Run

```bash
pip install -r requirements.txt
```

## To run

```bash
python run.py
```


## To populate some data
I made a script to populate some data do the API, all content of the file events.txt will be send to a API using requests from python

```bash
python populate.py
```


## Tests

The tests were done using pytest. To run just execute code below

 ```bash
 pytest -v tests
 ```