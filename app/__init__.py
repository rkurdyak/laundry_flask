from app.blueprints import user, web
from flask import Flask, request


app = Flask(__name__)

app.register_blueprint(web.bp)
app.register_blueprint(user.bp)
