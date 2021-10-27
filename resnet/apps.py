from django.apps import AppConfig
import html
import pathlib
import os

from .classifier import ResnetClassifier

class WebappConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'resnet'
    predictor = ResnetClassifier()