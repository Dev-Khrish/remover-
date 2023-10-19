from pyrogram import Client, filters

# Your bot token and API credentials
BOT_TOKEN = '6028376714:AAEc-lTbdg0HypAgdXg2Wz3vMeI5WvRjORA'
API_ID = '23830477'
API_HASH = '19f8365d98fb11c9cd6c1eaa8b1fa4b8'
CHANNEL_ID = -1001604178274  # Replace with your channel ID (a negative integer)

# List of user IDs to remove from the channel
users_to_remove = [123, 456, 789]  # Replace with the user IDs you want to remove

# Initialize the Pyrogram client
app = Client('my_bot', bot_token=BOT_TOKEN, api_id=API_ID, api_hash=API_HASH)

# Function to remove specific members from the channel
async def remove_specific_members(client, chat_id):
    try:
        for user_id in users_to_remove:
            await client.kick_chat_member(chat_id, user_id)
            print(f"Kicked user with ID: {user_id}")
    except Exception as e:
        print(f"Error removing members: {e}")

if __name__ == "__main__":
    app.start()
    app.loop.run_until_complete(remove_specific_members(app, CHANNEL_ID))
    app.stop()
