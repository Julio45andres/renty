from django.apps import apps
from django.test import TestCase
from ..apps import DetailConfig


class DetailConfigTest(TestCase):
    def test_apps(self):
        self.assertEqual(DetailConfig.name, 'detail')
        self.assertEqual(apps.get_app_config('detail').name, 'detail')
