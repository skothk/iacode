openssl req -new > cert.csr
openssl rsa -in privkey.pem -out key.pem
openssl req -x509 -newkey rsa:4096 -keyout key.pem -out cert.pem -days 365
cat key.pem>>cert.pem
