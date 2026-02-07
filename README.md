# System Log Analysis & Security Event Detection

A Python-based web application that analyzes system log files to detect failed login attempts and identify suspicious activity.

## 🔐 Features
- Upload system log files (`.log`, `.txt`)
- Detect repeated failed login attempts
- Identify and flag high-risk IP addresses
- Display results in a clean web dashboard
- No log data is stored (privacy-focused design)

## 🚀 Live Demo
https://system-log-security-ak.streamlit.app/

## 🛠️ Tech Stack
- Python
- Streamlit
- Pandas

## 📂 How It Works
1. User uploads a system log file
2. Application analyzes login events
3. Failed login attempts are counted per IP
4. Suspicious IPs are flagged based on thresholds
5. Results are displayed instantly

## 🔒 Privacy & Security
Uploaded log files are processed temporarily and are not stored or shared.

## 👤 Author
Abdul Kalam
