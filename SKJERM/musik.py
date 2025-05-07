import spotipy
from spotipy.oauth2 import SpotifyOAuth

# Sett inn dine egne verdier her:
CLIENT_ID = 'e52584f17679418a878ce05cb4583c99'
CLIENT_SECRET = '31d6f84a48b742be967a38ea3365e480'
REDIRECT_URI = 'http://127.0.0.1:8888/callback'

# Autorisasjon
scope = "user-read-playback-state user-modify-playback-state user-read-currently-playing"
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(
    client_id=CLIENT_ID,
    client_secret=CLIENT_SECRET,
    redirect_uri=REDIRECT_URI,
    scope=scope
))

# Hent køen (Spotify støtter dette via et skjult endepunkt!)
def get_queue():
    queue = sp._get("me/player/queue")  # Dette bruker intern API-vei
    upcoming = queue.get("queue", [])[:10]  # De neste 10 sangene
    if not upcoming:
        print("Ingen sanger i køen.")
        return

    print("🎶 Neste sanger i køen:")
    for idx, track in enumerate(upcoming, start=1):
        name = track["name"]
        artist = track["artists"][0]["name"]
        print(f"{idx}. {name} – {artist}")

get_queue()
