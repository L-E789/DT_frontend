from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/register')
def register():
    return render_template('index.html')

@app.route('/login')
def login():
    return render_template('index.html')

@app.route('/activated-account/<int:id>')
def activated_account(id):
    return render_template('index.html')

@app.route('/recovery/<int:id>')
def recoveryid(id):
    return render_template('index.html')

@app.route('/recovery')
def recovery():
    return render_template('index.html')

@app.route('/consult')
def consult():
    return render_template('index.html')

@app.route('/environments')
def environments():
    return render_template('index.html')

@app.route('/profile')
def profile():
    return render_template('index.html')

@app.route('/environments/users/<int:id>')
def environments_users(id):
    return render_template('index.html')

@app.route('/about-us')
def about_us():
    return render_template('index.html')

@app.route('/environment/<int:id>')
def environment(id):
    return render_template('index.html')

@app.route('/environment/join/<code>')
def environment_join(code):
    return render_template('index.html')

@app.route('/environments/report/<int:id>')
def environment_report(id):
    return render_template('index.html')

@app.route('/contact_us')
def contact_us():
    return render_template('index.html')

@app.route('/3RjZgfU&rZVRLC7fzTNf1IRgxRFPvQ5G1ekFXJZ9/Sd89AsYwD912')
def login_admin():
    return render_template('index.html')


if __name__ == '__main__':
    app.run()