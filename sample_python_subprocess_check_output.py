import subprocess

def index(event, context):
    for record in event['Records']:
        sns_message = json.loads(record['Sns']['Message'])
        raw_email = sns_message['content']
        parser = email.message_from_string(raw_email)
        if parser.is_multipart():
            for email_msg in parser.get_payload():
                file_name = email_msg.get_filename()
                if not file_name:
                    continue
                if not file_name.endswith('.pdf'):
                    continue

                # export pdf attachment to /tmp
                pdf_file_path = os.path.join('/tmp', file_name)
                with open(pdf_file_path, "wb") as pdf_file:
                    pdf_file.write(email_msg.get_payload(decode=True))

                # extract text from pdf file
                cmd = "/var/task/lib/pdftotext {} -".format(pdf_file_path)

                pdf_content = subprocess.check_output(cmd, shell=True)

