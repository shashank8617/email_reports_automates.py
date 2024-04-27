## update the system
```bash
sudo yum update
```
## install python
```bash
python3 -m pip install schedule
```
## to run the python file
```bash
python3 daily_email_report.py
```
## to schedule the event
```bash
crontab -e
```
## paste this in crontab -e
```bash
0 9 * * * /usr/bin/python3 /root/script.py
```

