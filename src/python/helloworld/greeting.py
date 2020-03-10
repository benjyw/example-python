
class Greeting:
  def __init__(self, greeting: str):
    self._greeting = greeting

  def greet(self, name: str) -> str:
    return f'{self._greeting}, {name}!'
