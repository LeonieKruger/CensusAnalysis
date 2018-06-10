import plotly.plotly as py
import plotly.graph_objs as go

import pandas as pd
import math

data = pd.read_csv("/Users/leoniekruger/CencusData/Data/BubbleCrimeData.csv")
hover_text = []
bubble_size = []

for index, row in data.iterrows():
    hover_text.append('test')
    bubble_size.append(row['Total'])

data['text'] = hover_text
data['size'] = bubble_size
sizeref = 2.*max(data['size'])/(100**2)

trace0 = go.Scatter(
    x=df_2007['gdpPercap'][df_2007['continent'] == 'Africa'],
    y=df_2007['lifeExp'][df_2007['continent'] == 'Africa'],
    mode='markers',
    name='Africa',
    text=df_2007['text'][df_2007['continent'] == 'Africa'],
    marker=dict(
        symbol='circle',
        sizemode='area',
        sizeref=sizeref,
        size=df_2007['size'][df_2007['continent'] == 'Africa'],
        line=dict(
            width=2
        ),
    )
)
trace1 = go.Scatter(
    x=df_2007['gdpPercap'][df_2007['continent'] == 'Americas'],
    y=df_2007['lifeExp'][df_2007['continent'] == 'Americas'],
    mode='markers',
    name='Americas',
    text=df_2007['text'][df_2007['continent'] == 'Americas'],
    marker=dict(
        sizemode='area',
        sizeref=sizeref,
        size=df_2007['size'][df_2007['continent'] == 'Americas'],
        line=dict(
            width=2
        ),
    )
)
trace2 = go.Scatter(
    x=df_2007['gdpPercap'][df_2007['continent'] == 'Asia'],
    y=df_2007['lifeExp'][df_2007['continent'] == 'Asia'],
    mode='markers',
    name='Asia',
    text=df_2007['text'][df_2007['continent'] == 'Asia'],
    marker=dict(
        sizemode='area',
        sizeref=sizeref,
        size=df_2007['size'][df_2007['continent'] == 'Asia'],
        line=dict(
            width=2
        ),
    )
)
trace3 = go.Scatter(
    x=df_2007['gdpPercap'][df_2007['continent'] == 'Europe'],
    y=df_2007['lifeExp'][df_2007['continent'] == 'Europe'],
    mode='markers',
    name='Europe',
    text=df_2007['text'][df_2007['continent'] == 'Europe'],
    marker=dict(
        sizemode='area',
        sizeref=sizeref,
        size=df_2007['size'][df_2007['continent'] == 'Europe'],
        line=dict(
            width=2
        ),
    )
)
trace4 = go.Scatter(
    x=df_2007['gdpPercap'][df_2007['continent'] == 'Oceania'],
    y=df_2007['lifeExp'][df_2007['continent'] == 'Oceania'],
    mode='markers',
    name='Oceania',
    text=df_2007['text'][df_2007['continent'] == 'Oceania'],
    marker=dict(
        sizemode='area',
        sizeref=sizeref,
        size=df_2007['size'][df_2007['continent'] == 'Oceania'],
        line=dict(
            width=2
        ),
    )
)

data = [trace0, trace1, trace2, trace3, trace4]
layout = go.Layout(
    title='Life Expectancy v. Per Capita GDP, 2007',
    xaxis=dict(
        title='GDP per capita (2000 dollars)',
        gridcolor='rgb(255, 255, 255)',
        range=[2.003297660701705, 5.191505530708712],
        type='log',
        zerolinewidth=1,
        ticklen=5,
        gridwidth=2,
    ),
    yaxis=dict(
        title='Life Expectancy (years)',
        gridcolor='rgb(255, 255, 255)',
        range=[36.12621671352166, 91.72921793264332],
        zerolinewidth=1,
        ticklen=5,
        gridwidth=2,
    ),
    paper_bgcolor='rgb(243, 243, 243)',
    plot_bgcolor='rgb(243, 243, 243)',
)

fig = go.Figure(data=data, layout=layout)
py.iplot(fig, filename='life-expectancy-per-GDP-2007')