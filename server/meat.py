from flask import Flask, render_template, request, url_for, make_response
import sys
sys.path.insert(1, '../')
import combine
from PIL import Image
from io import BytesIO
import base64

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    error = None
    if request.method == 'POST':
        f = request.files['receipt']
        f.save('./assets/image.png')
    return render_template("homepage.html")


@app.route("/process/", methods=["POST"])
def process_image():
    error = None
   # counter += 1
    #print(f'data: {request.get_data()}')
    print(f'content encoding: {request.content_encoding}')
    print(f'content type: {request.content_type}')
    #print(f'files: {request.files}')
    f = None
    if len(request.files) > 0:
        f = request.files['receipt']
        f.save(f'./assets/{1}.png')
    else:
        f = request.get_data()
        #print(request.files)

    #with open(f'./assets/{1}', 'wb') as img:
     #   img.write(f)
    #image = Image.open(BytesIO(f))
    #image.save(f'./assets/{1}.png')
    print('gets here?')
    return f"{combine.get_weight(f'./assets/{1}.png')}"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
