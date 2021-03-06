GUNICORN_PORT = 32001
SERVICES = {
    "nginx":
        {
            "port": 32000,
            "gunicorn_port": GUNICORN_PORT,
            "templates": ["{project_dir}/nginx.conf.template"],
            "start": "nginx -c {project_dir}/nginx.conf",
            "restart": "kill -s SIGHUP {pid}",
        },
    "gunicorn":
        {
            "port": GUNICORN_PORT,
            "templates": ["{project_dir}/settings_gunicorn.py.template"],
            "before": "./before_deploy.sh",
            "start": "gunicorn -D -c settings_gunicorn.py metakv.wsgi:application",
            "after": "./after_deploy.sh",
            "restart": "kill -s SIGHUP {pid}",
        },
    "memcached":
        {
            "pidfile": "{project_dir}/run/memcached.pid",
            "start": "memcached -d -m 32 -s {project_dir}/run/memcached.sock -P {project_dir}/run/memcached.pid",
        }
}

