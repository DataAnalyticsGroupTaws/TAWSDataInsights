from dash import html, dcc
import pandas as pd
import plotly.express as px

# Leer datos
df = pd.read_csv('data/materias.csv')

# Crear visualización
fig = px.bar(df, x='Semestre', y='Frecuencia', color='Materia', title='Distribución de Materias por Semestre')

# Definir el layout de la aplicación
layout = html.Div(children=[
    html.H1(children='Análisis de Materias Cursadas'),

    html.Div(children='''
        Distribución de las materias cursadas por los miembros del club TAWS.
    '''),

    dcc.Graph(
        id='example-graph',
        figure=fig
    )
])