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
