import streamlit as st
import pandas as pd

# ------------------ TITLE ------------------
st.title("System Log Analysis & Security Event Detection")
st.write("Upload your log file to analyze failed login attempts and detect suspicious activity.")

# ------------------ FILE UPLOAD ------------------
uploaded_file = st.file_uploader(
    "Choose a log file",
    type=["log", "txt"]
)

# ------------------ PROCESS LOG FILE ------------------
if uploaded_file is not None:
    failed_count = {}

    # Read file content
    lines = uploaded_file.read().decode("utf-8").splitlines()

    # Analyze each line
    for line in lines:
        if "FAILED" in line:
            parts = line.split()
            ip = parts[1].split("=")[1]

            if ip in failed_count:
                failed_count[ip] += 1
            else:
                failed_count[ip] = 1

    # ------------------ RESULTS ------------------
    st.subheader("Failed Login Count per IP")
    st.write(failed_count)

    # ------------------ TABLE VIEW ------------------
    table_data = []
    for ip, count in failed_count.items():
        table_data.append({
            "IP Address": ip,
            "Failed Login Attempts": count
        })

    df = pd.DataFrame(table_data)
    st.subheader("Failed Login Attempts (Table View)")
    st.table(df)

    # ------------------ SUSPICIOUS IP DETECTION ------------------
    st.subheader("Suspicious / High Risk IPs")

    found_risk = False
    for ip, count in failed_count.items():
        if count >= 3:
            st.error(f"High Risk IP Detected: {ip} (Failed Attempts: {count})")
            found_risk = True

    if not found_risk:
        st.success("No high-risk IPs detected.")

    # ------------------ PRIVACY NOTICE ------------------
    st.info("Uploaded log files are processed temporarily and are not stored.")
