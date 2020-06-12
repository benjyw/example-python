# Copyright 2020 Pants project contributors.
# Licensed under the Apache License, Version 2.0 (see LICENSE).

python_library(
    dependencies = [
        "//:django",
        "helloworld/greet",
    ],
)

python_tests(
    name = 'tests',
    # `sources` defaults to ['*_test.py', 'test_*.py', 'conftest.py'].
    dependencies = [
        ":greet",
        "helloworld/django",  # For settings.py.
        "helloworld/django/greet/migrations",
        "//:pytest_ini",
    ]
)
