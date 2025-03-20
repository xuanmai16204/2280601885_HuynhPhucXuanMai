from flask import Flask, render_template, request
from cipher.caesar import CaesarCipher

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/caesar')
def caesar():
    return render_template('caesar.html')

@app.route('/encrypt', methods=['POST'])
def caesar_encrypt():
    text = request.form.get("inputPlainText", "")
    key = request.form.get("inputKeyPlain", "0")
    key = int(key) if key.isdigit() else 0

    Caesar = CaesarCipher()
    encrypted_text = Caesar.encrypt_text(text, key)
    return f"text: {text}<br>Key: {key}<br>Encrypted text: {encrypted_text}"

@app.route('/decrypt', methods=['POST'])
def caesar_decrypt():
    text = request.form.get("inputCipherText", "")
    key = request.form.get("inputKeyCipher", "0")
    key = int(key) if key.isdigit() else 0

    Caesar = CaesarCipher()
    decrypted_text = Caesar.decrypt_text(text, key)
    return f"text: {text}<br>Key: {key}<br>Decrypted text: {decrypted_text}"

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5050, debug=True)
