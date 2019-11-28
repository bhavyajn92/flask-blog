from flask import Flask, render_template, request, session, redirect
from flask_sqlalchemy import SQLAlchemy
from flask_mail import Mail
import datetime
import json
import os
from werkzeug import secure_filename
import math


with open('config.json', 'r') as c:
    params = json.load(c)['params']


app = Flask(__name__)
app.secret_key='my-super-secret-key'

app.config['UPLOAD_FOLDER'] = params['upload_folder']

app.config.update(
    MAIL_SERVER='smtp.gmail.com',
    MAIL_PORT='465',
    MAIL_USE_SSL=True,
    MAIL_USER=params['gmail-user'],
    MAIL_PASSWORD=params['gmail-pass']
)
mail = Mail(app)

local_server = params['local_server']

if local_server:
    app.config['SQLALCHEMY_DATABASE_URI'] = params['local_uri']
else:
    app.config['SQLALCHEMY_DATABASE_URI'] = params['prod_uri']
db = SQLAlchemy(app)


class Contacts(db.Model):
    sno = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80),  nullable=False)
    phone_num = db.Column(db.String(12), nullable=False)
    msg = db.Column(db.String(120), nullable=False)
    date = db.Column(db.String(50), nullable=True)
    email = db.Column(db.String(120), nullable=False)


class Post(db.Model):
    sno = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    subtitle = db.Column(db.String(100), nullable=False)
    slug = db.Column(db.String(50), nullable=False)
    content = db.Column(db.String(500), nullable=False)
    posted_by = db.Column(db.String(50), nullable=False)
    date = db.Column(db.String(25), nullable=True)
    img_file = db.Column(db.String(25), nullable=True)


@app.route('/dashboard', methods=['GET','POST'])
def dashboard():
    if 'user' in session and session['user'] == params['admin_user']:
        posts = Post.query.order_by(Post.sno.desc()).all()
        return render_template('dashboard.html', params=params, posts=posts)
    if request.method == 'POST':
        if request.form.get('uname') == params['admin_user'] and request.form.get('pass') == params['admin_password']:
            posts = Post.query.order_by(Post.sno).all()
            session['user'] = request.form.get('uname')
            return render_template('dashboard.html', params=params, posts=posts)
    return render_template('login.html', params=params)


@app.route('/logout')
def logout():
    session.pop('user')
    return redirect('/')


@app.route('/delete/<int:sno>')
def delete_post(sno):
    if 'user' in session and session['user'] == params['admin_user']:
        post = Post.query.filter_by(sno=sno).first()
        db.session.delete(post)
        db.session.commit()
    return redirect('/dashboard')


@app.route('/uploader', methods=['GET', 'POST'])
def uploader():
    if 'user' in session and session['user'] == params['admin_user']:
        if request.method == 'POST':
            f = request.files["file"]
            f.save(os.path.join(app.config['UPLOAD_FOLDER'], secure_filename(f.filename)))
    return redirect('/dashboard')


@app.route('/edit/<string:sno>', methods=['GET', 'POST'])
def edit_post(sno):
    if 'user' in session and session['user'] == params['admin_user']:
        if request.method == 'POST':
            req_title = request.form.get('title')
            req_subtitle = request.form.get('subtitle')
            req_slug = request.form.get('slug')
            req_content = request.form.get('content')
            req_img_file = request.form.get('img_file')
            posted_by = session['user']
            if sno == '0':
                post = Post(title=req_title, subtitle=req_subtitle, slug=req_slug,
                            content=req_content, img_file=req_img_file, posted_by=posted_by, date=datetime.datetime.now())
                db.session.add(post)
            else:
                post = Post.query.filter_by(sno=sno).first()
                post.title = req_title
                post.subtitle = req_subtitle
                post.slug = req_slug
                post.content = req_content
                post.img_file = req_img_file
                post.posted_by = posted_by
                post.date = datetime.datetime.now()
            db.session.commit()
            return redirect('/dashboard')

        post = Post.query.filter_by(sno=sno).first()
        if sno == '0':
            post = dict()
            post['sno'] = 0
        return render_template('edit.html', params=params, post=post)
    return render_template('login.html', params=params)


@app.route('/', methods=['GET'])
# @app.route('/<int:page_id>', methods=['GET'])
def home():
    posts_data = Post.query.order_by(Post.date.desc()).all()
    num_of_posts = int(params['no_of_posts'])
    last = math.ceil(len(posts_data)/num_of_posts)
    page = request.args.get('page')
    if not str(page).isnumeric():
        page = 1
    page = int(page)
    if page == 1:
        prev = '#'
        next = '/?page=' + str(page + 1)
    elif page == last:
        prev = '/?page=' + str(page - 1)
        next = '#'
    else:
        prev = '/?page=' + str(page - 1)
        next = '/?page=' + str(page + 1)

    posts_data = posts_data[num_of_posts*page-num_of_posts: num_of_posts*page]
    return render_template('index.html', params=params, posts=posts_data, prev=prev, next=next)


@app.route('/about')
def about():
    return render_template('about.html', params=params)


@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        phone = request.form.get('phone')
        message = request.form.get('message')
        db_contact = Contacts(name=name, phone_num=phone, msg=message, date=datetime.datetime.now(), email=email)
        db.session.add(db_contact)
        db.session.commit()
        mail.send_message(f'New message from {name}',
                          sender='email',
                          recipients=[params['gmail-user']],
                          body = message + "\n" + phone
                          )
    return render_template('contact.html', params=params)


@app.route('/post/<string:post_slug>', methods=['GET'])
def post_route(post_slug):
    post = Post.query.filter_by(slug=post_slug).first()
    return render_template('post.html', params=params, post=post)


if __name__ == '__main__':
    app.run(debug=True)