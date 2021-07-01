import pytest

from application import Application


@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture


def test(app):
    app.open_page()
    app.login(username="ismetocp@gmail.com", password="ismetocp")
    app.search(element='webkassa')
