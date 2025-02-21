# YouTube Timestamp Extractor

A Python tool that extracts timestamps from YouTube video descriptions and emails them as a text file.

## 📝 Description

This tool uses the YouTube Data API to extract timestamps from any YouTube video description based on the video URL. It then formats the timestamps, saves them to a text file, and emails the file to a specified recipient.

## ✨ Features

- Extract timestamps from any YouTube video using just the URL
- No browser automation required (uses YouTube Data API)
- Automatically identifies common timestamp formats (0:00, 00:00, 00:00:00)
- Saves formatted timestamps to a text file
- Emails the extracted timestamps to any recipient

## 🛠️ Installation

### Prerequisites

- Python 3.6 or higher
- A Google account with YouTube Data API access
- An email account for sending the timestamps

### Setup

1. Clone this repository:
```bash
git clone https://github.com/KalyanRajSahu-Snap/Youtube-Timestamp-Extractor.git
cd Youtube-Timestamp-Extractor
```

2. Install the required packages:
```bash
pip install google-api-python-client
```

3. Get a YouTube Data API key:
   - Go to the [Google Cloud Console](https://console.cloud.google.com/)
   - Create a new project
   - Enable the YouTube Data API v3
   - Create an API key under "APIs & Services" > "Credentials"

## 🚀 Usage

Run the script from the command line:

```bash
python Youtube_Timestamp_Extractor.py
```

Follow the prompts to enter:
1. The YouTube video URL
2. Your YouTube Data API key
3. Your email address
4. Your email password (or app password)
5. The recipient's email address

### Using Gmail

If you're using Gmail to send the email:
1. Enable 2-step verification on your Google account
2. Generate an app password:
   - Go to your [Google Account settings](https://myaccount.google.com/)
   - Navigate to Security > App passwords
   - Select "Mail" and your device
   - Use the generated 16-character password when prompted

## 🧩 How It Works

1. The script extracts the video ID from the YouTube URL
2. It uses the YouTube Data API to fetch the video description
3. Regular expressions identify timestamp patterns in the description
4. Timestamps are formatted and saved to a text file
5. The file is attached to an email and sent to the specified recipient

## 🔍 Example Output

The resulting text file will look something like this:

```
Timestamps found in the video:

0:00 - Introduction
1:23 - First topic
4:56 - Second topic
10:32 - Conclusion
```

## ⚠️ Limitations

- The script can only extract timestamps that follow common formats
- YouTube Data API has usage quotas (10,000 units per day for free tier)
- Some email providers may block automated emails

## 🤝 Contributing

Contributions are welcome! Feel free to:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 🙏 Acknowledgements

- [Google for the YouTube Data API](https://developers.google.com/youtube/v3)
- [Python Email Documentation](https://docs.python.org/3/library/email.html)
