import os

os.system('wget https://github.com/prometheus/node_exporter/releases/download/v1.0.1/node_exporter-1.0.1.linux-amd64.tar.gz')
os.system('tar zxvf node_exporter-1.0.1.linux-amd64.tar.gz')
os.chdir('node_exporter-1.0.1.linux-amd64')
os.system('cp node_exporter /usr/local/bin/')
os.system('useradd --no-create-home --shell /bin/false nodeusr')
os.system('chown -R nodeusr:nodeusr /usr/local/bin/node_exporter')
os.system('cat /tmp/in > /etc/systemd/system/node_exporter.service')
os.system('systemctl daemon-reload')
os.system('systemctl enable node_exporter')
os.system('systemctl start node_exporter')
os.system('systemctl status node_exporter')
