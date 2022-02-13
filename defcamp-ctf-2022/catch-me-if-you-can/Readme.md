**catch-me-if-you-can**

**Author: Volk**

**Description**:
We need your technical expertise to analyze this Android project. We tried to compile it, no success, we tried to open it, no success, but we know for sure that the final product had to scope to deliver hidden messages to different attackers worldwide in a form of a mobile game. Flag format: not standard

**Walkthrough/Solution:**

**Part 1**:

`Challenge: What is the first code that you should deliver to us?`

When we look at an Android Application, the most important file is the AndoridManifest.xml file. It has essential information about the app. So, let's take a look at that file.
In our case, the file to look out for is under `app/src/main`.
The AndroidManifest.xml file in this directory has the following contents:
```
<?xml version="1.0" encoding="utf-8"?><!--
  ~ here you can create your own puzzles
  ~ secrets can be discovered along the way
  ~ here you can find the first gem: idopuzzlesforpleasure
  -->

<manifest xmlns:android="http://schemas.android.com/apk/res/android"
        package="com.jigdraw.draw">

    <uses-permission android:name="android.permission.WRITE_EXTERNAL_STORAGE" />

    <application
            android:allowBackup="true"
            android:icon="@drawable/ic_launcher"
            android:label="@string/app_name"
        android:theme="@style/Theme.AppCompat" >
            android:largeHeap="true">
        <activity
                android:name=".activity.DrawActivity"
                android:label="@string/app_name"
                android:screenOrientation="portrait">
            <intent-filter>
                <action android:name="android.intent.action.MAIN" />
                <category android:name="android.intent.category.LAUNCHER" />
            </intent-filter>
        </activity>

        <provider
                android:name=".provider.ImageProvider"
                android:authorities="com.jigdraw.draw.provider.jigsaw"
            android:exported="false" />

        <activity
                android:name=".activity.JigsawActivity"
                android:label="@string/app_name"
                android:screenOrientation="portrait"
                android:parentActivityName=".activity.DrawActivity">
            <meta-data
                    android:name="android.support.PARENT_ACTIVITY"
                    android:value=".activity.DrawActivity" />
        </activity>

        <activity
                android:name=".activity.JigsawHistoryActivity"
                android:label="@string/app_name"
                android:screenOrientation="portrait"
                android:parentActivityName=".activity.DrawActivity">
            <meta-data
                    android:name="android.support.PARENT_ACTIVITY"
                    android:value=".activity.DrawActivity" />
        </activity>
    </application>

</manifest>
```
Hey, hey! Look what we have here! 
`
~ here you can create your own puzzles
  ~ secrets can be discovered along the way
  ~ here you can find the first gem: idopuzzlesforpleasure
`
Looks like a flag!

*Flag*: `idopuzzlesforpleasure`

**What does this tell us?**

Always start by looking at the AndroidManifest.xml file whenever you are dealing with Android App Forensics.

_____________________________________________________________________________________________________________________________________________________________________________

**Part 2:**

`Challenge: Some file is triggered when the user is launching the application. Can you provide its name?`

From the question, we can infer that there is a file being triggered within the application. This means that there must be a file within the app that stores such information. Additionally, there is a standard directory in Android apps that has information about the functionality of the app called `activity`. After a bit of searching, we see that there is a directory called `app/src/main/java/com/jigdrawdraw/activity/` and there is an interesting file called `ExternalStorage.java`. 
These are the contents of that file:
```
package com.jigdraw.draw.activity;
import android.content.Context;
import android.content.Intent;
import android.content.SharedPreferences;
import android.os.Bundle;
import android.os.Environment;
import android.support.v7.app.AppCompatActivity;
import android.view.View;
import android.widget.Button;
import android.widget.EditText;
import android.widget.Toast;

import com.jigdraw.draw.R;

import java.io.File;
import java.io.FileNotFoundException;
import java.io.FileOutputStream;
import java.io.IOException;
import java.math.BigInteger;
import java.nio.charset.Charset;
import java.security.MessageDigest;
import java.security.NoSuchAlgorithmException;

public class ExternalStorage extends AppCompatActivity {
    public int totalCount=0;
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        getSupportActionBar().setTitle("External Storage");
        getSupportActionBar().setDisplayHomeAsUpEnabled(true);
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_external_storage);
        setTitle("External Storage");

        if (isExternalStorageWritable()) {
            File file = new File (Environment.getExternalStorageDirectory(), "H4sIAAAAAAAA/ytPLc/MySkuSU3MSczJyc3PS63MzCvJSC3PL8pJAQBLJvfnHQAAAA==.txt");

//            Log.d("External Storage Directory", String.valueOf(Environment.getExternalStorageDirectory()));

            FileOutputStream fos;

            try {
                fos = new FileOutputStream(file);
                fos.write(flag.getBytes());
                fos.close();
            } catch (FileNotFoundException e) {
                e.printStackTrace();
            } catch (IOException e) {
                e.printStackTrace();
            }

        }
    public boolean isExternalStorageWritable() {
        String state = Environment.getExternalStorageState();
        return Environment.MEDIA_MOUNTED.equals(state);
    }
    public boolean isExternalStorageReadable() {
        String state = Environment.getExternalStorageState();
        return Environment.MEDIA_MOUNTED.equals(state) ||
                Environment.MEDIA_MOUNTED_READ_ONLY.equals(state);
    }
    public static String md5(String s) {
        MessageDigest digest;
        try {
            digest = MessageDigest.getInstance("MD5");
            digest.update(s.getBytes(Charset.forName("US-ASCII")), 0, s.length());
            byte[] magnitude = digest.digest();
            BigInteger bi = new BigInteger(1, magnitude);
            String hash = String.format("%0" + (magnitude.length << 1) + "x", bi);
            return hash;
        } catch (NoSuchAlgorithmException e) {
            e.printStackTrace();
        }
        return "";
    }

}
```
Woah, `File file = new File (Environment.getExternalStorageDirectory(), "H4sIAAAAAAAA/ytPLc/MySkuSU3MSczJyc3PS63MzCvJSC3PL8pJAQBLJvfnHQAAAA==.txt");` seems interesting. 
Looks like it is an encrypted string. Let's try to decode it with the help of our old friend, CyberChef.
![image](https://user-images.githubusercontent.com/95949180/153769565-1f2169ee-9641-417a-8b64-2c10ceec9d90.png)
This means that the file being mentioned is `wewillstealallmoneyintheworld.txt`. Solved!

*Flag*:

**What does this tell us?**

This challenge tells us that the activity directory of an Android app holds crucial information about the functionality of the file. Also, finding encrypted strings should make us more alert and should prompt us to find a way to decode it.

_____________________________________________________________________________________________________________________________________________________________________________

**Part 3:**

`Challenge: Something is triggered on the device screen when launching the application, you know like buttons, logos, and stuff like that. There are suspicions that hidden applications may be found.`

The main directory for logos, buttons, etc. is the `res` (resources) directory.
In this app, the `res` directory is located at `app/src/main/res`. Let's examine the directory. Hmm, `drawable-xxhdpi` looks interesting. There is also a file called `model_signature.png`. That doesn't look standard. Let's take a closer look.

![model_signature](https://user-images.githubusercontent.com/95949180/153770471-0db153c3-794f-4fe0-b4ad-d102db8b3384.png)

Hmm, a QR Code. Let's read the QR Code using a scanner.
Interesting, it gives us this link: https://qrty.mobi/preview/vc5lGV

![image](https://user-images.githubusercontent.com/95949180/153770556-9d2066a3-8ef5-4878-a6a4-b7d6b42dc3d9.png)

What is this weird code? Ohh, it looks like a SHA1 checksum. But wait, that is not a full checksum, it's only part of it.
Looking back at the challenge description, we can infer that this partial checksum relates to some kind of malware or malicious application. Looks like some OSINT is required here.
After some searching, we come across a list of SHA1 Checksums of Android Malware. 
https://github.com/mstfknn/android-malware-sample-library/tree/master/Covid19%20Samples
![image](https://user-images.githubusercontent.com/95949180/153770725-ee9d76ab-8045-4584-8d9a-82d81d601188.png)
Let's see if we can find the full checksum of our partial one.
![image](https://user-images.githubusercontent.com/95949180/153770742-1cd98d09-9502-47a6-bff3-daf1117a8c0f.png)
Hey, look! There it is!
![image](https://user-images.githubusercontent.com/95949180/153770764-f992237b-908d-42d9-b397-8d8c0b14c2f2.png)
Full Checksum: `2B43AF46398ECE7B9E1E41BB7C2E2FF3EC227EDB38283BEA7622115BB76A7823`
Going back to the link we found from our QR, we see the word `free`. 
![image](https://user-images.githubusercontent.com/95949180/153770794-8cc21dd6-abef-417f-a386-34f43f585264.png)
Hmm, what can this refer to? Oh yea, VirusTotal. VirusTotal is a free malware detection/searching service. A lot of common malware are uploaded there by the community.
Let's try searching for the malware with our full checksum.
![image](https://user-images.githubusercontent.com/95949180/153770855-5b0d74dd-3a07-4d8f-8ee8-fe86dde8bf79.png)
A malware indeed! Oh, there is the name we are looking for! `Covid_CovidMap.apk`

*Flag:* `Covid_CovidMap.apk`

**

_____________________________________________________________________________________________________________________________________________________________________________

**Part 4:**

`Challenge: Something is wrong with the SharedPreferences file. We didn't manage to understand the string value. Please share it with us.`

So the challenge needs a string value with the correct interpretation. Hmm. `SharedPreferences` seems familiar. Oh yea, we saw it earlier when we were doing the first part! It is in the same directory! `app/src/main/java/com/jigdraw/draw/activity`
There it is.
```
package com.jigdraw.draw.activity;


import android.content.Context;
import android.content.Intent;
import android.content.SharedPreferences;
import android.os.Bundle;
import android.support.v7.app.AppCompatActivity;
import android.view.View;
import android.widget.Button;
import android.widget.EditText;
import android.widget.Toast;

import java.math.BigInteger;
import java.nio.charset.Charset;
import java.security.MessageDigest;
import java.security.NoSuchAlgorithmException;
public class SharedPref extends AppCompatActivity {

    public static final String MyPREFERENCES ;
    public int totalCount=0;
    SharedPreferences sharedpreferences;
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_shared_pref);
        setTitle("1337");

        sharedpreferences = getSharedPreferences(MyPREFERENCES, Context.);
        String n = "|][]¥°|_|7#][\\]X'/[](_):-:∂|/€|†\n";
        SharedPreferences.Editor editor = sharedpreferences.edit();
        String decrypted = "";
```
Woah, there is an encrypted string. We can tell by looking at this line `String n = "|][]¥°|_|7#][\\]X'/[](_):-:∂|/€|†\n";`
Let's try decrypting it. 
Not sure what this cipher is? No problem. Just use https://www.dcode.fr/cipher-identifier
![image](https://user-images.githubusercontent.com/95949180/153771251-b31580bf-a20d-47c8-8e13-f7d5891e7252.png)
Looks like it is `Leet Speak 1337` cipher. Let's head to that page to decode it.
![image](https://user-images.githubusercontent.com/95949180/153771313-106ca194-05d5-4e51-bd05-86241cf97324.png)
Hmm. This does not look fully decoded. Let's try decoding this output we recieved.
![image](https://user-images.githubusercontent.com/95949180/153771344-9027d40c-c7ec-4e0e-8678-a68fd2911bbc.png)
I think we can see what the message should say. The correct phrase would be `DOYOUTHINKYOUHAVEIT`.
Wow, looks like a flag!
Let's submit it!

*Flag*: `DOYOUTHINKYOUHAVEIT`

**What does this tell us?**

This challenge shows how an encrypted string can be hidden within an app to send a secret message to someone.
