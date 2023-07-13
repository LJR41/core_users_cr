# burgers.py
from flask_app import app
from flask import render_template,redirect,request,session,flash
from flask_app.models.users_model import User




@app.route('/')          # The "@" decorator associates this route with the function immediately following
def display_all():
    all_users = User.display_all()
    return render_template('read_all.html',all_users=all_users)

@app.route('/new')
def new_user():
    return render_template('create.html')

@app.route('/create', methods=['POST'])
def create_user():
    User.create(request.form)
    return redirect('/')

@app.route('/show/<int:id>')
def show_user(id):
    data ={
        'id': id
    }
    one_user = User.display_one(data)
    print(one_user)
    return render_template('show.html', one_user=one_user)

@app.route('/edit/<int:id>')
def edit_user(id):
    data ={
        'id': id
    }
    one_user = User.display_one(data)
    return render_template('edit.html', one_user=one_user)

@app.route('/update/<int:id>', methods=['POST'])
def update_user(id):
    data ={
        'first_name' : request.form['first_name'],
        'last_name' : request.form['last_name'],
        'email' : request.form['email'],
        'id': id
    }
    User.update_one(data)
    return redirect(f'/show/{id}')

@app.route('/delete/<int:id>')
def delete_user(id):
    data ={
        'id': id
    }
    one_user = User.delete_user(data)
    return redirect('/')