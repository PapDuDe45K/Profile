from waitress import serve
from myprofile.wsgi import application

if __name__ == "__main__":
    print("Starting Waitress server...")
    serve(application, host='0.0.0.0', port=8080)
