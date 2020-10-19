from flask import Flask
import time
TIMEOUT = 5

app = Flask( __name__)

@app.route('/')
def raiz():
    return "Ping"

@app.route('/timeout')
def esperar():
    time.sleep(TIMEOUT)
    return "Timeout"

if __name__ == "__main__":
    app.run()