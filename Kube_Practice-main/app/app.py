from flask import Flask, render_template_string

app = Flask(__name__)

@app.route('/')
def home():
    return render_template_string('''
        <html>
            <head><title>Hello Kubernetes</title></head>
            <body style="text-align:center;">
                <h1>Hello, Kubernetes!</h1>
                <button onclick="document.getElementById('msg').style.display='block'">Click Me</button>
                <p id="msg" style="display:none; font-size:20px; color:green;">You clicked the button!</p>
            </body>
        </html>
    ''')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
