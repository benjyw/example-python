python_library(
    # name defaults to the name of this directory, i.e., `helloworld`.
    # sources defaults to ['*.py', '!*_test.py', '!test_*.py', '!conftest.py'].
    dependencies = [
        '3rdparty/python:translate'
    ]
)

python_binary(
    name = 'main',
    entry_point = 'helloworld.main',
    dependencies = [
        ':helloworld'
    ]
)
