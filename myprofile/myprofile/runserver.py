from waitress import serve
import myprofile.wsgi

if __name__ == '__main__':
    serve(myprofile.wsgi.application, host='127.0.0.1', port=8000)
