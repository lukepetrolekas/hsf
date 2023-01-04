from sanic import Sanic
from sanic.response import Request, HTTPResponse
from tortoise.contrib.sanic import register_tortoise
import os
from models import Service

print(os.getcwd())

app = Sanic("my-hello-world-app")

app.static("/static/main.css", "static/css/main.css", name="stylesheet")

register_tortoise(
    app, db_url="sqlite://db.sqlite", modules={"models": ["models"]}, generate_schemas=True
)

@app.get("/")
@app.ext.template("home.html")
async def handler_home(request: Request):
    return {}


@app.get("/results")
@app.ext.template("results.html")
async def handler_results(request: Request):
    relevant_services = await Service.all();
    return { "type": request.args.get("type"), "services": relevant_services }

if __name__ == '__main__':
    app.run()
