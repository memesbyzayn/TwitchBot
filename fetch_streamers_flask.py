# from flask import Flask, render_template, request, redirect, url_for, jsonify, send_file
# import configparser
# import os
# import threading
# import subprocess
# import time
# import sqlite3
# import csv
# from datetime import datetime

# app = Flask(__name__)

# CONFIG_FILE = "CONFIG2.ini"
# DB_FILE = "streamers.db"

# # Initialize database
# def init_db():
#     conn = sqlite3.connect(DB_FILE)
#     cursor = conn.cursor()
#     cursor.execute('''
#         CREATE TABLE IF NOT EXISTS streamers (
#             id INTEGER PRIMARY KEY AUTOINCREMENT,
#             name TEXT,
#             viewers INTEGER,
#             language TEXT,
#             timestamp TEXT,
#             first_message_sent TEXT,
#             first_message_timestamp TEXT,
#             first_reply TEXT,
#             first_reply_timestamp TEXT,
#             second_message_sent TEXT,
#             second_reply TEXT,
#             second_reply_timestamp TEXT,
#             socials TEXT,
#             abandoned TEXT
#         )
#     ''')
#     conn.commit()
#     conn.close()

# init_db()

# # Fetch streamers from the database
# def get_streamers(from_date, to_date):
#     conn = sqlite3.connect(DB_FILE)
#     cursor = conn.cursor()
#     cursor.execute("""
#         SELECT name, viewers, language, timestamp, first_message_sent, first_message_timestamp, 
#                first_reply, first_reply_timestamp, second_message_sent, second_reply, 
#                second_reply_timestamp, socials, abandoned 
#         FROM streamers WHERE timestamp BETWEEN ? AND ?""", (from_date, to_date))
#     results = cursor.fetchall()
#     conn.close()
#     return results

# @app.route('/')
# def home():
#     return render_template("index.html")

# @app.route('/fetch_streamers', methods=["GET", "POST"])
# def fetch_streamers():
#     if request.method == "POST":
#         language = request.form["language"]
#         max_viewers = request.form["max_viewers"]
#         limit = request.form["limit"]
        
#         thread = threading.Thread(target=run_fetch_script, args=(language, max_viewers, limit))
#         thread.start()
#         return jsonify({"message": "Fetching started..."})
#     return render_template("fetch_streamers.html")

# def run_fetch_script(language, max_viewers, limit):
#     subprocess.run(["python", "fetch_streamers.py", "--language", language, "--max_viewers", max_viewers, "--limit", limit])

# @app.route('/download_db', methods=["GET"])
# def download_db():
#     from_date = request.args.get("from_date", "2000-01-01 00:00:00")
#     to_date = request.args.get("to_date", datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
#     streamers = get_streamers(from_date, to_date)
#     csv_filename = f"streamers_{datetime.now().strftime('%Y%m%d_%H%M%S')}.csv"
#     csv_path = os.path.join("temp", csv_filename)
#     os.makedirs("temp", exist_ok=True)
    
#     with open(csv_path, "w", newline="") as file:
#         writer = csv.writer(file)
#         writer.writerow(["Name", "Viewers", "Language", "Timestamp", "First Message Sent", "First Message Timestamp", 
#                          "First Reply", "First Reply Timestamp", "Second Message Sent", "Second Reply", 
#                          "Second Reply Timestamp", "Socials", "Abandoned"])
#         writer.writerows(streamers)
    
#     return send_file(csv_path, as_attachment=True)

# if __name__ == '__main__':
#     app.run(host="0.0.0.0", port=5000, debug=True)
