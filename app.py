import base64
from io import BytesIO
import urllib.request

from flask import Flask, request, send_file
from PIL import Image
from werkzeug.exceptions import BadRequest


app = Flask(__name__)


@app.route('/')
def image():
    url = request.args.get('url')
    if not url:
        raise BadRequest('Missing required parameter "url"')
    try:
        url = base64.urlsafe_b64decode(url).decode('utf-8')
    except Exception:
        raise BadRequest('Failed to decode "url" parameter') from None
    try:
        width = int(request.args.get('width', 0))
    except Exception:
        raise BadRequest('Parameter "width" must be integer') from None
    try:
        height = int(request.args.get('height', 0))
    except Exception:
        raise BadRequest('Parameter "height" must be integer') from None

    image = Image.open(urllib.request.urlopen(url))
    obj = BytesIO()
    if width or height:
        image.thumbnail((width or height, height or width))
    image.save(obj, image.format)
    obj.seek(0)
    return send_file(obj, mimetype=Image.MIME[image.format])
