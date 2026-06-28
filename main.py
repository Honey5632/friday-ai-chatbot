import os
import pathlib
from flask import Flask, render_template, request, jsonify
from google import genai
from google.genai import types

app = Flask(__name__)

# Directory where files will sit temporarily before being pushed to Gemini
UPLOAD_FOLDER = pathlib.Path("temp_flask_uploads")
UPLOAD_FOLDER.mkdir(exist_ok=True)

try:
    with open("api_file", 'r') as api:
        google_api = api.read().strip()
    client = genai.Client(api_key=google_api)

    friday_config = types.GenerateContentConfig(
        system_instruction=(
            "You are FRIDAY, the advanced AI operating system. "
            "Address the user as 'Honey'. When a file or image is passed through your core data feeds, "
            "acknowledge that you are tracking the matrix stream and scan the attachment to answer "
            "the request sharply and intelligently."
        ),
        temperature=0.7
    )
    chat = client.chats.create(model="gemini-3.5-flash", config=friday_config)
except FileNotFoundError:
    print("CRITICAL: Key token asset 'api_file' missing.")
    client = None


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/ask_friday', methods=['POST'])
def ask_friday():
    if not client:
        return jsonify({"response": "Mainframe offline. Key array missing, Sir."}), 500

    # 1. Capture the text prompt from the form data payload
    user_message = request.form.get('message', '').strip()

    # 2. Check for file attachment streams inside the request
    uploaded_file = request.files.get('file')

    payload = []

    if uploaded_file and uploaded_file.filename != '':
        try:
            # Securely cache the file to the local directory temporarily
            file_path = UPLOAD_FOLDER / uploaded_file.filename
            uploaded_file.save(str(file_path))

            # Transfer the file structure directly into Gemini secure sandbox cloud
            gemini_file = client.files.upload(file=file_path)
            payload.append(gemini_file)

            # Wipe local storage file trace immediately
            file_path.unlink()

        except Exception as file_err:
            return jsonify({"response": f"Failed compiling data stream packet: {str(file_err)}"}), 500

    # Add text context if the user provided text alongside the file
    if user_message:
        payload.append(user_message)
    elif len(payload) == 1:
        # If a file was uploaded with zero text instruction
        payload.append("Analyze this uploaded data stream completely, Boss.")
    else:
        return jsonify({"response": "Awaiting active input command matrix, Boss."})

    try:
        # Transmit compiled multimodal arrays to the conversational engine
        response = chat.send_message(payload)
        return jsonify({"response": response.text})
    except Exception as e:
        return jsonify({"response": f"Core execution runtime fault: {str(e)}"}), 500


if __name__ == '__main__':
    app.run(debug=True, port=5000)