sudo apt-get update

# Install Python 3.9
sudo apt install software-properties-common
#sudo dpkg --configure -a
#sudo apt-get install -f
sudo apt install build-essential zlib1g-dev libncurses5-dev libgdbm-dev libnss3-dev libssl-dev libsqlite3-dev libreadline-dev libffi-dev curl libbz2-dev
cd ../
wget https://www.python.org/ftp/python/3.9.1/Python-3.9.1.tgz
tar -xzf Python-3.9.1.tgz
cd Python-3.9.1
./configure --enable-optimizations
make -j 2
sudo make install

sudo apt install python3.9
sudo apt-get install python3-pip git gcc python-dev libkrb5-dev libssl-dev -y
pip install --upgrade pip
pip install --user ansible pywinrm ansible-vault
