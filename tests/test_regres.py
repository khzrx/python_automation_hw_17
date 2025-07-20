import requests
import jsonschema

from tests import schemas

BASE_URL = 'https://reqres.in'
SIGN_HEADER = {'x-api-key': 'reqres-free-v1'}


# 1. Тесты на каждый из методов GET/POST/PUT/DELETE ручек reqres.in
# 3. На разные статус-коды 200/201/204/404/400


def test_users_get():
    endpoint = '/api/users/2'

    response = requests.get(BASE_URL + endpoint)

    assert response.status_code == 200


def test_users_post():
    endpoint = '/api/users'
    payload = {
        'name': 'morpheus',
        'job': 'leader'
    }

    response = requests.post(BASE_URL + endpoint, data=payload, headers=SIGN_HEADER)

    assert response.status_code == 201


def test_users_put():
    endpoint = '/api/users/2'
    payload = {
        'name': 'morpheus',
        'job': 'zion resident'
    }

    response = requests.put(BASE_URL + endpoint, data=payload, headers=SIGN_HEADER)

    assert response.status_code == 200


def test_users_delete():
    endpoint = '/api/users/2'

    response = requests.delete(BASE_URL + endpoint, headers=SIGN_HEADER)

    assert response.status_code == 204


# 2. Позитивные/Негативные тесты на одну из ручек.
# 3. На разные статус-коды 200/201/204/404/400


def test_single_user_has_current_data():
    endpoint = '/api/users/2'
    user_data = {
        'id': 2,
        'email': 'janet.weaver@reqres.in',
        'first_name': 'Janet',
        'last_name': 'Weaver',
        'avatar': 'https://reqres.in/img/faces/2-image.jpg'
    }

    response = requests.get(BASE_URL + endpoint)

    assert response.status_code == 200
    assert response.json()['data'] == user_data


def test_single_user_has_current_support():
    endpoint = '/api/users/2'
    support_data = {
        'url': 'https://contentcaddy.io?utm_source=reqres&utm_medium=json&utm_campaign=referral',
        'text': 'Tired of writing endless social media content? Let Content Caddy generate it for you.'
    }

    response = requests.get(BASE_URL + endpoint)

    assert response.status_code == 200
    assert response.json()['support'] == support_data


def test_single_user_invalid_id():
    endpoint = '/api/users/999'

    response = requests.get(BASE_URL + endpoint, headers=SIGN_HEADER)

    assert response.status_code == 404
    assert response.json() == {}


def test_single_user_invalid_id_unauthorized():
    endpoint = '/api/users/999'

    response = requests.get(BASE_URL + endpoint)

    assert response.status_code == 401
    assert response.json() == {
        'error': 'Missing API key.',
        'how_to_get_one': 'https://reqres.in/signup'
    }


# 4. Тесты на проверку схем


def test_single_user_validate_schema():
    endpoint = '/api/users/2'

    response = requests.get(BASE_URL + endpoint)

    jsonschema.validate(response.json(), schemas.single_user)


def test_single_user_unauthorized_validate_schema():
    endpoint = '/api/users/999'

    response = requests.get(BASE_URL + endpoint)

    jsonschema.validate(response.json(), schemas.unauthorized_error)


def test_user_post_validate_schema():
    endpoint = '/api/users'
    payload = {
        'name': 'morpheus',
        'job': 'leader'
    }

    response = requests.post(BASE_URL + endpoint, data=payload, headers=SIGN_HEADER)

    jsonschema.validate(response.json(), schemas.users_post)


def test_user_delete_validate_schema():
    endpoint = '/api/users/2'
    payload = {
        'name': 'morpheus',
        'job': 'zion resident'
    }

    response = requests.put(BASE_URL + endpoint, data=payload, headers=SIGN_HEADER)

    jsonschema.validate(response.json(), schemas.users_put)