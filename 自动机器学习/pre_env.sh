name=$1
pyenv virtualenv 3.7.0 ${name}_3.7.0
pyenv local ${name}_3.7.0
pyenv rehash
pyenv activate ${name}_3.7.0
pip install -U pip

