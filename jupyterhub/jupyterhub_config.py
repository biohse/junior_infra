import os
from firstuseauthenticator import FirstUseAuthenticator

c.JupyterHub.spawner_class = "dockerspawner.DockerSpawner"
c.DockerSpawner.image = os.environ["DOCKER_JUPYTER_IMAGE"]
c.DockerSpawner.network_name = os.environ["DOCKER_NETWORK_NAME"]
c.JupyterHub.hub_ip = os.environ["HUB_IP"]
c.JupyterHub.services = [
    {
        "name": "cull_idle",
        "admin": True,
        # kill idle containers after 1 hour, but do not remove
        "command": "cull_idle_servers.py --timeout=3600".split(),
    },
]
c.JupyterHub.authenticator_class = "firstuseauthenticator.FirstUseAuthenticator"
c.Authenticator.admin_users = {"admin"}
c.DockerSpawner.notebook_dir = "/home/jovyan"
c.Spawner.default_url = "/lab" # use JupyterLab (instead of Notebook) by default
c.Spawner.cpu_limit = 1
c.Spawner.mem_limit = "1G"
c.JupyterHub.admin_access = True