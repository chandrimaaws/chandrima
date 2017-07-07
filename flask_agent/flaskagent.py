# Call flask agent

from flask import Flask
import os
from flask import  render_template, url_for, json
from flask import jsonify , json
from flask import request

app= Flask(__name__)

@app.route('/sayan', methods=['POST'])
def get_json_data():
    ec2_instance_store= request.get_json()
    f= open('/etc/ansible/playbooks/home/group_vars/all','w')
    f.write('ec2_access_key: ')
    f.write(ec2_instance_store['ec2_instance_variable']['ec2_access_key'] + '/n')
    f.close()

    os.system('ansible-playbook /etc/ansible/playbooks/home/install_ec2.yml')

    return'success'


if __name__ == '__main__':
   app.run('0.0.0.0',8089,debug = True)
