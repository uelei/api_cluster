[![CircleCI](https://circleci.com/gh/uelei/api_cluster.svg?style=svg)](https://circleci.com/gh/uelei/api_cluster) [![Codacy Badge](https://api.codacy.com/project/badge/Grade/3cdc4e77e106428199370c83999d1e1a)](https://www.codacy.com/app/uelei/api_cluster?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=uelei/api_cluster&amp;utm_campaign=Badge_Grade)
# api_cluster


## Usage


The API has two main Resorces


### To Insert new record


send a POST request to endpoint **/upload** with the data to be stored as curl below

```bash
 curl --data 'Device: ID=1; Fw=16071801; Evt=2; Alarms: CoilRevesed=OFF; Power: Active=1862W; Reactive=279var; Appearent=403VA; Line: Current=7.77400017; Voltage=230.08V; Phase=-43,841rad; Peaks: 7.71500015;7.71500015;7.75500011;7.70200014;7.70800018;7.70200014;7.77400017;7.73500013;7.77400017;7.77400017; FFT Re: 10659;679;-396;-217;1029;-13;884;-39;594; FFT Img: -59;-112;-831;39;838;19;297;39;462; UTC Time: 2016-10-4 16:47:50; hz: 49.87; WiFi Strength: -62; Dummy: 20' localhost:5000/upload
```

### To Get Information about the clusters
send a GET request to endpoint **/upload**
```bash
curl localhost:5000/upload
```

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