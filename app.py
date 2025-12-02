from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def home():
    message = "Welcome to my Python Web App on Azure!"
    return render_template("index.html", message=message)


@app.route("/health")
def health():
    # Simple health-check endpoint for debugging/monitoring
    return {"status": "ok", "app": "my-python-webapp"}


if __name__ == "__main__":
    # This is only used for local development.
    # In Azure, a production server (gunicorn) will be used instead.
    app.run(host="0.0.0.0", port=8000, debug=True)
