# Assignment 11

This project is a Flask API with Docker integration, allowing you to run and test various endpoints using a CLI shell.

## Prerequisites

- Docker: Ensure that Docker is installed on your machine or server.

## Getting Started

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/Chaddnius/Assignment-11.git
   cd my-api-project

**Build and Run Docker Containers:** 
docker-compose up -d

**Stop and remove Docker Containers**
docker-compose down 

Run the CLI shell interactively:

Copy code
python my_api_cli.py
Example commands in the CLI shell:

Copy code
md5 hello
factorial 5
fibonacci 8
is-prime 13
slack-alert "Hello, world!"
keyval-create my_key my_value
keyval-read my_key
keyval-update my_key new_value
keyval-delete my_key