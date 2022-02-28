import http.server
import requests
import json

PORT = 8000
KEEP_RUNNING = True

class MyHttpRequestHandler(http.server.BaseHTTPRequestHandler):
    
    def _set_response(self, content_type='text/html'):
        self.send_response(200)
        self.send_header("Content-type", content_type)
        self.end_headers()
    
    def do_GET(self):
        self._set_response()
        
        if self.path == '/v2_checkbox.html':
            h = open("templates/v2_checkbox.html", "rb")
            self.wfile.write(h.read())
        elif self.path == '/shutdown':
            global KEEP_RUNNING
            KEEP_RUNNING = False
            self.wfile.write("server is stopped".encode('utf-8'))
            print('server is stopped')
        else:
            h = open("templates/index.html", "rb")
            self.wfile.write(h.read())

    def do_POST(self):
        content_length = int(self.headers['Content-Length']) # <--- Gets the size of data
        post_data = self.rfile.read(content_length) # <--- Gets the data itself
        print('post data: '+ post_data.decode('utf-8'))
        
        resp_json = json.loads(post_data.decode('utf-8'))
        self._set_response(content_type='application/json')
        
        # send private key and token to google for verification
        r = requests.post('https://www.google.com/recaptcha/api/siteverify', data={
            "secret": "replace me with private key",
            "response": resp_json.get('response_token')
        })
        print(f'verfication result from google: {str(r.json())}')
        
        # return verification result from google to client
        self.wfile.write(r.content)

my_server = http.server.HTTPServer(("localhost", PORT), MyHttpRequestHandler)

def keep_running():
    return KEEP_RUNNING
    
while keep_running():
    my_server.handle_request()
