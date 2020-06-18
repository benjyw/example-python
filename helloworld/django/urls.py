# Copyright 2020 Pants project contributors.
# Licensed under the Apache License, Version 2.0 (see LICENSE).

from django.urls import path, include


urlpatterns = [
    path('greet/', include('helloworld.django.greet.urls')),
]
