import os
import json
import sys
import tempfile

def report_handler(session, message):
    email = message

    # Generate a random temp file for the report
    _, temp_path = tempfile.mkstemp()

    # Write balance to temp file
    with open(temp_path, 'w') as tmp:
        tmp.write("balance=%s" % session.account.balance)
    filename = "/tmp/%s.tar.gz" % email
    command = "tar -czvf %s %s" % (filename, temp_path)

    # Compress the report before sending
    os.system(command)

    # Prepare email message
    msg = MIMEMultipart()
    msg['Subject'] = 'Bank statement report'
    ses = boto3.client("ses")

