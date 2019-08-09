from flask import Flask, render_template
app = Flask(__name__)
@app.route('/')
def hello_world():
    print("Welcome!")
    return "Hellooo, please add /play to the url"

@app.route('/play')
def play():
    print("Play with 3 boxes")
    return render_template("playground_index.html",times=3)

@app.route('/play/<times>')
def play_repeat(times):
    return render_template("playground_index.html",times=int(times))

@app.route('/play/<times>/<color>')
def play_repeat_color(times, color):
    return render_template("playground_index.html",times=int(times),color=color)
    

if __name__=="__main__":
    app.run(debug=True)


