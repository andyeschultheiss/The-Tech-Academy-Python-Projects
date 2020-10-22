from flask import Flask, render_template
from data import scrape_poll_data

app = Flask(__name__)

@app.route('/')
def presidential_poll_dashboard():
    pollster_data_array = scrape_poll_data()
    return render_template('home.html', pollster_data_array = pollster_data_array)

if __name__ == '__main__':
    app.run()