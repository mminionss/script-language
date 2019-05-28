import smtplib
from email.mime.text import MIMEText

s=smtplib.SMTP('smtp.gmail.com',587)

s.starttls()

s.login('jinsy2098@gmail.com','dapfiukbpfiiilcm')

msg=MIMEText('내용:본문 내용 테스트입니다.')
msg['Subject']='유기동물 상세정보 조회'

s.sendmail("jinsy2098@gmail.com","tiurit12@naver.com",msg.as_string())

s.quit()