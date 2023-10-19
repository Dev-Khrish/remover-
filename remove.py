import requests
from pyrogram import Client

# Your bot token and API credentials
BOT_TOKEN = '6028376714:AAEc-lTbdg0HypAgdXg2Wz3vMeI5WvRjORA'
API_ID = '23830477'
API_HASH = '19f8365d98fb11c9cd6c1eaa8b1fa4b8'
CHANNEL_ID = -1001604178274  # Replace with your channel ID (a negative integer)

# Initialize the Pyrogram client
app = Client('my_bot', bot_token=BOT_TOKEN, api_id=API_ID, api_hash=API_HASH)

# Function to remove all members from the channel
def remove_all_members():
    try:
        # Use the Bot API to get chat members
        url = f"https://api.telegram.org/bot{BOT_TOKEN}/getChatMembers?chat_id={CHANNEL_ID}"
        response = requests.get(url)
        data = response.json()
        members = data['result']

        for member in members:
            user_id = member['user']['id']
            user_name = member['user']['first_name']
            # Kick the user using the Bot API
            kick_url = f"https://api.telegram.org/bot{BOT_TOKEN}/kickChatMember?chat_id={CHANNEL_ID}&user_id={user_id}"
            kick_response = requests.get(kick_url)
            print(f"Kicked user: {user_name} (ID: {user_id})")

    except Exception as e:
        print(f"Error removing members: {e}")

if __name__ == "__main__":
    app.start()
    remove_all_members()
    app.stop()
