# 🎵 Spotipy Telegram Daily Song Bot

A Python bot that sends you a **random liked song from your Spotify library to your Telegram daily**, helping you rediscover your music automatically.

Built with:
- [Spotipy](https://spotipy.readthedocs.io/) for Spotify API.
- Telegram Bot API for delivery.
- Railway (or local scheduling) for automation.

---

## 🚀 Features

✅ Fetches a **random liked song from your Spotify library** daily.  
✅ Sends it automatically to your **Telegram**.  
✅ Uses **CRON scheduling on Railway for 24/7 delivery** without keeping your PC on.  
✅ Easy to extend with genre-based picks, Discord delivery, or playlist creation.

---

## 🗂️ Project Structure

```
daily-song-bot/
├── main.py            # Main script for fetching and sending songs
├── requirements.txt   # Dependencies
├── .gitignore         # Ignores .env and __pycache__
├── .env               # Your API keys (DO NOT COMMIT)
└── sample.env         # Template for environment variables
```

---

## ⚙️ Setup Locally

### 1️⃣ Clone the repository

```
git clone https://github.com/<your_username>/daily-song-bot.git
cd daily-song-bot
```

---

### 2️⃣ Install dependencies

```
pip install -r requirements.txt
```

---

### 3️⃣ Add environment variables

- Copy `sample.env` ➔ `.env`.
- Fill with your Spotify and Telegram credentials:

```
SPOTIPY_CLIENT_ID=your_client_id_here
SPOTIPY_CLIENT_SECRET=your_client_secret_here
SPOTIPY_REDIRECT_URI=http://localhost:8888/callback
TELEGRAM_BOT_TOKEN=your_telegram_bot_token_here
TELEGRAM_CHAT_ID=your_chat_id_here
```

---

### 4️⃣ Run the bot manually for testing

```
python main.py
```

✅ You should receive a **random liked song in your Telegram**.

---

## 🚀 Deploy on Railway

✅ Allows **automatic daily delivery without your PC on**.

1️⃣ Push your project to GitHub (excluding your `.env`).  
2️⃣ Create a **new project on [Railway](https://railway.app)** → “Deploy from GitHub.”  
3️⃣ Add your environment variables in Railway’s “Variables” tab.  
4️⃣ Set up a **Schedule**:
- **Cron:** `0 2 * * *` (daily at 7:30 AM IST; adjust as needed).
- **Command:** `python main.py`

✅ Your bot will now **run daily automatically**, sending you a song on Telegram.

---

## 🪐 Future Extensions

✅ Genre-based or mood-based daily picks.  
✅ Automatically add each day’s pick to a Spotify playlist.  
✅ Parallel delivery to Discord.  
✅ Logging sent songs to `.csv` for personal analytics.

---

## 🤝 Contributing

Pull requests are welcome for:
- Feature additions (genre filters, playlist builder).
- Deployment enhancements.
- Code cleanups.

---

## 🌟 Acknowledgements

- [Spotipy](https://spotipy.readthedocs.io/)
- [Telegram Bot API](https://core.telegram.org/bots/api)
- [Railway](https://railway.app/)

---

## 🎶 Enjoy rediscovering your music daily!
