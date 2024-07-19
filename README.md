# NETLLMBENCH

This repository contains the source code for the NETLLMBENCH framework.


## Repository Structure

- `docker`: folder containing the docker-compose file for required Docker environment
- `statistics`: folder where the statistics will be collected by the framework
- `config.py`: the configuration file for the model names and the server where the model is hosted
- `prompts.py`: prompts for the used tasks in evaluation


## Quickstart

### Requirements

In order to reproduce our measurement results, a working Docker version 27.0.3 and Docker Compose version v2.28.1 is required.

### Running the framework

You can run `main.py` for evaluation.