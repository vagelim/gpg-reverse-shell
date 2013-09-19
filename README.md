gpg-reverse-shell
=================

Reverse HTTP Shell With GnuPG Encryption<br>
Purpose: To permit a number of clients to poll a server for commands while keeping those commands secret

Requirements:<br>
-GnuPG<br>
-IP address of server (for clients)<br>


Typical Session Flow (first run):<br>
1. Client generates keypair<br>
2a. Client and Server exchange Pubkeys<br>
2b. Client shares pubkey fingerprint with server through trust (server trusts client)<br>
    2bi.Client requests authorization from server (sends server Client Pubkey Fingerprint)<br>
    2bii. Server checks fingerprint against preauthorized client database<br>
    2biii. Server authenticates client<br>
    2biv.  Client and Server exchange Pubkeys<br><br>
    !!!Preshared key encrypts nonce which is evaluated by client and sent back to server!!!<br>
      Requires pre-shared key to establish trust between parties<br>
      Allows clients to generate new keypairs on the fly<br>
      If PSK is found in memory, trust is broken<br>
