from dataclasses import asdict

from sqlalchemy import select

from ceoop.models import User


def test_create_user(session, mock_db_time):
    with mock_db_time(model=User) as time:
        new_user = User(
            name='Brendon', username='brendonwallacee', password='secret'
        )
        session.add(new_user)
        session.commit()

    user = session.scalar(
        select(User).where(User.username == 'brendonwallacee')
    )
    assert asdict(user) == {
        'id': 1,
        'name': 'Brendon',
        'username': 'brendonwallacee',
        'password': 'secret',
        'created_at': time,
    }
