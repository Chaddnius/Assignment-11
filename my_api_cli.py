import argparse
import requests

API_BASE_URL = "http://127.0.0.1:4000"  
def md5(text):
    url = f"{API_BASE_URL}/md5/{text}"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        print(f"Input: {data['input']}")
        print(f"MD5 Hash: {data['output']}")
    else:
        print(f"Error: {response.status_code} - {response.text}")

def factorial(num):
    url = f"{API_BASE_URL}/factorial/{num}"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        print(f"Input: {data['input']}")
        print(f"Factorial: {data['output']}")
    else:
        print(f"Error: {response.status_code} - {response.text}")

def fibonacci(num):
    url = f"{API_BASE_URL}/fibonacci/{num}"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        print(f"Input: {data['input']}")
        print(f"Fibonacci Sequence: {data['output']}")
    else:
        print(f"Error: {response.status_code} - {response.text}")

def is_prime(num):
    url = f"{API_BASE_URL}/is-prime/{num}"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        if data['is_prime']:
            print(f"{data['input']} is prime")
        else:
            print(f"{data['input']} is not prime")
    else:
        print(f"Error: {response.status_code} - {response.text}")

def slack_alert(message):
    url = f"{API_BASE_URL}/slack-alert/{message}"
    response = requests.post(url)
    if response.status_code == 200:
        data = response.json()
        if data["success"]:
            print(f"Message '{message}' sent successfully to Slack.")
        else:
            print("Failed to send message to Slack.")
    else:
        print(f"Error: {response.status_code} - {response.text}")

def keyval_create(storage_key, storage_val):
    url = f"{API_BASE_URL}/keyval"
    payload = {"storage-key": storage_key, "storage-val": storage_val}
    response = requests.post(url, json=payload)
    if response.status_code == 200:
        data = response.json()
        print(f"Command: {data['command']}")
        print(f"Result: {data['result']}")
        if not data['result']:
            print(f"Error: {data['error']}")
    else:
        print(f"Error: {response.status_code} - {response.text}")

def keyval_read(storage_key):
    url = f"{API_BASE_URL}/keyval/{storage_key}"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        print(f"Command: {data['command']}")
        if data['result']:
            print(f"Value for {data['storage-key']}: {data['storage-val']}")
        else:
            print(f"Error: {data['error']}")
    else:
        print(f"Error: {response.status_code} - {response.text}")

def keyval_update(storage_key, storage_val):
    url = f"{API_BASE_URL}/keyval/{storage_key}"
    payload = {"storage-key": storage_key, "storage-val": storage_val}
    response = requests.put(url, json=payload)
    if response.status_code == 200:
        data = response.json()
        print(f"Command: {data['command']}")
        print(f"Result: {data['result']}")
        if not data['result']:
            print(f"Error: {data['error']}")
    else:
        print(f"Error: {response.status_code} - {response.text}")

def keyval_delete(storage_key):
    url = f"{API_BASE_URL}/keyval/{storage_key}"
    response = requests.delete(url)
    if response.status_code == 200:
        data = response.json()
        print(f"Command: {data['command']}")
        print(f"Result: {data['result']}")
        if not data['result']:
            print(f"Error: {data['error']}")
    else:
        print(f"Error: {response.status_code} - {response.text}")

parser = argparse.ArgumentParser(description="CLI for interacting with your REST API")
subparsers = parser.add_subparsers(dest="command")

md5_parser = subparsers.add_parser("md5", help="Calculate MD5 hash")
md5_parser.add_argument("text", help="Text to calculate MD5 hash for")

factorial_parser = subparsers.add_parser("factorial", help="Calculate factorial")
factorial_parser.add_argument("num", type=int, help="Non-negative integer for factorial calculation")

fibonacci_parser = subparsers.add_parser("fibonacci", help="Generate Fibonacci sequence")
fibonacci_parser.add_argument("num", type=int, help="Non-negative integer for Fibonacci sequence")

is_prime_parser = subparsers.add_parser("is-prime", help="Check if a number is prime")
is_prime_parser.add_argument("num", type=int, help="Number to check for primality")

slack_alert_parser = subparsers.add_parser("slack-alert", help="Send a message to Slack")
slack_alert_parser.add_argument("message", help="Message to send to Slack")

keyval_create_parser = subparsers.add_parser("keyval-create", help="Create a key-value pair")
keyval_create_parser.add_argument("storage_key", help="Key for the key-value pair")
keyval_create_parser.add_argument("storage_val", help="Value for the key-value pair")

keyval_read_parser = subparsers.add_parser("keyval-read", help="Read a key-value pair")
keyval_read_parser.add_argument("storage_key", help="Key to read")

keyval_update_parser = subparsers.add_parser("keyval-update", help="Update a key-value pair")
keyval_update_parser.add_argument("storage_key", help="Key for the key-value pair")
keyval_update_parser.add_argument("storage_val", help="Value for the key-value pair")

keyval_delete_parser = subparsers.add_parser("keyval-delete", help="Delete a key-value pair")
keyval_delete_parser.add_argument("storage_key", help="Key to delete")

args = parser.parse_args()

if args.command == "md5":
    md5(args.text)
elif args.command == "factorial":
    factorial(args.num)
elif args.command == "fibonacci":
    fibonacci(args.num)
elif args.command == "is-prime":
    is_prime(args.num)
elif args.command == "slack-alert":
    slack_alert(args.message)
elif args.command == "keyval-create":
    keyval_create(args.storage_key, args.storage_val)
elif args.command == "keyval-read":
    keyval_read(args.storage_key)
elif args.command == "keyval-update":
    keyval_update(args.storage_key, args.storage_val)
elif args.command == "keyval-delete":
    keyval_delete(args.storage_key)
