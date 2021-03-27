Image resizing on the fly using Flask and Pillow.

Prepare Python virtual environment::

   python3 -m venv venv
   ./venv/bin/pip install -U pip wheel setuptools
   ./venv/bin/pip install -r requirements.txt

Start the application::

   FLASK_APP=app.py ./venv/bin/python -m flask run

Base64 encode the original image URL::

   echo 'https://upload.wikimedia.org/wikipedia/commons/3/3f/JPEG_example_flower.jpg' | base64 -w 0

Query the application for resized image::

   http://127.0.0.1:5000/?url=<encoded-URL>&width=<width>&height=<height>
