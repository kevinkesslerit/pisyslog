# pisyslog
Uses rsyslog, and blinkt.

**Set up rsyslog**
`sudo nano /etc/rsyslog.conf`

**Uncomment UDP**
```
module(load="imudp")
input(type="imudp" port="514")
```

**Uncomment TCP**
```
module(load="imtcp")
input(type="imtcp" port="514")
```

`CTRL + O`
`{Enter}`
`CTRL + X`

**Create Log File**
`sudo touch /var/log/syslog.log`

**Create Config File**
`sudo nano /etc/rsyslog.d/syslog.conf`

**Configure Log File**
Enter content below, change router IP address as needed:
```
$template NetworkLog, "/var/log/syslog.log"
:fromhost-ip, isequal, "192.168.0.1" -?NetworkLog
& stop
```

**Create logrotate Config**
`sudo nano /etc/logrotate.d/syslog-rotate.conf`

**Configure logrotate File**
Enter content below:
```
/var/log/syslog.log {
        rotate 7
        size 500k
        notifempty
        compress
        postrotate
                invoke-rc.d rsyslog rotate > /dev/null
        endscript
}
```

# Install Blinkt!
Follow instructions here: https://github.com/pimoroni/blinkt

**As of this writing this is the preferred method:**
`curl https://get.pimoroni.com/blinkt | bash`

# Final Step
```
$ python3 syslog.py
```
Sit back and wait for the red LED when a DNS query is made to trigger the phrase match.
