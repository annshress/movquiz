from bs4 import BeautifulSoup
import os
import random
import requests

from project.models.quiz import Question
from project import db, create_app


def get_details(soup):
    details = [
        {
            'title': ele.select('.lister-item-header a')[0].text,
            'release': ele.select('span.lister-item-year')[0].text[1:-1],
            'rating': ele.select('.ratings-imdb-rating strong')[0].text,
            'director': ele.select('p[class=""] a')[0].text,
            'actors': [actor.text for actor in ele.select('p[class=""] a')[1:]],
        }
        for ele in soup.select('.lister-item-content')
    ]
    return details


def movie_details():
    """
    create an object of movie dicts from the obtained soup
    """
    movies = []
    url_builder = 'https://www.imdb.com/search/title/?groups=top_250&sort=user_rating,desc&start={start}&ref_=adv_nxt'

    for start in range(1, 250, 50):
        url = url_builder.format(start=start)
        print(f"Fetching movies details from {url}", end='\n-----------------\n')
        response = requests.get(url)
        soup = BeautifulSoup(response.text, features="html.parser")
        movies.extend(get_details(soup))
    return movies

# -------------QUESTION BUILDERS ---------- #


def release_date_question(movie):
    question = Question(
        question=f'When was {movie["title"]} released?',
        answer=movie['release']
    )
    db.session.add(question)


def director_question(movie, movie2):
    director = random.choice([movie['director'], movie2['director']])
    question = Question(
        question=f'Did {director} direct the movie \"{movie["title"]} ({movie["release"]})\" ?',
        answer='yes' if movie['director'] == director else 'no',
        type='director'
    )
    db.session.add(question)


def rating_question(movie):
    question = Question(
        question=f'Guess the rating of movie \"{movie["title"]} ({movie["release"]})\" from 1 to 100.',
        answer=int(float(movie["rating"])*10),
        type="rating"
    )
    db.session.add(question)


def actor_question(movie, movie2):
    wrong = movie2['actors'][0]
    actors = movie['actors'] + [wrong]
    random.shuffle(actors)
    question = Question(
        question=f'Which of the following actors [{", ".join(actors)}] did not'
                 f' star in the movie {movie["title"]}({movie["release"]}) ?',
        answer=wrong
    )
    db.session.add(question)

# ---------END QUESTION BUILDERS------------- #


def populate_questions():
    if os.path.exists('scrape_complete.lock'):
        raise NotImplementedError('Database has been populated. Scraping further is not supported!')
    movies = movie_details()
    # shuffle the movies to create wrong choices
    shuffled = random.sample(movies, len(movies))

    print("Populating Questions into database", end='\n-----------------\n')

    for movie in movies:
        release_date_question(movie)
        rating_question(movie)
    for movie_pair in zip(movies, shuffled):
        director_question(*movie_pair)
        actor_question(*movie_pair)

    db.session.commit()
    with open('scrape_complete.lock', 'w'):
        pass
    print("Questions loaded into the database", end='\n-----------------\n')


if __name__ == '__main__':
    filename = 'flask.cfg'
    print("Creating questions based on top 250 movies in IMDB.")
    print("##################################################")
    print(f"Configuring flask app and db according to {filename}", end='\n-----------------\n')
    app = create_app(filename)
    app.app_context().push()

    try:
        populate_questions()
    except NotImplementedError as e:
        print(e)
