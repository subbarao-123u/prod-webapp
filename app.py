from flask import Flask
app = Flask(__name__)

@app.route('/')
def home():
    return "🚀 Production Web App LIVE!"

@app.route('/health')
def health():
    return '{"status": "healthy", "deployed": "Jenkins CI/CD"}'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

