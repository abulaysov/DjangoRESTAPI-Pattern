from rest_framework.test import APIClient

import pytest

from users.tests import factories as user_factories


@pytest.fixture
def logged_user(db):
    user = user_factories.ActiveUserFactory()
    return user


@pytest.fixture
def logged_client(logged_user):
    client = APIClient()
    client.force_authenticate(logged_user)
    return client
