from flask import Flask, request, jsonify, render_template
import openai
import os

openai.api_key = os.getenv('OPENAI_API_KEY')  # Store your API key in environment variable

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    user_input = request.json['message']

    response = openai.ChatCompletion.create(
        model='gpt-4',
        messages=[
            {"role": "system", "content": "You are a helpful business consultant that helps local business owners grow their businesses."},
            {"role": "user", "content": user_input}
        ]
    )

    reply = response['choices'][0]['message']['content']
    return jsonify({'reply': reply})

if __name__ == '__main__':
    app.run(debug=True)