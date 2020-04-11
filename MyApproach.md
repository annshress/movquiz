The question was straight forward. Flask is very lean compared to Django. 

Other than finding the right ways, right structures and right tools, the point #3 in the description was convoluting.

## Battle between Memory and Space

**How to show 10 questions to user?**

The words like "dynamic generation" and "executable background scripts" were hard to go around with.

I jotted down three approaches from the top of my head:
1. Scraping movies, storing a random subsection and building & storing those questions only
2. Scraping *complete movies details into the storage, and building 10 questions on the go by random selection of the 
movies

**What I did**
3. On the first launch, pull the *complete collection of movies, build questions and store questions

**Why?**
- Easier to implement
- Scraping logic is completely detached from application logic
- Fetching questions for the quiz is solely affected by database read operations

**Downside**
- Storage of all the possible questions

_Note_:

*complete - in this context, the top 250 IMDB movies
