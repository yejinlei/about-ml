name=$1
pyenv virtualenv 3.7.0 ${name}_3.7.0
pyenv deactivate
pyenv activate ${name}_3.7.0
pyenv local ${name}_3.7.0
pyenv rehash
pip install --upgrade pip
pip install -r requirements.txt
