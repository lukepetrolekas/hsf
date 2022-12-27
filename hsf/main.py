from sanic import Sanic
from sanic.response import Request

app = Sanic("my-hello-world-app")

app.static("/static/main.css", "static/css/main.css", name="stylesheet")

@app.get("/")
@app.ext.template("home.html")
async def handler(request: Request):
    return {"seq": ["one", "two"]}

if __name__ == '__main__':
    app.run()
