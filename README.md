# NodeRGB Realtime Client

This repository contains:
* A REST API implemented using python3 and flask to manage and run one out of a selection of python scripts
* An easy to use python API that interfaces with (nodergb-server)[https://github.com/cedrichaase/nodergb-server]
* Scripts that are managed by the REST API and use the nodergb-server API

## Features

### REST API

* GET names of available scripts
* start/stop scripts by name
* GET the name of the script that is currently running, if any


### NodeRGB-server API

* setting a color
* transitioning between colors
* cycling between colors


### Scripts

* A realtime screengrabber, resulting in functionality comparable to `ambilight` by Philips
* Demo scripts
