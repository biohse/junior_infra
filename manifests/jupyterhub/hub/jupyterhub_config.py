import os
from oauthenticator.generic import GenericOAuthenticator

def default_url_fn(handler):
    user = handler.current_user
    if user and user.admin:
        return '/hub/admin'
    return '/hub/home'


c = get_config()

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

notebook_dir = os.environ.get("DOCKER_NOTEBOOK_DIR", "/home/jovyan")
c.DockerSpawner.notebook_dir = notebook_dir
c.DockerSpawner.volumes = {"jupyterhub-user-{username}": notebook_dir}
c.DockerSpawner.remove = True

# Adding GPU
import docker
c.DockerSpawner.extra_host_config = {
    "device_requests": [
        docker.types.DeviceRequest(
            count=-1,
            capabilities=[["gpu"]],
        ),
    ],
}

c.JupyterHub.authenticator_class = GenericOAuthenticator
c.GenericOAuthenticator.client_id = os.environ['OAUTH_CLIENT_ID']
c.GenericOAuthenticator.client_secret = os.environ['OAUTH_CLIENT_SECRET']
c.GenericOAuthenticator.authorize_url = os.environ['OAUTH_AUTHORIZE_URL']
c.GenericOAuthenticator.token_url = os.environ['OAUTH_TOKEN_URL']
c.GenericOAuthenticator.userdata_url = os.environ['OAUTH_USERDATA_URL']
c.GenericOAuthenticator.scope = ["openid", "email", "profile"]
c.GenericOAuthenticator.username_claim = "preferred_username"
c.GenericOAuthenticator.claim_groups_key = "groups"
c.GenericOAuthenticator.allow_all = True
c.GenericOAuthenticator.auto_login = True

c.Authenticator.admin_users = {"narek01", "zhiyanov"}
c.DockerSpawner.notebook_dir = "/home/jovyan"
c.Spawner.default_url = "/lab" # use JupyterLab (instead of Notebook) by default
c.Spawner.cpu_limit = 4

c.JupyterHub.allow_named_servers = False
c.JupyterHub.default_url = default_url_fn
c.JupyterHub.logo_file = "hse_logo.png"
