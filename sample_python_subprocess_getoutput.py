import os
import subprocess

def lambda_handler(event, context):

    # Set environmental variables

    s3 = boto3.resource('s3')
    bucket = s3.Bucket(s3_bucket_name)
    bucket.download_file(s3_bin_dir + mysqldump_bin, work_dir + '/' + mysqldump_bin)
    mysqldump_ret = os.path.isfile(work_dir + '/' + mysqldump_bin)

    # Get the subject from the email event
    subject = event['Records'][0]['ses']['mail']['commonHeaders']['subject']

    mysqldump_filename = mysql_dbname + '_current.sql'
    cmd = work_dir + '/mysqldump' + ' -u ' + mysql_user + ' -p ' + \
        mysql_pass + ' -h ' + subject + ' ' + mysql_dbname + \
        mysqldump_option + ' > ' + work_dir + '/' + mysqldump_filename

    # Call mysqldump
    ret = subprocess.getoutput(cmd)

    print('dump finished')

