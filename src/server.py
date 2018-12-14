from main import *
from sanic import Sanic, response
from sanic.response import text

app = Sanic()

app.config.REQUEST_TIMEOUT = 600
app.config.RESPONSE_TIMEOUT = 600


@app.route('/post', methods=['POST'])
async def post_handler(request):
    print("PRINT:", request.json)
    obj = request.json
    modelAssemblyService(obj)
    return text('New model is at this addreess: <a href=http://127.0.0.1:8000/model target=_blank>Click Here</a>')


@app.route('/model')
async def handle_request(request):
    return await response.file('model.xml')


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8000)
