from flask import Flask

TIMEOUT = 5

app = Flask( __name__)

@app.route('/')
def raiz():
    return "Ping"

if __name__ == "__main__":
    app.run()