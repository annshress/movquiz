import threading

from project import create_app
from scrape_questions import populate_questions


CONFIG = 'flask.cfg'
app = create_app(CONFIG)

if __name__ == '__main__':
    thread = threading.Thread(target=populate_questions, args=(CONFIG, ),
                              daemon=True)
    thread.start()
    # populate_questions(CONFIG)
    app.run(use_reloader=False)
