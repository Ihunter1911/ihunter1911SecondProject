from flask import jsonify
import pandas as pd
import numpy as np
from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
import psycopg2
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://kgi:@localhost/500_cities'
db= SQLAlchemy(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/about')
def about ():
    return render_template('about.html')

@app.route('/contact')
def contact ():
    return render_template('contact.html')

@app.route('/abseentism')
def abseentism ():
    return render_template('abseentism.html')

@app.route('/average_live_span_by_state')
def average_live_span_by_state ()
    return render_template('averagelifespanbystate.html')

@app.route('/display_city_data')
def display_data():
    df = pd.read_csv("db/CHDB_data_city_all v6_0.csv")
    df_dict= df.to_dict('records')
    resp = jsonify(df_dict)
    return resp

if __name__ == "__main__":
    app.run(debug=True)



