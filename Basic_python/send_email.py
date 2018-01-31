# coding: utf-8
import smtplib
from email.mime.text import MIMEText
import datetime
# from email.header import Header
# from email.utils import formatdate

"""
[ref]
https://qiita.com/ColdFreak/items/1294258400f3ef149c3b

[ref]
http://w.builwing.info/2013/09/21/python3-3%E3%81%A7%E3%83%A1%E3%83%BC%E3%83%AB%E9%80%81%E4%BF%A1/

[tutorial]
https://www.tutorialspoint.com/python3/python_sending_email.htm

[python3.5 send email]
http://thinkami.hatenablog.com/entry/2016/06/09/062528
"""

jp='iso-2022-jp'

# file.txt 中に送信したい内容
fp = open('email_file.txt')
raw_msg = fp.read()
msg = MIMEText(raw_msg.encode(jp), 'plain', jp, )
fp.close()

from_address = 'jota5084phantom@gmail.com'
to_address   = 'junya.usui.0714@gmail.com'

# subject指定の時に使う
d = datetime.datetime.today()
# date = d.strftime("%2018-%1-%31")
date = d.strftime("%Y-%m-%d")

msg['Subject'] = date+"の仕様状況"
msg['from'] = from_address
msg['To'] = to_address


try:
    with smtplib.SMTP('localhost') as server:
        server.send_message(msg)
        print("Successfully sent email")

except Exception:
    print("Error: unable to send email")
    
    
    
