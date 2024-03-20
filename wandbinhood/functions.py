import plotly.graph_objs as go
import plotly.io as pio
import base64
import pandas as pd

PATH_TO_LOGS = './projects'

def load_data(path):
    df = pd.read_csv(path)
    return df

def generate_plot(df, column):
    x = df['Epoch']
    y = df[column]

    # Get the last element of y
    curr_price = y.iloc[-1]
    curr_price = f"{abs(curr_price):.3f}" 

    # Determine the color based on the first and last elements of y
    color = '#28A12F' if y.iloc[0] < y.iloc[-1] else '#FF0000'
    
    # Create the plot trace
    trace = go.Scatter(x=x, y=y, mode='lines', line=dict(color=color, width=4))
    change = y.iloc[-1] - y.iloc[-2]
    sign = f"▲ ${abs(change):.3f}" if change >= 0 else f"▼ ${abs(change):.3f}"
    change_color =  '#28A12F' if change > 0 else '#FF0000'

    # Increase the width of the line in the trace
    layout = go.Layout(
        title=dict( text=f"<span style='font-size:58;'>{column}<br><br>{curr_price} </span><span style='font-size:28px; color:{change_color};'>{sign}</span>",
                    font=dict(family='Helvetica',color='white', size=30)),
        xaxis=dict(title='', color='gray', showgrid=False, zeroline=False, tickfont=dict(size=28)), 
        yaxis=dict(title='', color='gray', showgrid=False, zeroline=False, tickfont=dict(size=28)),
        plot_bgcolor='black',
        paper_bgcolor='black',
        margin=dict(l=100, r=100, t=200, b=100)
    )

    # Create the figure
    fig = go.Figure(data=[trace], layout=layout)
    plot_data = pio.to_image(fig, format='png', width=1200, height=800, scale=2)
    return plot_data

def make_plots(df):
    plot_data_list = []
    for column in df.columns:
        if column != 'Epoch':
            plot_data = generate_plot(df, column)
            plot_data_base64 = base64.b64encode(plot_data).decode('utf-8')
            plot_data_list.append({'column': column, 'plot_data': plot_data_base64})
    return plot_data_list

def create_project(name, fields, path='', overwrite=False):
    df = pd.DataFrame(columns=['Epoch']+fields)
    PATH_TO_LOGS = PATH_TO_LOGS if path == '' else path
    if overwrite:
        df.to_csv(f'{PATH_TO_LOGS}/{name}.csv', index=False)
    print("Project initalized, lets gamble!")

def append_project(name,fields, path=''):
    # Load the existing data
    PATH_TO_LOGS = PATH_TO_LOGS if path == '' else path
    df = pd.read_csv(f'{PATH_TO_LOGS}/{name}.csv')
    # Extract the number of columns in the DataFrame
    num_columns = len(df.columns)
    # Check that the number of fields matches the number of columns in the DataFrame
    assert len(fields) == num_columns - 1, "The number of fields does not match the number of columns in the DataFrame."
    # Append the records to the DataFrame
    df.loc[len(df)] = [len(df)+ 1]+fields 
    # Save the updated DataFrame
    df.to_csv(f'{PATH_TO_LOGS}/{name}.csv', index=False)