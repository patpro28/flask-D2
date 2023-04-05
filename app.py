from flask import Flask, request, render_template, session, redirect
from forms import LoginForm

app = Flask(__name__)

app.config['SECRET_KEY'] = 'adakwuydgajsdbawbdadkahsd'

@app.route('/login', methods=['GET', 'POST'])
def login():
    if 'username' in session:
        username = session['username']
        return render_template('hello.html', username=username)
    if request.method == 'POST':
        username = session['username'] = request.form['username']
        return redirect('todo')
    
    form = LoginForm()

    return render_template('login.html', form=form)

@app.route('/logout')
def logout():
    if 'username' in session:
        session.pop('username')
    return redirect('login')

@app.route('/todo')
def todo():
    todolist = []
    if 'username' in session:
        if 'todolist' in session:
            todolist = session['todolist']
        return render_template('todolist.html', todos=todolist)
    return redirect('login')

@app.route('/add', methods=['POST'])
def add():
    if 'username' in session:
        if 'todolist' in session:
            todolist = session['todolist']
        else:
            todolist = []
        todolist.append(request.form['todo'])
        session['todolist'] = todolist
        return redirect('todo')
    return redirect('login')

@app.route('/delete', methods=['POST'])
def delete():
    if 'username' in session:
        if 'todolist' in session:
            todolist = session['todolist']
        else:
            todolist = []
        todolist.remove(request.form['todo'])
        session['todolist'] = todolist
        return redirect('todo')
    return redirect('login')
