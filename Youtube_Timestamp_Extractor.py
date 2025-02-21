import re
import os
import googleapiclient.discovery
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
from urllib.parse import parse_qs, urlparse

def get_video_id(youtube_url):
    """Extract the video ID from a YouTube URL"""
    parsed_url = urlparse(youtube_url)
    if parsed_url.hostname in ('youtu.be',):
        return parsed_url.path[1:]
    if parsed_url.hostname in ('www.youtube.com', 'youtube.com'):
        if parsed_url.path == '/watch':
            return parse_qs(parsed_url.query)['v'][0]
        if parsed_url.path.startswith('/embed/'):
            return parsed_url.path.split('/')[2]
        if parsed_url.path.startswith('/v/'):
            return parsed_url.path.split('/')[2]
    return None

def extract_timestamps(youtube_url, api_key):
    """Extract timestamps from YouTube video description using the YouTube Data API"""
    video_id = get_video_id(youtube_url)
    if not video_id:
        return []
    
    # Initialize the YouTube API client
    youtube = googleapiclient.discovery.build('youtube', 'v3', developerKey=api_key)
    
    # Get video details including description
    request = youtube.videos().list(
        part="snippet",
        id=video_id
    )
    response = request.execute()
    
    if not response['items']:
        return []
    
    # Extract description
    description = response['items'][0]['snippet']['description']
    
    # Extract timestamps using regex
    # This pattern looks for time formats like 0:00, 00:00, or 00:00:00
    timestamp_pattern = r'(?:^|\n)(?P<timestamp>\d+:\d+(?::\d+)?)\s+(?P<description>.+)'
    timestamps = re.finditer(timestamp_pattern, description, re.MULTILINE)
    
    # Format the timestamps
    formatted_timestamps = []
    for match in timestamps:
        timestamp = match.group('timestamp')
        desc = match.group('description')
        formatted_timestamps.append(f"{timestamp} - {desc}")
    
    return formatted_timestamps

def save_timestamps_to_file(timestamps, filename="timestamps.txt"):
    """Save extracted timestamps to a text file"""
    with open(filename, "w", encoding="utf-8") as file:
        file.write("Timestamps found in the video:\n\n")
        for timestamp in timestamps:
            file.write(f"{timestamp}\n")
    return filename

def send_email(sender_email, sender_password, receiver_email, subject, body, attachment_path):
    """Send email with timestamps file attachment"""
    # Create a multipart message
    message = MIMEMultipart()
    message["From"] = sender_email
    message["To"] = receiver_email
    message["Subject"] = subject
    
    # Add body to email
    message.attach(MIMEText(body, "plain"))
    
    # Open file in binary mode
    with open(attachment_path, "rb") as attachment:
        # Add file as application/octet-stream
        part = MIMEBase("application", "octet-stream")
        part.set_payload(attachment.read())
    
    # Encode file in ASCII characters to send by email    
    encoders.encode_base64(part)
    
    # Add header as key/value pair to attachment part
    part.add_header(
        "Content-Disposition",
        f"attachment; filename= {os.path.basename(attachment_path)}",
    )
    
    # Add attachment to message
    message.attach(part)
    
    # Convert message to string
    text = message.as_string()
    
    # Log in to server using secure context and send email
    try:
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()
        server.login(sender_email, sender_password)
        server.sendmail(sender_email, receiver_email, text)
        server.quit()
        return True
    except Exception as e:
        print(f"Error sending email: {e}")
        return False

def main():
    # Get YouTube URL from user
    youtube_url = input("Enter the YouTube video URL: ")
    
    # Get API key - you'll need to obtain this from Google Cloud Console
    api_key = input("Enter your YouTube Data API key: ")
    
    # Extract timestamps
    timestamps = extract_timestamps(youtube_url, api_key)
    
    if not timestamps:
        print("No timestamps found in the video description.")
        return
    
    print(f"Found {len(timestamps)} timestamps!")
    
    # Save timestamps to file
    filename = save_timestamps_to_file(timestamps)
    
    # Email configuration
    sender_email = input("Enter your email address: ")
    sender_password = input("Enter your email password (or app password): ")
    receiver_email = input("Enter recipient email address: ")
    subject = "YouTube Video Timestamps"
    body = f"Attached are the timestamps extracted from: {youtube_url}"
    
    # Send email
    success = send_email(sender_email, sender_password, receiver_email, subject, body, filename)
    
    if success:
        print(f"Email with timestamps successfully sent to {receiver_email}")
    else:
        print("Failed to send email. Check your credentials and try again.")

if __name__ == "__main__":
    main()