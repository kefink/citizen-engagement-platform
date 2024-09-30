from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/report', methods=['POST'])
def report():
    issue = request.form['issue']
    location = request.form['location']
    return render_template('report.html', issue=issue, location=location)

if __name__ == "__main__":
    app.run(debug=True)
