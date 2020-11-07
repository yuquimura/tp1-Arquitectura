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

@app.route('/intense')
def intense():
    init = time.time()
    now = init
    while (now - init) < TIMEOUT:
        now = time.time()
    
    return 'Intense'

if __name__ == "__main__":
    app.run()