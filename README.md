# README: YouTube Timestamp Extractor

This Python script extracts timestamps from YouTube videos and sends them as an email attachment using Gmail's SMTP server.

---

## Features

- Extract timestamps from YouTube videos.
- Send the extracted timestamps as a file attachment via email.
- Supports Gmail's SMTP server.

---

## Prerequisites

1. **Python Installed**:
   Ensure Python 3.x is installed on your system.

   ```bash
   python --version
   ```

2. **Required Libraries**:
   Install the necessary Python libraries by running:

   ```bash
   pip install smtplib email
   ```

3. **Gmail SMTP Access**:
   Ensure your Gmail account has access to SMTP:

   - Enable "Allow Less Secure Apps" or generate an **App Password**.

---

## How to Download and Use

### **Step 1: Clone or Download**

Download the Python script file:

```bash
git clone https://github.com/yourusername/youtube-timestamp-extractor.git
cd youtube-timestamp-extractor
```

Alternatively, download the script directly as a ZIP file and extract it.

### **Step 2: Modify the Script**

Open the script file and replace the placeholder values:

#### Replace Sender's Credentials:

```python
sender_email = "your-email@gmail.com"
sender_password = "your-app-password"
```

#### Replace Receiver's Email Address:

```python
receiver_email = "receiver-email@example.com"
```

#### Replace File Path:

Ensure the file path to the attachment is valid. For example:

```python
file_path = "/path/to/your/timestamps.txt"
```

---

### **Step 3: Run the Script**

Run the Python script using the following command:

```bash
python send_email_with_attachment.py
```

---

## Notes

- **Security**:
  - Use an **App Password** instead of your Gmail account password.
  - Avoid hardcoding sensitive information; use environment variables instead.
- **Attachment File**:
  Ensure the specified file exists at the given path.

---

## Troubleshooting

- **SMTP Authentication Error**:
  - Ensure SMTP is enabled in your Gmail account settings.
  - Double-check your app password and email.
- **File Not Found Error**:
  - Verify the file path is correct and the file exists.

---

## Example Use Case

Suppose you want to extract timestamps from a YouTube video and email them to a collaborator. Update the `file_path` to point to the file containing the timestamps, replace the email addresses, and run the script to send it effortlessly.

---

Feel free to fork and customize this script for your specific needs!

