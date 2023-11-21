FROM condaforge/mambaforge:22.9.0-1
RUN mamba install configurable-http-proxy -y && \
    python -m pip install --no-cache-dir \
    dockerspawner \
    jupyterhub \
    jupyterhub-firstuseauthenticator \
    jupyterhub-idle-culler \
    oauthenticator \
    pycurl
COPY . .
ENTRYPOINT jupyterhub
