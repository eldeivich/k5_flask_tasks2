from flask import Flask, flash

app = Flask(__name__)

from tasks import routes_copy