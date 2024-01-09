# Client-server

## Prerequisites

- Python installed
- Docker installed

## Getting Started

Clone the repository: ```git clone https://github.com/zvierievkp31ms/labs-pogorelov.git```

## Use app

-> Use **development** branch

### Run Without Docker
1. Install dependencies: ```pip install -U Flask``` **OR** ```pip install -r requirements.txt```
2. Run the Python script: ```python app.py```

### Run With Docker
1. Build the Docker image: ```./build.sh```
2. Run the Docker container: ```./run.sh```

## Testing app

-> Use **testing** branch
1. Install dependencies: ```pip install -U Flask``` **OR** ```pip install -r requirements.txt```
2. Run the Python scripts: ```./test.sh```
