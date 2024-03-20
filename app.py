from flask import Flask, render_template, jsonify
from wandbinhood import *

app = Flask(__name__)
PATH_TO_CSV = 'projects/wandbinhood.csv'

@app.route('/')
def plot():
    return render_template('plot.html')

@app.route('/data')
def data():
    df = load_data(PATH_TO_CSV)  # Replace with the path to your CSV file
    plot_data_list = make_plots(df)
    return jsonify(project_name='', plot_data_list=plot_data_list)

if __name__ == '__main__':
    app.run(debug=True)
