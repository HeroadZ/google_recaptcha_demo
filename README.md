# recaptcha_demo
A google recaptcha demo in Python(3.x supported) with http.server for backend verification.  
### Currently supported version
- [x] v2 checkbox
- [x] v2 invisible
- [x] v3
    
  
### Prerequisites
You should have registered google recaptcha. 
Select the version you want, and please add `127.0.0.1` in your domain for localhost test.
You can get public key and private key from [google recaptcha admin](https://www.google.com/recaptcha/admin).

### 1. Install Dependencies
```sh
pip install -r requirements.txt
```

### 2. Replace public and private key
1. Replace public key in the html page (search with `const public_key=`)
2. Replace private keys in the `server.py` with the version you want.

### 3. Run the server
```sh
python server.py
```

### 4. Verify

1. open the browser and visit the url: http://127.0.0.1:8000/
2. choose the version you want to play with
3. verify it and check output of python and log in the browser console

### 5. Shutdown server
Don't use Ctrl+C to shutdown the server cause that will stuck it.
Instead, click the `shutdown server` button.
