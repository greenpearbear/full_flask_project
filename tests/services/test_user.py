from unittest.mock import MagicMock
import pytest
from dao.model.user_model import User
from dao.user_dao import UserDAO
from service.user_service import UserService


@pytest.fixture()
def user_dao():
    user_dao = UserDAO(None)

    user_1 = User(id=1, email='Test_User_1@mail.ru', password='bdsvnmnusdvbyndsvmj',
                  name='Roma', surname='Sherlock', favorite_genre='Комедия')
    user_2 = User(id=2, email='Test_User_2@mail.ru', password='dsvnmrowbhywuecjvdu',
                  name='Ivan', surname='Boss', favorite_genre='Аниме')
    user_3 = User(id=3, email='Test_User_3@mail.ru', password='oqkcsvknqufnqunfuvd',
                  name='Oleg', surname='Home', favorite_genre='Детектив')

    user_dao.get_one = MagicMock(return_value=user_1)
    user_dao.get_all = MagicMock(return_value=[user_1, user_2, user_3])
    user_dao.get_by_username = MagicMock(return_value=user_2)
    user_dao.post = MagicMock(return_value=User(id=4, email='Test_User_4@mail.ru', password='qiejfudsvjidjsvidjv',
                                                name='Viktor', surname='Lego', favorite_genre='Мюзикл'))
    user_dao.put = MagicMock(return_value=User(id=3, email='Test_User_3_update@mail.ru', password='oqkcsvknqufnqunfuvd',
                                               name='Oleg', surname='Home', favorite_genre='Детектив'))
    user_dao.delete = MagicMock()

    return user_dao


class TestUserService:
    @pytest.fixture(autouse=True)
    def user_service(self, user_dao):
        self.user_service = UserService(dao=user_dao)

    def test_get_one(self):
        user = self.user_service.get_one(1)

        assert user is not None
        assert user.id is not None

    def test_get_all(self):
        users = self.user_service.get_all()

        assert len(users) == 3

    def test_post(self):
        user_d = {
            "username": "Test_User_4",
            'password': 'qiejfudsvjidjsvidjv',
            'role': 'user'
        }
        user = self.user_service.post(user_d)

        assert user.id is not None

    def test_put(self):
        user_d = {
            "username": "Test_User_3_update",
            'password': 'oqkcsvknqufnqunfuvd',
            'role': 'user'
        }
        user = self.user_service.put(3, user_d)

        assert user.id is not None
