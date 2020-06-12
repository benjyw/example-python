from django.http import HttpResponse, Http404

from helloworld.django.greet.models import PersonToGreet
from helloworld.greet.greeting import Greeter


def index(request, slug):
    try:
        # TODO: Load Greeter from config once we figure out a good solution for running manage.py from Pants,
        #  so that codegen works properly in manage.py's context.
        person_to_greet = PersonToGreet.objects.get(slug=slug)
        greeter = Greeter(languages=["en", "fr"], greetings=["hello", "good morning"])
        return HttpResponse(greeter.greet(person_to_greet.full_name))
    except PersonToGreet.DoesNotExist:
        raise Http404(f"No such person: {slug}")
