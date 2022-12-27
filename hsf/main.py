from sanic import Sanic
from sanic.response import text

app = Sanic("my-hello-world-app")

@app.route('/')
async def test(request):
    return text("Done.")

if __name__ == '__main__':
    app.run()
