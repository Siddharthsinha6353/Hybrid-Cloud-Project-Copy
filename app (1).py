import os
import redis
from flask import Flask, jsonify

app = Flask(__name__)
store = redis.Redis(
    host=os.getenv("REDIS_HOST", "localhost"),
    port=int(os.getenv("REDIS_PORT", "6379")),
    decode_responses=True,
    socket_connect_timeout=2
)

@app.get("/")
def home():
    try:
        visits = store.incr("visits")
        return f"<h1>Hybrid Cloud Demo</h1><p>Visit count: {visits}</p>", 200
    except redis.RedisError:
        return "Application is running, but Redis is unavailable.", 503

@app.get("/health")
def health():
    return jsonify(status="ok"), 200

@app.get("/ready")
def ready():
    try:
        store.ping()
        return jsonify(status="ready", redis="connected"), 200
    except redis.RedisError:
        return jsonify(status="not-ready", redis="unavailable"), 503

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
