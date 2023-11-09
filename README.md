**Steps for running the repo**
1. Clone repo to local machine
2. Navigate to repo's directory
3. Open terminal and run this command
    - docker compose up
4. In a separate terminal run the testapp file
    - python testapp.py
5. To check for logs (either redis or flask containers)
    - docker compose logs redis
    - docker compose logs flask-app
