from app import app, db
from flask import render_template, redirect, url_for
from models import Task

import forms

@app.route('/')
@app.route('/index')
def index():
    tasks = Task.query.all()
    return render_template('index.html', tasks=tasks)

@app.route('/about', methods=['GET', 'POST'])
def about():
    form = forms.AddTaskForm()
    if form.validate_on_submit():
        t = Task(title=form.title.data, date=datetime.utcnow())
        db.session.add(t) # save to database
        db.session.commit() # This is the line that actually adds the task to the database
    print('Submitted title', form.title.data)
    return redirect(url_for('index'))
    #return render_template('about.html', form=form, title=form.title.data)
    
    #return render_template('about.html', form=form)