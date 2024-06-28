FROM gitpod/workspace-full:latest

USER gitpod

RUN pip3 install pytest==6.2.5 mock pytest-testdox toml numpy==1.24.2
RUN npm i @learnpack/learnpack@2.1.39 -g && learnpack plugins:install @learnpack/python@1.0.3
