# -*- coding: utf-8 -*-
"""
Created on Wed May 27 14:57:35 2015

@author: Taikor
"""

import smtplib

from email.mime.text import MIMEText

from_addr  = "furaoing@qq.com"
to_addr =  "raofu@hotmail.com"

msg = MIMEText("This is a Test !")
msg["Subject"] = "Test"
msg["From"] = from_addr
msg["To"] = to_addr


smtp = smtplib.SMTP()
smtp.connect("smtp.qq.com")
smtp.login(r"furaoing@qq.com", r"fxh94941")
smtp.sendmail(from_addr, to_addr, msg.as_string())
smtp.close()

