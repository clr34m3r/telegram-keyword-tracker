# Telegram Channel Monitor

This project is a Telegram client that monitors specified channels for messages containing certain target words. When a target word is detected in a message, the client logs the message and prints an alert to the terminal.

## Features

- Monitors multiple Telegram channels.
- Tracks multiple target words.
- Logs messages containing target words to a JSON file.
- Prints alerts to the terminal.

## Prerequisites

- Python 3.6+
- Telethon library

## Setup

1. **Clone the repository:**

   ```sh
   git clone https://github.com/yourusername/telegram-channel-monitor.git
   cd telegram-channel-monitor
   ```
2. **Install the required packages:**
   ```sh
   pip install telethon
   ```
3. **Create a config.json file:**
   Create a config.json file in the root directory of the project with the following structure:
   ```sh
   {
       "api_id": "YOUR_API_ID",
       "api_hash": "YOUR_API_HASH",
       "target_words": ["word1", "word2"],
       "channel_ids": ["@channel1", "@channel2"]
   }
   ```
  Replace YOUR_API_ID and YOUR_API_HASH with your actual API ID and API Hash from my.telegram.org. Add the target words and channel IDs you want to monitor.
4. **Run the client:**
   ```sh
   python channel_getter.py
   ```
## Usage
   - The client will start and monitor the specified channels for messages containing the target words.
   - When a target word is detected, an alert will be printed to the terminal, and the message will be logged to alerts.json.
## Logging
   - Alerts are logged to alerts.json in the following format:
   ```sh
   [
       {
           "timestamp": "2023-10-01T12:34:56",
           "message": "example message containing target word",
           "alert": "Mentioned the word \"word1\": example message containing target word"
       }
   ]
   ```
## License
This project is licensed under the MIT License. See the LICENSE file for details.
