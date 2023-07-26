from flask import Flask, send_file
import random
import os

app = Flask(__name__)

@app.route("/ignimgs.com/")
def index():
    image_dir = "static/images"
    image_files = os.listdir(image_dir)
    image_file = random.choice(image_files)
    return send_file(os.path.join(image_dir, image_file), mimetype="image/jpeg")

if __name__ == "__main__":
    app.run()
