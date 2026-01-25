Task: https://terokarvinen.com/application-hacking/#h2-break--unbreak-tero

# C
Command: `ffuf -c -w ./common.txt -u http://127.0.0.2:8000/FUZZ -fs  154`

- Admin page:
	- http://127.0.0.2:8000/wp-admin
	- `FLAG{tero-wpadmin-3364c855a2ac87341fc7bcbda955b580}`
- Version control related page: 
	- http://127.0.0.2:8000/.git/
	- `FLAG{tero-git-3cc87212bcd411686a3b9e547d47fc51}`