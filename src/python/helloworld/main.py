from colors import green

from helloworld.greeting import Greeter


def say_hello():
    greeter = Greeter()
    sentence = greeter.greet("world")
    print(green(sentence))


if __name__ == "__main__":
    say_hello()
