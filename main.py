import os
import random
import spotipy
from spotipy.oauth2 import SpotifyOAuth
from dotenv import load_dotenv
import schedule
import time
import requests

load_dotenv()

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(
    scope="user-library-read playlist-read-private",
    show_dialog=True
))

TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
TELEGRAM_CHAT_ID = os.getenv("TELEGRAM_CHAT_ID")

def send_telegram_message(message):
    url = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage"
    payload = {
        "chat_id": TELEGRAM_CHAT_ID,
        "text": message,
        "parse_mode": "Markdown"
    }
    response = requests.post(url, data=payload)
    if response.status_code != 200:
        print(f"❌ Telegram send error: {response.text}")

def fetch_and_send_random_song():
    try:
        results = sp.current_user_saved_tracks(limit=50)
        tracks = results['items']

        if not tracks:
            message = "⚠️ No liked songs found in your Spotify!"
            send_telegram_message(message)
            print(message)
            return

        random_track = random.choice(tracks)['track']
        song_name = random_track['name']
        artist_name = random_track['artists'][0]['name']
        spotify_url = random_track['external_urls']['spotify']

        message = (
            f"🎶 *Today's Random Song:*\n"
            f"*Song:* {song_name}\n"
            f"*Artist:* {artist_name}\n"
            f"[Listen on Spotify]({spotify_url})"
        )

        send_telegram_message(message)
        print(f"✅ Sent: {song_name} by {artist_name}")

    except Exception as e:
        error_message = f"❌ Error: {str(e)}"
        send_telegram_message(error_message)
        print(error_message)

schedule.every().day.at("14:00").do(fetch_and_send_random_song)

print("GG is running...")

while True:
    schedule.run_pending()
    time.sleep(60)