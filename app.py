from flask import Flask, request, render_template, session, redirect
from forms import LoginForm, RegisterForm
from database import db
from models import User

from flask_migrate import Migrate

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite3'

app.config['SECRET_KEY'] = 'adakwuydgajsdbawbdadkahsd'
# app.config['ALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)
migrate = Migrate(app, db)

@app.route('/register', methods=['GET', 'POST'])
def register():
    if 'username' in session:   # Check if user is logged in
        return redirect('todo')
    form = RegisterForm() # Create form object
    if form.validate_on_submit(): # Check if form is valid
        username = form.username.data # Get username from form in HTML
        password = form.password.data # Get password from form in HTML

        user = User(username=username, password=password) # Create new user
        db.session.add(user) # Add new user to database
        db.session.commit() # Commit changes
        return redirect('login')
    return render_template('register.html', form=form)


@app.route('/login', methods=['GET', 'POST'])
def login():
    if 'username' in session:   # Check if user is logged in
        return redirect('todo')
    form = LoginForm() # Create form object
    if form.validate_on_submit(): # Check if form is valid
        username = form.username.data  # Get username from form in HTML
        password = form.password.data  # Get password from form in HTML
        user = User.query.filter_by(username=username, password=password).first()
        # Check if user exists in database
        if user:
            session['username'] = username  # Add username to session
            return redirect('todo')
        return redirect('login')
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
