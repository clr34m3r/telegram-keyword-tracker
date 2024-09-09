import json
import logging
from telethon import TelegramClient, events

# Read configuration from the JSON file
with open('config.json', 'r') as config_file:
    config = json.load(config_file)

API_ID = config['api_id']
API_HASH = config['api_hash']
TARGET_WORDS = [word.lower() for word in config['target_words']]
CHANNEL_IDS = config['channel_ids']

# Configure logging for easier debugging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)

# Create the client and connect
client = TelegramClient('session_name', API_ID, API_HASH)

@client.on(events.NewMessage(chats=CHANNEL_IDS))
async def handle_message(event):
    message_text = event.message.message.lower()
    for target_word in TARGET_WORDS:
        if target_word in message_text:
            alert_message = f'Mentioned the word "{target_word}": {message_text}'
            
            # Print alert to the terminal
            print(alert_message)
            
            # Create log entry
            log_entry = {
                'timestamp': event.message.date.isoformat(),
                'message': message_text,
                'alert': alert_message
            }
            
            # Load existing log entries if the file exists
            try:
                with open('alerts.json', 'r') as log_file:
                    try:
                        log_entries = json.load(log_file)
                    except json.JSONDecodeError:
                        log_entries = []
            except FileNotFoundError:
                log_entries = []
            
            # Append the new log entry
            log_entries.append(log_entry)
            
            # Write log entries to a JSON file
            with open('alerts.json', 'w') as log_file:
                json.dump(log_entries, log_file, indent=4)
            break  # No need to check other words if one is found

async def main():
    # Start the client
    await client.start()
    print("Client is running...")
    await client.run_until_disconnected()

if __name__ == '__main__':
    import asyncio
    asyncio.run(main())
