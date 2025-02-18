from flask import Flask
from flask_cors import CORS
from api.routes import api_bp
from config import Config
import traceback

app = Flask(__name__)
app.config.from_object(Config)

@app.errorhandler(Exception)
def handle_exception(e):
    """Handle exceptions and print only clean error messages."""
    print("❌ ERROR:", e)  # Print the error message only
    print(traceback.format_exc())  # Print the Python traceback (no HTML)
    return {"error": str(e)}, 500  # Return a JSON response

# ✅ Allow frontend requests
CORS(app, resources={r"/api/*": {"origins": "*"}})

# ✅ Register API routes
app.register_blueprint(api_bp, url_prefix='/api')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)

