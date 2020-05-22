from flask import Flask
from utils.datetime import format_datetime

app = Flask('app')
app.logger.info(__name__)
app.config.from_object('config')

app.jinja_env.filters['datetime'] = format_datetime
