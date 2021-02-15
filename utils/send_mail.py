import smtplib
from pathlib import Path
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
from email.utils import COMMASPACE, formatdate
from email import encoders
from os import listdir
from os.path import abspath, join



# folder_path = 'C:\\Users\\pfm\\Downloads\\'
folder_path = 'R:\\test'
recipients = ['orkhangasanov@dme.ru']


def get_files_name(path):
	return [abspath(join(path, f)) for f in listdir(path)]


def send_mail(send_from, send_to, subject, message='', files=[],
              server="localhost", port=587, username='', password='',
              use_tls=False):

    msg = MIMEMultipart()
    msg['From'] = send_from
    msg['To'] = COMMASPACE.join(send_to)
    msg['Date'] = formatdate(localtime=True)
    msg['Subject'] = subject

    msg.attach(MIMEText(message))

    for path in files:
        part = MIMEBase('application', "octet-stream")
        with open(path, 'rb') as file:
            part.set_payload(file.read())
        encoders.encode_base64(part)
        part.add_header('Content-Disposition',
                        'attachment; filename="{}"'.format(Path(path).name))
        msg.attach(part)

    smtp = smtplib.SMTP(server, port)
    if use_tls:
        smtp.starttls()
    # smtp.login(username, password)
    smtp.sendmail(send_from, send_to, msg.as_string())
    smtp.quit()


def main():
	if get_files_name(folder_path):
		send_mail(
				send_from=gethostname(), send_to=recipients,
				subject=get_files_name(folder_path)[0].split('\\')[-1],
				files=get_files_name(folder_path), server='10.6.4.231', port=25
			)


if __name__ == '__main__':
	main()
