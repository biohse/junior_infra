# FROM jupyter/scipy-notebook:x86_64-python-3.11.6
FROM glcr.b-data.ch/jupyterlab/cuda/python/scipy
COPY ./sudoers /etc/sudoers
COPY --chmod=644 . /temp
RUN pip install -r /temp/python-torch-requirements.txt --no-cache-dir
RUN sudo rm -rf /temp
# RUN sudo usermod -u 65535 jovyan && sudo groupmod -g 65535 jovyan
# USER 65535:65535
