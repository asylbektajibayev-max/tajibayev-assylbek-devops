import importlib.util
import json
import os
import threading
import unittest
from pathlib import Path
from unittest.mock import patch
from urllib.error import HTTPError
from urllib.request import urlopen
from http.server import ThreadingHTTPServer

spec = importlib.util.spec_from_file_location('app_main', Path(__file__).parents[1] / 'app/main.py')
app = importlib.util.module_from_spec(spec)
spec.loader.exec_module(app)


class ApplicationTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.server = ThreadingHTTPServer(('127.0.0.1', 0), app.Handler)
        cls.thread = threading.Thread(target=cls.server.serve_forever, daemon=True)
        cls.thread.start()
        cls.url = f'http://127.0.0.1:{cls.server.server_port}'

    @classmethod
    def tearDownClass(cls):
        cls.server.shutdown()
        cls.server.server_close()
        cls.thread.join()

    def test_default_student(self):
        with patch.dict(os.environ, {}, clear=True):
            self.assertEqual(app.student(), dict(name='Assylbek', surname='Tajibayev', group='IT2-2310', id='38288'))

    def test_environment_overrides_all_fields(self):
        with patch.dict(os.environ, dict(STUDENT_NAME='Test', STUDENT_SURNAME='User', STUDENT_GROUP='G1', STUDENT_ID='42')):
            with urlopen(self.url + '/api/student') as r:
                self.assertEqual(json.load(r), dict(name='Test', surname='User', group='G1', id='42'))

    def test_health(self):
        with urlopen(self.url + '/health') as r:
            self.assertEqual(json.load(r), {'status': 'ok'})

    def test_html_escapes_input(self):
        with patch.dict(os.environ, {'STUDENT_NAME': '<script>alert(1)</script>'}):
            with urlopen(self.url) as r:
                body = r.read().decode()
            self.assertIn('&lt;script&gt;', body)
            self.assertNotIn('<script>', body)

    def test_unknown_route(self):
        with self.assertRaises(HTTPError) as error:
            urlopen(self.url + '/missing')
        self.assertEqual(error.exception.code, 404)


if __name__ == '__main__':
    unittest.main()
