from flask import request
import time
import sys
from datadog import DogStatsd

statsd = DogStatsd(host="statsd", port=9125)
REQUEST_LATENCY_METRIC_NAME = "request_latency_seconds"
REQUEST_COUNT_METRIC_NAME = "request_count"


class Metrics:
    def start_timer(self):
        request.start_time = time.time()

    def stop_timer(self, response):
        response_time = time.time() - request.start_time
        statsd.histogram(
            REQUEST_LATENCY_METRIC_NAME,
            response_time,
            tags=[
                "service:functions",
                "endpoint: %s" % request.path,
            ],
        )
        return response

    def record_request_data(self, response):
        statsd.increment(
            REQUEST_COUNT_METRIC_NAME,
            tags=[
                "service: functions",
                "method: %s" % request.method,
                "endpoint: %s" % request.path,
                "status: %s" % str(response.status_code),
            ],
        )
        return response

    def app_metrics(self, app):
        app.before_request(self.start_timer)
        app.after_request(self.record_request_data)
        app.after_request(self.stop_timer)
