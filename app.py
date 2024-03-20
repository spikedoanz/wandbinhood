from flask import Flask, render_template, jsonify
import numpy as np
import plotly.graph_objs as go
import plotly.io as pio
import base64
import time

app = Flask(__name__)

def generate_data(t):
    x = np.arange(10000)/100
    y = np.sin(x[:t])
    time.sleep(0.01)
    return x, y

def time_step():
    for i in range(10000):
        yield i

TIME_STEP = time_step()

def generate_plot(t):
    # Generate the plot data
    x, y = generate_data(t)
    
    # Create the plot trace
    trace = go.Scatter(x=x, y=y, line=dict(color='#28A12F', width=2))
    
    # Create the layout
    layout = go.Layout(
        title=dict(text='Validation Accuracy', x=0.05, y=0.95, font=dict(color='white')),
        xaxis=dict(title='', color='black', showgrid=False, zeroline=False),
        yaxis=dict(title='Value', color='white', showgrid=False, zeroline=False),
        plot_bgcolor='black',
        paper_bgcolor='black',
        margin=dict(l=50, r=20, t=30, b=50)
    )
    
    # Create the figure
    fig = go.Figure(data=[trace], layout=layout)
    
    # Convert the plot to a PNG image
    plot_data = pio.to_image(fig, format='png')
    
    return plot_data

@app.route('/')
def plot():
    return render_template('plot.html')


@app.route('/data')
def data():
    t = next(TIME_STEP) # Simulate increasing time steps
    plot_data = generate_plot(t)
    plot_data_base64 = base64.b64encode(plot_data).decode('utf-8')
    return jsonify(plot_data=plot_data_base64)

if __name__ == '__main__':
    app.run(debug=True)
