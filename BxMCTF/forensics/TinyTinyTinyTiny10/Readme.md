##Description :

Windows 10 takes up so much space and resources that I managed to strip it down to a mere 12.2MB. All I really needed to build it anyways was cmd and calc, and out of the final size, all of it is just the GPT table and other random garbage that I don't really understand.
Next year, I'm going to try and completely eliminate the GPT table too!
BitLocker password: bitlocker
foren4.zip

##Solution :

You can mount the vhd with bitlocker support on Linux using bdemount 

```sh
bdemount -o $((32768*512)) -p bitlocker disk.vhd /media/bitlocker/
```

Then I simply used grep to get the flag.

```sh
strings -n 10 bde1 | grep ctf
ctf{10V3D_4ND_1057}
```


