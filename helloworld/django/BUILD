# Copyright 2020 Pants project contributors.
# Licensed under the Apache License, Version 2.0 (see LICENSE).

python_library(
    # `name` defaults to the name of this directory, i.e., `django`.
    # `sources` defaults to ['*.py', '!*_test.py', '!test_*.py', '!conftest.py'].
    dependencies = [
        "//:django",
        "helloworld/django/greet"
    ]
)


python_binary(
    name = "manage",
    entry_point = "helloworld.django.manage",
    dependencies = [
        ":django"
    ],
    zip_safe=False
)
