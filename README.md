# Configuration for Ultra-Fast-Object-Detection-in-Multispectral-Satellite-Imagery-using-UFOnet

The host to the rmit gpu cluster requires a jump proxy and so some prior setup was needed to make sure this worked with the ansible scripts

First added an ssh key on the jump box via ssh into it manually and generating it.
```bash
ssh-keygen -t rsa -b 4096 -C "s3630120@student.rmit.edu.au"
```
Then added the public key to the gpu-server
```bash
ssh-copy-id s3630120@10.205.51.154
```
#### Setting python version

SSH into the gpu server and the poetry version was 3.8, I needed 3.9, so i 
installed pyenv with this command
```bash
curl -L https://github.com/pyenv/pyenv-installer/raw/master/bin/pyenv-installer | bash
```
Then I added the following to my .bashrc file
```bash
export PATH="/opt/home/s3630120/.local/bin:$PATH"
export PATH="$HOME/.pyenv/bin:$PATH"
eval "$(pyenv init -)"
eval "$(pyenv virtualenv-init -)"
```
Then I installed python 3.9.12
```bash
pyenv install 3.9.12
pyenv global 3.9.12
python --version
```
#### Issues I had setting up poetry

Then I had issues running `poetry install`, as it wasn't installing the 
packages giving me an error in utils and other dependancy code bases.
The fix was the environment needed some keyring access.
The fix was 
1. python -c "import keyring.util.platform_; print(keyring.util.platform_.config_root())"
2. Creating the output directory printed
3. Creating a keyringrc.cfg file in the output directory with the following contents
```bash
[backend]
default-keyring=keyring.backends.null.Keyring
```

Then I ran poetry install and it worked.