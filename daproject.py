import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

# Tus credenciales de la app de Spotify
CLIENT_ID = '04afb9a4dfc34a2ba6ab9fefc30358b5'
CLIENT_SECRET = '44ef46e579df499c8a155933264a04fb'

# Autenticación con Client Credentials Flow
auth_manager = SpotifyClientCredentials(client_id=CLIENT_ID, client_secret=CLIENT_SECRET)
sp = spotipy.Spotify(auth_manager=auth_manager)

# Prueba: buscar a Bad Bunny, imprimir si se encuentra
resultado = sp.search(q='Bad Bunny', type='artist', limit=1)
print(resultado['artists']['items'][0]['name'])
# Imprime
