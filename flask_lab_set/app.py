from flask import Flask, render_template, request
from markupsafe import escape

app = Flask(__name__)

# 1) String modification routes
@app.route('/upper/<name>')
def upper(name):
    return name.upper()


@app.route('/lower/<name>')
def lower(name):
    return name.lower()


# Home + custom username page
@app.route('/')
def home_info():
    return (
        "Flask Lab Running ✅<br>"
        "Try: /upper/hardik, /lower/HARDIK, /form, /faculty, /user/alex"
    )


@app.route('/user/<username>')
def user_page(username):
    username = escape(username)
    return f"""
    <html>
      <head>
        <title>{username}'s Page</title>
        <link rel=\"stylesheet\" href=\"/static/style.css\"> 
      </head>
      <body>
        <div class=\"card\">
          <h1>Welcome, {username}!</h1>
          <p>This is your custom webpage.</p>
        </div>
      </body>
    </html>
    """


# 2) Template + form + request object
@app.route('/form', methods=['GET', 'POST'])
def form_page():
    if request.method == 'POST':
        name = request.form.get('name', '').strip()
        return render_template('result.html', name=name or 'Guest')
    return render_template('index.html')


# 3) Faculty table using template
@app.route('/faculty')
def faculty():
    faculty_data = [
        {'name': 'Dr. Sharma', 'subject': 'DBMS'},
        {'name': 'Prof. Verma', 'subject': 'AI'},
        {'name': 'Dr. Singh', 'subject': 'Networks'},
    ]
    return render_template('faculty.html', data=faculty_data)


if __name__ == '__main__':
    app.run(debug=True)
