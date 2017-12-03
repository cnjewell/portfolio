from app import app, db
from flask import request, redirect, render_template, session, flash
from werkzeug.routing import BaseConverter
import cgi, re, html

from models import User, Post
from hashutils import check_pw_hash, make_salt, make_pw_hash
import caesar


###############################################
################## USER AUTH ##################
###############################################

login_needed = ['newpost', 'logout']

@app.before_request
def require_login():
    if ('user' not in session and request.endpoint in login_needed):
        flash('Login required to access certain pages.', category="is-warning")
        return redirect("/login")

def logged_in_user():
    return User.query.filter_by(email=session['user']).first()

email_regex = re.compile(r'^[-\w]+@[-\w]+[.][-\w]+$')
def is_email(string):
    if email_regex.match(string):
        return True
    else:
        return False

valid_username_regex = re.compile(r'^[-\w]+$')
def is_valid_username(string):
    if string:
        if valid_username_regex.match(string):
            return True
        else:
            False
    else:
        return False

@app.route("/login", methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template('login.html')
    
    if request.method == 'POST':
        
        email = request.form['email']
        password = request.form['password']
        
        # VAILDATION #

        if email == '' or password == '':
            flash('Error: One or more fields left blank', category="is-warning")
            return redirect('/login')

        users = User.query.filter_by(email=email)
        if users.count() != 1:
            flash('Error: Email not in our system.', category="is-warning")
            return redirect("/login")            

        user = users.first()        
        pw_hash, salt = user.pw_hash.split(',')
        test_pw_hash, salt = make_pw_hash(password, salt).split(',')

        if test_pw_hash != pw_hash:
            flash('Error: Incorrect password', category="is-warning")
            return redirect("/login")     
        
        # SUCCESS # 

        session['user'] = user.email
        flash('Welcome Back, '+user.email, category="is-primary")
        return redirect("/")



@app.route("/register", methods=['GET', 'POST'])
def register():
    
    if request.method == 'GET':
        return render_template('register.html')

    if request.method == 'POST':

        email = request.form['email']
        username = request.form['username']
        password = request.form['password']
        verify = request.form['verify']

        # VALIDATION #

        if email == '' or username == '' or password == '' or verify == '':
            flash('Error: One or more fields left blank', category="is-warning")
            return render_template("register.html", email=email, username=username)

        if not is_email(email):
            flash('Error: Entered email is not formatted like an email address', category="is-warning")
            return render_template("register.html", email=email, username=username)

        if not is_valid_username(username):
            flash('Error: Usernames can only include: hyphens, underscores, letters and numbers', category="is-warning")
            return render_template("register.html", email=email, username=username)
        
        email_db_count = User.query.filter_by(email=email).count()
        if email_db_count > 0:
            flash('Error: Email is already taken.', category="is-warning")
            return render_template("register.html", email=email, username=username)

        username_db_count = User.query.filter_by(username=username).count()
        if username_db_count > 0:
            flash('Error: Username is already taken.', category="is-warning")
            return render_template("register.html", email=email, username=username)

        if len(email) < 3 or len(username) < 3 or len(password) < 3:
            flash('Error: Email, username or password has fewer than three characters', category="is-warning")
            return render_template("register.html", email=email, username=username)            

        if password != verify:
            flash('Error: Passwords entered do not match.', category="is-warning")
            return render_template("register.html", email=email, username=username)

        # SUCCESS #

        pw_hash = make_pw_hash(password)
        user = User(email=email, username=username, pw_hash=pw_hash)
        db.session.add(user)
        db.session.commit()
        
        session['user'] = user.email
        flash('Successfully registered, '+user.email, category="is-primary")
        return redirect("/")


@app.route("/logout", methods=[ 'POST'])
def logout():
    user = session['user']
    del session['user']
    flash('Successfully logged out of '+user, category="is-primary")
    return redirect("/")



###############################################
##################### BLOG ####################
###############################################

# TODO: BLOGZ 
    # Pagination

    # Posts
    # - add DateTime to Post model
        # - add datetime to templates displaying posts
        # - reinitalize database for updated Post model

# /blog                   display all authors
# /blog/username          display all posts by single author, pagination included
# /blog/posts             display all posts, pagination included
# /blog/posts/post_id     display a single post by Post.id

@app.route("/blog", methods=['GET'])
@app.route("/blog/<username>", methods=['GET'])
def blog(username=None):
    
    if is_valid_username(username):
        
        author = User.query.filter_by(username=username).first()

        if not author:
            flash('Error: Requested username not in database.', category="is-warning")
            return redirect("/blog")

        postlist = db.session.query(Post, User).join(User).filter(User.username == username).all()
        return render_template("blog.html", postlist=postlist)

    else:
        authors = User.query.all()
        return render_template("authors.html", authors=authors)


@app.route('/blog/posts', methods=['GET'])
@app.route('/blog/posts/<int:url_post_id>', methods=['GET'])
def blog_posts(url_post_id=None):
    
    if url_post_id:
        postlist = db.session.query(Post, User).join(User).filter(Post.id == url_post_id).all()
        if not postlist:
            flash('Error: Requested post not in database.', category="is-warning")
            return redirect("/blog/posts")
        return render_template("blog.html", postlist=postlist)    
    
    else:
        postlist = db.session.query(Post, User).join(User).order_by(Post.id.desc()).all()
    
    return render_template("blog.html", postlist=postlist)


@app.route("/blog/newpost", methods=['GET', 'POST'])
def newpost():
    if request.method == "GET":
        return render_template("newpost.html", title='', body='')
    
    if request.method == "POST":
        title = request.form['title']
        body = request.form['body']
        
        if title == '' or body == '':
            flash("Title and Body fields cannot be left blank", category="is-warning")
            return render_template("newpost.html", title=title, body=body)
        
        new_post = Post(title, body, logged_in_user())
        db.session.add(new_post)
        db.session.commit()
        flash("Success: New blog post published.", category="is-primary")
        return render_template('blog.html', postlist=db.session.query(Post, User).join(User).filter(Post.id == new_post.id).all())



###############################################
##################### MISC ####################
###############################################

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/web_caesar", methods=['GET', 'POST'])
def web_caesar():
    
    text = ''
    rot = 0
    
    if request.method == 'POST':
        text = request.form['text']
        rot = request.form['rot']
        
        if text == '' or rot == '':
            flash('Enter required values. Either rotation or plaintext area is blank.', category="is-warning")
            return render_template('web_caesar.html', text=text, rot=rot)

        try:
            text = caesar.encrypt(text, rot)
        except ValueError:
            flash('Numbers only for rotation value.', category="is-warning")

    return render_template('web_caesar.html', text=text, rot=rot)


if __name__ == "__main__":
    app.run()