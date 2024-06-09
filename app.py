from flask import Flask, render_template, request, jsonify
import openai
app = Flask(__name__)
openai.api_key = 'your-api-key'

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    message = request.form['message']
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=message,
        max_tokens=150
    )
    return jsonify(response.choices[0].text.strip())

if __name__ == '__main__':
    app.run(debug=True)
