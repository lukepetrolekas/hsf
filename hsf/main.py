from sanic import Sanic
from sanic.response import Request
from tortoise.contrib.sanic import register_tortoise
import os

print(os.getcwd())

app = Sanic("my-hello-world-app")

app.static("/static/main.css", "static/css/main.css", name="stylesheet")

register_tortoise(
    app, db_url="sqlite://db.sqlite", modules={"models": ["models"]}, generate_schemas=True
)

@app.get("/")
@app.ext.template("home.html")
async def handler(request: Request):
    return {"services": ["Food", "Sleep", "Doctor", "Clothes", "Shower", "Washroom", "Laundry", "Someone to Talk To"]}

if __name__ == '__main__':
    app.run()
