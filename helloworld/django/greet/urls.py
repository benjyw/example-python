# Copyright 2020 Pants project contributors.
# Licensed under the Apache License, Version 2.0 (see LICENSE).

from django.urls import path

from helloworld.django.greet import views


urlpatterns = [
    path('<str:slug>/', views.index, name='index'),
]
