# Telegram Keyword Tracker

This project is a Telegram client that monitors specified channels for messages containing certain target words. It is designed for use cases where you do not have permission to add a bot to the channel.

## Features

- Monitors multiple Telegram channels.
- Tracks multiple target words.
- Logs messages containing target words to a JSON file.

## Prerequisites

- Python 3.6+
- Telethon library

## Setup

1. **Clone the repository:**

   ```sh
   git clone https://github.com/clr34m3r/telegram-keyword-tracker.git
   cd telegram-keyword-tracker
   ```
2. **Install the required packages:**
   ```sh
   pip3 install telethon
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
   python3 keywork-tracker.py
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
## Use Case
   This project is particularly useful for scenarios where you need to monitor Telegram channels but do not have permission to add a bot. By using your own Telegram account, you can still track specific keywords or phrases in real-time across multiple channels.
## Example Use Cases
   - Security Monitoring: Track mentions of specific threats or vulnerabilities in security-focused Telegram channels.
   - Brand Monitoring: Monitor mentions of your brand or product in various Telegram communities.
   - Research: Collect data on specific topics or keywords for research purposes.
## License
This project is licensed under the MIT License. See the LICENSE file for details.
