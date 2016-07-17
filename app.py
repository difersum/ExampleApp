from flask import Flask, render_template, request, redirect
import numpy as np
app = Flask(__name__)

@app.route('/')
def main():
  return redirect('/index')

@app.route('/index')
def index():
  return render_template('index.html')

@app.route('/hi')
def hello_world_lulu():
    # this is a comment, just like in Python
    # note that the function name and the route argument
    # do not need to be the same.
    r = [1,2,3,4,5,6,7,8]
    
    return str(np.random.choice(r))


if __name__ == '__main__':
  app.run(port=33507)