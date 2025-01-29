from flask import Flask, request, send_file
from rembg import remove
from PIL import Image
import io

app = Flask(__name__)

@app.route('/remove', methods=['POST'])
def process():
    if 'file' not in request.files:
        return "Send image via POST with 'file' key", 400
        
    img = Image.open(request.files['file'].stream)
    result = remove(img)
    
    output = io.BytesIO()
    result.save(output, format="PNG")
    output.seek(0)
    
    return send_file(output, mimetype='image/png')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
