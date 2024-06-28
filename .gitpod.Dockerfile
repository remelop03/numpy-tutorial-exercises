FROM gitpod/workspace-full:latest

USER gitpod

# Install Python 3.11
RUN pyenv install 3.11.5
RUN pyenv global 3.11.5

# Upgrade setuptools
RUN pip3 install --upgrade setuptools

# Install required packages
RUN pip3 install pytest==6.2.5 mock pytest-testdox toml numpy==1.24.2
RUN npm i @learnpack/learnpack@2.1.39 -g && learnpack plugins:install @learnpack/python@1.0.3
