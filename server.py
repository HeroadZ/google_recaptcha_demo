import http.server
import requests
import json

class MyHttpRequestHandler(http.server.BaseHTTPRequestHandler):
    
    def _set_response(self, content_type='text/html'):
        self.send_response(200)
        self.send_header("Content-type", content_type)
        self.end_headers()
    
    def do_GET(self):
        self._set_response()
        h = open("templates/v2_checkbox.html", "rb")
        self.wfile.write(h.read())

    def do_POST(self):
        content_length = int(self.headers['Content-Length']) # <--- Gets the size of data
        post_data = self.rfile.read(content_length) # <--- Gets the data itself
        print('post data: '+ post_data.decode('utf-8'))
        resp_json = json.loads(post_data.decode('utf-8'))
        self._set_response(content_type='application/json')
        r = requests.post('https://www.google.com/recaptcha/api/siteverify', data={
            "secret": "replace me with private key",
            "response": resp_json.get('response_token')
        })
        print(f'verfication result from google: {str(r.json())}')
        self.wfile.write(r.content)
    

# Create an object of the above class
handler_object = MyHttpRequestHandler

PORT = 8000
my_server = http.server.HTTPServer(("localhost", PORT), handler_object)

# Star the server
my_server.serve_forever()
