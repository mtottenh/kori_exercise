#!/bin/bash

echo "Installing Xcode tooling"
xcode-select --install

echo "Installing Homebrew"
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"

echo "Installing libraires"
brew install vscodium pyenv pyenv-virtualenv vim git openssl readline sqlite3 xz zlib tcl-tk

echo "Setting up bashrc for pyenv/pyenv-virtualenv"
echo 'export PYENV_ROOT="$HOME/.pyenv"' >> ~/.bashrc
echo 'command -v pyenv >/dev/null || export PATH="$PYENV_ROOT/bin:$PATH"' >> ~/.bashrc
echo 'eval "$(pyenv init -)"' >> ~/.bashrc
echo 'eval "$(pyenv virtualenv-init -)"' >> ~/.bashrc

source ~/.bashrc

echo "Cloning KORI git repo"
git clone https://github.com/mtottenh/kori_exercise.git
pushd kori_exercise
pyenv update
pyenv install 3.10.10
pyenv virtualenv 3.10.10 kori
pyenv activate kori
pip install pytest


