from main import *
from sanic import Sanic, response

app = Sanic()

app.config.REQUEST_TIMEOUT = 600
app.config.RESPONSE_TIMEOUT = 600


@app.route('/model')
async def handle_request(request):
    modelAssemblyService()
    return await response.file('model.xml')


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8000)
