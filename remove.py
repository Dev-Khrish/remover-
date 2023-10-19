from pyrogram import Client, filters

# Your bot token and API credentials
BOT_TOKEN = '6028376714:AAEc-lTbdg0HypAgdXg2Wz3vMeI5WvRjORA'
API_ID = '23830477'
API_HASH = '19f8365d98fb11c9cd6c1eaa8b1fa4b8'
CHANNEL_ID = -1001604178274  # Replace with your channel ID (a negative integer)

# Initialize the Pyrogram client
app = Client('my_bot', bot_token=BOT_TOKEN, api_id=API_ID, api_hash=API_HASH)

# Function to remove all members from the channel
async def remove_all_members(client, chat_id):
    try:
        async with app.with_chats([chat_id]):
            chat_members = await client.iter_chat_members(chat_id)
            for member in chat_members:
                if member.status not in ["creator", "administrator"]:
                    await client.kick_chat_member(chat_id, member.user.id)
                    print(f"Kicked user: {member.user.username}")
    except Exception as e:
        print(f"Error removing members: {e}")

if __name__ == "__main__":
    app.start()
    app.loop.run_until_complete(remove_all_members(app, CHANNEL_ID))
    app.stop()
