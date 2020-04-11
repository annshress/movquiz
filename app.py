from project import create_app
from scrape_questions import populate_questions

CONFIG = 'flask.cfg'
app = create_app(CONFIG)

if __name__ == '__main__':
    try:
        populate_questions(CONFIG)
    except NotImplementedError as e:
        pass
    app.run()
