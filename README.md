# recaptcha_demo
A google recaptcha demo in Python(3.x supported) with http.server for backend verification.
    
  
### Prerequisites
You should have registered google recaptcha with '127.0.0.1' domain. 
You can get public key and private key from [google recaptcha admin](https://www.google.com/recaptcha/admin).

### 1. Install Dependencies
```sh
pip install -r requirements.txt
```

### 2. Replace public and private key
1. Replace public key in the html page (L13 in v2_checkbox.html)
2. Replace private key in the python script (L24 in server.py)

### 3. and Run the server
```sh
python server.py
```

### 3. Verify

1. open the browser and visit the url: http://127.0.0.1:8000/
2. click "I'm not a robot" button
3. you will see the verification result and output in the console
