from http import HTTPStatus

from ceoop.schemas import UserPublic


def test_root_deve_retornar_ok_e_ola_mundo(client):

    response = client.get('/')

    assert response.status_code == HTTPStatus.OK
    assert response.json() == {'message': 'Bem vindo a API do CEOOP!'}


def test_html_deve_retornar_ok_e_html(client):

    response = client.get('/html')

    assert response.status_code == HTTPStatus.OK
    assert response.text == '<h1> Bem vindo a API do CEOOP! </h1>'


def test_create_user(client):
    response = client.post(
        '/users/',
        json={
            'name': 'Brendon',
            'username': 'brendonwallacee',
            'password': 'secret',
        },
    )
    assert response.status_code == HTTPStatus.CREATED
    assert response.json() == {
        'name': 'Brendon',
        'username': 'brendonwallacee',
        'id': 1,
    }


def test_read_users(client):
    response = client.get('/users/')
    assert response.status_code == HTTPStatus.OK
    assert response.json() == {'users': []}


def test_read_users_with_users(client, user):
    user_schema = UserPublic.model_validate(user).model_dump()
    response = client.get('/users/')
    assert response.json() == {'users': [user_schema]}


def test_update_user(client, user):
    response = client.put(
        '/users/1',
        json={
            'name': 'Ana',
            'username': 'annavelloso',
            'password': 'secreta',
        },
    )
    assert response.status_code == HTTPStatus.OK
    assert response.json() == {
        'name': 'Ana',
        'username': 'annavelloso',
        'id': 1,
    }


def test_update_integrity_error(client, user):
    client.post(
        '/users',
        json={
            'name': 'fausto',
            'username': 'faustoduno',
            'password': 'secret',
        },
    )

    response_update = client.put(
        f'/users/{user.id}',
        json={
            'name': 'fausto',
            'username': 'faustoduno',
            'password': 'mynewpassword',
        },
    )
    assert response_update.status_code == HTTPStatus.CONFLICT
    assert response_update.json() == {'detail': 'Usuário já existe'}


def test_get_user(client, user):
    response = client.get(f'/users/{user.id}')

    assert response.status_code == HTTPStatus.OK
    assert response.json() == {
        'name': user.name,
        'username': user.username,
        'id': user.id,
    }


def test_delete_user(client, user):
    response = client.delete('/users/1')

    assert response.status_code == HTTPStatus.OK
    assert response.json() == {'message': 'Usuário deletado com sucesso'}


def test_update_user_should_return_not_found(client):
    response = client.put(
        '/users/666',
        json={
            'name': 'Ana',
            'username': 'annavelloso',
            'password': 'secreta',
        },
    )
    assert response.status_code == HTTPStatus.NOT_FOUND
    assert response.json() == {'detail': 'Usuário não encontrado'}


def test_delete_user_should_return_not_found(client):
    response = client.delete('/users/666')

    assert response.status_code == HTTPStatus.NOT_FOUND
    assert response.json() == {'detail': 'Usuário não encontrado'}


def test_get_user_should_return_not_found(client):
    response = client.get('/users/666')

    assert response.status_code == HTTPStatus.NOT_FOUND
    assert response.json() == {'detail': 'Usuário não encontrado'}


def test_create_user_should_return_409_username_exists(client, user):
    response = client.post(
        '/users/',
        json={
            'name': 'Brendon',
            'username': user.username,
            'password': 'secret',
        },
    )
    assert response.status_code == HTTPStatus.CONFLICT
    assert response.json() == {'detail': 'Usuário já existe'}
