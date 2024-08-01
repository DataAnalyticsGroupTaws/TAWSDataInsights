from dash import Dash
import dash_bootstrap_components as dbc

# Inicializar la aplicación Dash
app = Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

# Importar layout de index.py
from index import layout

app.layout = layout

# Ejecutar la aplicación
if __name__ == '__main__':
    app.run_server(debug=True)