from flask import Flask
app = Flask(__name__)

@app.route('/')
def resume():
    return render_template('home.html')

@app.route('home')
def home():
    return render_template('home.html')

@app.route('about')
def about():
    return render_template('about.html')

@app.route('/courses')
def courses():
    courses = [
        'MISY160'
        'MISY330'
        'MISY350'
    ]
    return render_template('courses.html', courses=courses)

if __name__ == '__main__':
    app.run()
