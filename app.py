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
        return render_template('hello.html', username=username)
    
    form = LoginForm()

    return render_template('login.html', form=form)

@app.route('/logout')
def logout():
    if 'username' in session:
        session.pop('username')
    return redirect('login')