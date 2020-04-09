Requires:
-
- Python3.6+

### Setting up
1. Clone this repo
2. Change the current directory into the repo
3. Setup a virtualenv of your choice, or don't if you like to live dangerously
4. Run `pip install -r requirements.txt`
5. Run `flask db upgrade` which will setup up a database in *instance path* and run available migrations
6. Setup questions for quiz by running `python scrape_questions.py`
7. Run flask app
    1. `python app.py`
    2. In your browser, navigate to **localhost:5000**

### In the browser
1. Register with a username
2. A code is generate in *codes.json* in project directory
3. Copy the code for given username
4. In the browser, click on `Activate`
5. Paste the copied code, and choose a new password
6. Login with your username and the new password

Requirement:
1. A document should present your approach and the reasoning behind the approach. It
should also explain any current shortcomings of the current approach and how can it be
improved in the future
2. Unit Tests should be included.
3. Code documentation should be followed according to python guidelines.
4. Setup Documentation for running the application should be included in README
5. Should use one of “requirements.txt” or “poetry” for dependency management.