# crmpaalen
Descriptions

# Issue
1. SQLite3
Django can't find new sqlite version: SQLite 3.8.3 or later is required
Solution:
wget http://www6.atomicorp.com/channels/atomic/centos/7/x86_64/RPMS/atomic-sqlite-sqlite-3.8.5-3.el7.art.x86_64.rpm
sudo yum localinstall atomic-sqlite-sqlite-3.8.5-3.el7.art.x86_64.rpm
sudo mv /lib64/libsqlite3.so.0.8.6{,-3.17}
sudo cp /opt/atomic/atomic-sqlite/root/usr/lib64/libsqlite3.so.0.8.6 /lib64wget http://www6.atomicorp.com/channels/atomic/centos/7/x86_64/RPMS/atomic-sqlite-sqlite-3.8.5-3.el7.art.x86_64.rpm
sudo yum localinstall atomic-sqlite-sqlite-3.8.5-3.el7.art.x86_64.rpm
sudo mv /lib64/libsqlite3.so.0.8.6{,-3.17}
sudo cp /opt/atomic/atomic-sqlite/root/usr/lib64/libsqlite3.so.0.8.6 /lib64

Go to python sonsole once again
>>> import sqlite3
>>> sqlite3.sqlite_version
'3.8.5'
