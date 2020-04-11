Requires:
-
- Python3.6+

### Setting up
1. Clone this repo
2. Change the current directory into the repo
3. Setup a virtualenv of your choice, or don't if you like to live dangerously
4. Run `pip install -r requirements.txt`
5. Run `flask db upgrade` which will setup up a database in *instance path* and run available migrations
6. Run flask app
    1. `python app.py` *This might take about 10 seconds on the first run*
    2. In your browser, navigate to **localhost:5000**

### In the browser
1. Register with a username
2. A code is generate in *codes.json* in project directory
3. Copy the code for given username
4. In the browser, click on `Activate`
5. Paste the copied code, and choose a new password
6. Login with your username and the new password

