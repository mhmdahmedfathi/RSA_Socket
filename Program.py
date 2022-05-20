# -*- coding: utf-8 -*-


from flask import Flask, render_template, request
import sys
import RSA

app = Flask(__name__)


@app.route('/')
def index():
    global n, e, d, min_e, bits
    context = {
        'n': n,
        'e': e,
        'd': d,
        'min_e': min_e,
        'bits': bits
    }
    return render_template('index.html', **context)



if __name__ == "__main__":
    port = 8080
    if len(sys.argv) > 1:
        port = sys.argv[1]
        if port.isnumeric():
            port = int(port)

    app.run(debug=True, port=port)  # listen on localhost ONLY