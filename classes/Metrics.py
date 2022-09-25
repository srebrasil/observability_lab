#create a class for opentelemetry metrics
from msilib.schema import Environment
from prometheus_client import make_wsgi_app
from werkzeug.middleware.dispatcher import DispatcherMiddleware
from werkzeug.serving import run_simple
from flask_prometheus_metrics import register_metrics

class Metrics:
    def __init__(self, version, environment):
        self.version = version
        self.environment = environment
    def collect_metrics(self):
        # provide app's version and deploy environment/config name to set a gauge metric
        register_metrics(app, app_version="v0.1.2", app_config="staging")

        # Plug metrics WSGI app to your main app with dispatcher
        dispatcher = DispatcherMiddleware(app.wsgi_app, {"/metrics": make_wsgi_app()})