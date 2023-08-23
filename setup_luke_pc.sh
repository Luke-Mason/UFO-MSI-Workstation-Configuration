sudo ansible-playbook -i ../ansible_playbook/inventory/luke_pc.ini ../ansible_playbook/playbook.yml --connection=local --tag role_datasets -vvv --ask-vault-pass

