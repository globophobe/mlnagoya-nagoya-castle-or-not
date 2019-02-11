import sys
from io import BytesIO

import aiohttp
import responder
from fastai.vision import load_learner, open_image

api = responder.API()
learner = load_learner(".")


async def download_url(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            return await response.read()


@api.route("/upload")
async def upload(req, resp):
    # Files in responder are in a dict,
    # files['file'] = {'filename': <filename>, 'content': <bytes>}
    # Official docs were meh, see tests:
    # https://github.com/kennethreitz/responder/blob/master/tests/test_responder.py
    files = await req.media("files")
    if "file" in files:
        data = files["file"]["content"]
        resp.media = predict_image_from_bytes(data)
    else:
        resp.text = "Image is required."


@api.route("/classify-url")
async def classify_url(req, resp):
    # Initially, dreamt api.requests.get_url might be requests for asyncio.
    # No such thing, make your own with aiohttp.
    # A la, download_url.
    if "url" in req.params:
        url = req.params["url"]
        data = await download_url(url)
        resp.media = predict_image_from_bytes(data)
    else:
        resp.text = "URL is required."


def predict_image_from_bytes(data):
    img = open_image(BytesIO(data))
    _, _, losses = learner.predict(img)
    return {
        "predictions": sorted(
            zip(learner.data.classes, map(float, losses)),
            key=lambda p: p[1],
            reverse=True,
        )
    }


@api.route("/", default=True)
def index(req, resp):
    # Default template_dir in responder is 'templates'
    resp.content = api.template("index.html")


if __name__ == "__main__":
    if "production" in sys.argv:
        # Bind to all interfaces, so can access on localhost with:
        # docker run -p 8000:8000 -t <image>
        api.run(address="0.0.0.0", port=8000)
    if "debug" in sys.argv:
        # Don't bind to all interfaces,
        # so no macOS security popup on startup.
        api.run(port=8000)
