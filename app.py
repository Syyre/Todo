from flask import Flask, render_template, redirect, request, url_for

app = Flask(__name__, template_folder="templates")

"""
    todo List in form {task:"blah", done: bool}
"""
todos = [{"todo":"Sample Todo", "done":False}]

@app.route("/")
def index():
    return render_template("index.html", todos=todos)

#TODO: Add more functionality. Ability to create more tasks, edit/delete tasks.
#TODO: edit index.html files with css.


if __name__ == '__main__':
    app.run(debug=True)