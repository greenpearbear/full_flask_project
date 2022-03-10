from unittest.mock import MagicMock
import pytest
from dao.model.movie_model import Movie
from dao.movie_dao import MovieDAO
from service.movie_service import MovieService


@pytest.fixture()
def movie_dao():
    movie_dao = MovieDAO(None)

    movie_1 = Movie(id=1, title='Test_Movie_1', description='description_1', trailer='trailer_1', year=2011,
                    rating=8.1, genre_id=1, director_id=1)
    movie_2 = Movie(id=2, title='Test_Movie_2', description='description_2', trailer='trailer_2', year=2012,
                    rating=8.2, genre_id=2, director_id=2)
    movie_3 = Movie(id=3, title='Test_Movie_3', description='description_3', trailer='trailer_3', year=2013,
                    rating=8.3, genre_id=3, director_id=3)

    movie_dao.get_one = MagicMock(return_value=movie_1)
    movie_dao.get_all = MagicMock(return_value=[movie_1, movie_2, movie_3])

    return movie_dao


class TestMovieService:
    @pytest.fixture(autouse=True)
    def movie_service(self, movie_dao):
        self.movie_service = MovieService(dao=movie_dao)

    def test_get_one(self):
        movie = self.movie_service.get_one(1)

        assert movie is not None
        assert movie.id is not None

    def test_get_all(self):
        movies = self.movie_service.get_all()

        assert len(movies) == 3
