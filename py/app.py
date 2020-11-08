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
    n = 100
    while (now - init) < TIMEOUT:
        now = time.time()
        n = n*n
    
    return 'Intense'

if __name__ == "__main__":
    app.run()