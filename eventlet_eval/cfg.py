gunicorn_port = 5050
bind = f"0.0.0.0:{gunicorn_port}"

workers = 8
threads = 1
# worker_class = "eventlet"

preload_app = False
reload = True

accesslog = "-"  # stdout
timeout = 60
keepalive = 65
