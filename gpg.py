import os,sys
import gnupg
import platform


temp = os.path.abspath(sys.argv[0])
print temp
path = temp[:temp.find('gpg.py')]
print path
###Configuration Options###
# MOVE TO SEPARATE FILE#
user = platform.node()
comment = 'test key creation'
email = 'none@test.com'
directory =  '.gpg'
pubkey_file = None


#####GnuPG Integration with HTTP Reverse Shell#####

#Create GPG object to interface with, local working directory for keys being <working dir>/.gpg
gpg = gnupg.GPG(gnupghome= path + "/" + directory + "/")


#Check to see if key exists
if not os.path.exists(user + ".pub"):
	print "No key found"
	#Set options for GPG key
	input_data = gpg.gen_key_input(key_type="RSA", key_length=2048 , name_real=user , name_comment=comment , name_email=email)

	#Generate Key
	print "Generating key"
	key = gpg.gen_key(input_data)
	
	print "Exporting Public Key"
	#Export keys to variable to be saved to text file for sharing with clients
	ascii_armored_public_keys = gpg.export_keys(str(key))
	
	#Open file and write pub key
	with  open(user+".pub", 'w') as pubkey_file:
		pubkey_file.write(ascii_armored_public_keys)

if os.path.exists('server.pub'):
	#Import Server PubKey
	with open("server.pub", 'r') as server_pubkey_file:
		server_pubkey_tainted = server_pubkey_file.read()
		server_pubkey = gpg.import_keys(server_pubkey_tainted)
