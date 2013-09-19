import os,sys
import gnupg
import platform


path = os.path.abspath(sys.argv[0])

###Configuration Options###
# MOVE TO SEPARATE FILE#
user = platform.node()
comment = 'test key creation'
email = 'none@test.com'
directory =  '/.gpg'


#####GnuPG Integration with HTTP Reverse Shell#####

#Create GPG object to interface with, local working directory for keys being <working dir>/.gpg
gpg = gnupg.GPG(gnupghome= path + director)

#Set options for GPG key
input_data = gpg.gen_key_input(key_type="RSA", key_length=2048 , name_real=user , name_comment=comment , name_email=email)

#Generate Key
key = gpg.gen_key(input_data)

#Export keys to variable to be saved to text file for sharing with clients
ascii_armored_public_keys = gpg.export_keys(str(key))

#Open file and write pub key
