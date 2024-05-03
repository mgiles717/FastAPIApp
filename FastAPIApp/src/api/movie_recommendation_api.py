from enum import Enum

from fastapi import FastAPI
from pydantic import BaseModel

import uvicorn

app = FastAPI()

""" Creating an Enum class to define the genre of the movie. """
class Genre(str, Enum):
    ACTION = "action"
    COMEDY = "comedy"
    DRAMA = "drama"
    HORROR = "horror"
    ROMANCE = "romance"
    THRILLER = "thriller"
    
""" Creating a class to define the properties of the movie. """
class Movie(BaseModel):
    title: str
    genre: Genre
    
movies = {
    "1": Movie(title="The Shawshank Redemption", genre=Genre.DRAMA),
}

""" Defining the index route to return the list of movies. """
@app.get("/")
def index() -> dict[str, dict[int, Movie]]:
    return {"movies": movies}

if __name__ == "__main__":
    uvicorn.run("movie_recommendation_api:app", host="127.0.0.1", port=5000, log_level="info")