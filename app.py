from flask import Flask, request, jsonify
from flask_cors import CORS
import requests

app = Flask(__name__)
CORS(app)

# 在这里填你的API Key
DIFY_API_KEY = "app-s1E1FMjnsaQ6vAiupjvhVJaI"
DIFY_API_URL = "https://api.dify.ai/v1/chat-messages"

@app.route('/api/chat', methods=['POST'])
def chat():
    try:
        data = request.get_json()
        
        headers = {
            'Authorization': f'Bearer {DIFY_API_KEY}',
            'Content-Type': 'application/json'
        }
        
        payload = {
            'inputs': {
                'query': data.get('query', ''),
                'round': data.get('round', 1),
                'script_name': data.get('script_name', '疑云'),
                'current_speaker': ''
            },
            'query': data.get('query', ''),
            'response_mode': 'blocking',
            'conversation_id': data.get('conversation_id', ''),
            'user': 'player-001'
        }
        
        response = requests.post(DIFY_API_URL, headers=headers, json=payload, timeout=60)
        return jsonify(response.json()), response.status_code
        
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=False)