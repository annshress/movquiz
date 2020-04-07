### task

...However you want only your
friends to be able to sign up so you have created a system for user verification.
1. Build a flask application which accepts a username during registration. Upon registration,
a code is written to a file in the backend. You must provide the user who is trying to
register the code so that he/she can activate the username. Upon registration
completed, the user can use the username and a password to login

Stack:
- Database = SQLite
- API = Python/Flask
- Front End = Any

2. Upon logging in successfully, the following are shown
a. The “Take the movie quiz” button. This let’s you take the movie quiz
b. A paginated table shown high scores of your friends
Upon taking the quiz the user’s name and score should appear on the table in
descending order of the score. All other user’s scores should also be seen. The table
should be paginated
The quiz should always have 10 questions. But the questions should appear randomly
and be generated dynamically.
3. A background process in your application should be executable to scrape movie data
from IMDB and populate the database. Flask should read the database and randomly
provide the view with a sample of questions for the quiz
Requirement:
1. A document should present your approach and the reasoning behind the approach. It
should also explain any current shortcomings of the current approach and how can it be
improved in the future
2. Unit Tests should be included.
3. Code documentation should be followed according to python guidelines.
4. Setup Documentation for running the application should be included in README
5. Should use one of “requirements.txt” or “poetry” for dependency management.