
from helloworld.greeting import Greeting


def say_hello():
    greeting = Greeting('hello')
    sentence = greeting.greet('world', to_lang="es")
    print(sentence)


if __name__ == '__main__':
    say_hello()
