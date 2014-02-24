from django.contrib.auth import get_user_model

from metakv.test_helpers import ExtendedTestCase
from metakv import models

class metakvTests(ExtendedTestCase):
    def test_404(self):
        self.assertStatus(404, '/foobar/')

    def test_home(self):
        self.assertStatus(200, '/')
