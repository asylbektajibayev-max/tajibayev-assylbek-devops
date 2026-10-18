"""Personal DevOps application using only the Python standard library."""
import json
import os
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from html import escape


def student():
    return {key: os.getenv('STUDENT_' + key.upper(), default) for key, default in {
        'name': 'Assylbek', 'surname': 'Tajibayev', 'group': 'IT2-2310', 'id': '38288'
    }.items()}


class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/health':
            payload, kind = b'{"status":"ok"}', 'application/json'
        elif self.path == '/api/student':
            payload, kind = json.dumps(student()).encode(), 'application/json'
        elif self.path == '/':
            rows = ''.join('<p><b>' + k.title() + ':</b> ' + escape(v) + '</p>'
                           for k, v in student().items())
            payload = ('<!doctype html><html lang="en"><meta charset="utf-8">'
                       '<title>DevOps Student Application</title><body>'
                       '<h1>DevOps Student Application</h1>' + rows +
                       '<p>Application is running successfully!</p></body></html>').encode()
            kind = 'text/html; charset=utf-8'
        else:
            self.send_error(404)
            return
        self.send_response(200)
        self.send_header('Content-Type', kind)
        self.send_header('Content-Length', str(len(payload)))
        self.end_headers()
        self.wfile.write(payload)


if __name__ == '__main__':
    print('DevOps Student Application', flush=True)
    for key, value in student().items():
        print(f'{key.title()}: {value}', flush=True)
    print('Application is running successfully!', flush=True)
    ThreadingHTTPServer(('0.0.0.0', int(os.getenv('PORT', '8000'))), Handler).serve_forever()
