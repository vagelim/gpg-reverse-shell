gpg-reverse-shell
=================

Reverse HTTP Shell With GnuPG Encryption
Purpose: To permit a number of clients to poll a server for commands while keeping those commands secret

Requirements:
-GnuPG
-IP address of server (for clients)


Typical Session Flow (first run):
1. Client generates keypair
2a. Client and Server exchange Pubkeys
2b. Client shares pubkey fingerprint with server through trust (server trusts client)
    2bi.Client requests authorization from server (sends server Client Pubkey Fingerprint)
    2bii. Server checks fingerprint against preauthorized client database
    2biii. Server authenticates client
    2biv.  Client and Server exchange Pubkeys
    !!!Preshared key encrypts nonce which is evaluated by client and sent back to server!!!
      Requires pre-shared key to establish trust between parties
      Allows clients to generate new keypairs on the fly
      If PSK is found in memory, trust is broken
