# Copyright 2020 Pants project contributors.
# Licensed under the Apache License, Version 2.0 (see LICENSE).

import pytest

from helloworld.django.greet.models import PersonToGreet


@pytest.mark.django_db
def test_database_is_seeded():
    sherlock = PersonToGreet.objects.get(slug="sherlock")
    assert "Sherlock Holmes" == sherlock.full_name
