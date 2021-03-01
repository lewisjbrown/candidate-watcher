# Candidate Watcher

## Quick Start

Build the Docker image from the project root directory:

```
docker build . -t candidate-watcher
```

Run the Docker container from the directory containing the file you want to watch, e.g. "test.txt"

```
docker run -it --rm -v "$(pwd):/app/data" candidate-watcher test.txt
```

The above command will watch the file $(pwd)/test.txt

The file test.txt need not exist when the application is started: it will watch in a 1 second polling loop for the file to be created.

If the file is deleted after the app has started, the app will again go into a 1 second polling loop.

The file can be modified in the usual ways, and a log message will be emitted. The one case where it doesn't work well is when the file is opened and saved with VIM, because VIM does a file swap. The Watchdog author suggests that VIM is reconfigured to not behave in this way. Otherwise, more development work would be needed to handle the VIM editor case.

## General Usage:

docker run -it --rm -v "<host_directory_to_watch>:/app/data" candidate-watcher <file_or_filepath_relative_to_host_directory>


## For development without using Docker (for ease of development)

Prerequisites: Python 3.8 

1. Create Python virtual environment

```
    python -m venv .venv
```

2. Activate the virtual environment
   
```
    source .venv/bin/activate
```

3. Install Python packages

```
    pip install -r requirements.txt
```

4. Create directory /app/data on the host directory (to simulate the /app/data directory in Docker)

5. Create a test file /app/data/test1

6. Run Python app

```
    python candidate_watcher/main.py test1
```