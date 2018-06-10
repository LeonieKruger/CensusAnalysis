import plotly.plotly as py
import plotly.graph_objs as go

import pandas as pd
df = pd.read_csv('/Users/leoniekruger/CencusData/Data/MapPlot.csv')
df.head()

cases = []
colors = ['rgb(93,206,175)','rgb(94,204,243)','rgb(78,103,200)']
type = {6: 'Housebreaking', 7: 'HomeRobbery', 8: 'TheftMotorVehicle'}

for i in range(6,9)[::-1]:
    cases.append(go.Scattergeo(
        lon = df[ df['Type'] == i ]['Lon'], #-(max(range(6,10))-i),
        lat = df[ df['Type'] == i ]['Lat'],
        text = df[ df['Type'] == i ]['Value'],
        name = type[i],
        marker = dict(
            size = df[ df['Type'] == i ]['Value']/3.5,
            color = colors[i-6],
            line = dict(width = 0)
        ),
    ) )

cases[0]['text'] = df[ df['Type'] == 8 ]['Value'].map('{:.0f}'.format).astype(str)+' '+ \
                   df[ df['Type'] == 8 ]['Country']
cases[0]['mode'] = 'markers+text'
cases[0]['textposition'] = 'bottom center'

inset = [
    go.Choropleth(
        locationmode = 'country names',
        locations = df[ df['Type'] == 9 ]['Country'],
        z = df[ df['Type'] == 8 ]['Value'],
        text = df[ df['Type'] == 8 ]['Country'],
        colorscale = [[0,'rgb(0, 0, 0)'],[1,'rgb(0, 0, 0)']],
        autocolorscale = False,
        showscale = False,
        geo = 'geo2'
    )
]

layout = go.Layout(
    title = 'Crimes in SA by type and province',
    geo = dict(
        resolution = 50,
        scope = 'africa',
        showframe = False,
        showcoastlines = True,
        showland = True,
        landcolor = "rgb(229, 229, 229)",
        countrycolor = "rgb(255, 255, 255)" ,
        coastlinecolor = "rgb(255, 255, 255)",
        projection = dict(
            type = 'Mercator'
        ),
        lonaxis = dict( range= [ -15.0, -5.0 ] ),
        lataxis = dict( range= [ 0.0, 12.0 ] ),
        domain = dict(
            x = [ 0, 1 ],
            y = [ 0, 1 ]
        )
    ),
    geo2 = dict(
        scope = 'africa',
        showframe = False,
        showland = False,
        landcolor = "rgb(229, 229, 229)",
        showcountries = False,
        domain = dict(
            x = [ 0, 0.6 ],
            y = [ 0, 0.6 ]
        ),
        bgcolor = 'rgba(255, 255, 255, 0.0)',
    ),
    legend = dict(
        traceorder = 'reversed'
    )
)

fig = go.Figure(layout=layout, data=cases+inset)
py.iplot(fig, validate=False, filename='Crimes South Africa 2018',fileopt='new')
i=110

# https://plot.ly/python/choropleth-maps/ Code generated with the help of
