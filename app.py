import dash 
import os 
from dash_bootstrap_components import themes

app = dash.Dash(__name__, external_stylesheets=[themes.DARKLY], suppress_callback_exceptions=True)
server = app.server
server.secret_key = os.environ.get('secret_key', 'secret')

app.title = 'Función Urbana Zona Metropolitana Mty'

