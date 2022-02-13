**catch-me-if-you-can**

**Author: Volk**

**Description**:
We need your technical expertise to analyze this Android project. We tried to compile it, no success, we tried to open it, no success, but we know for sure that the final product had to scope to deliver hidden messages to different attackers worldwide in a form of a mobile game. Flag format: not standard

**Walkthrough/Solution:**

**Part 1**:

Challenge: What is the first code that you should deliver to us?

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

**Part 2:**

Challenge: Some file is triggered when the user is launching the application. Can you provide its name?

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

**What does this tell us?**

This challenge tells us that the activity directory of an Android app holds crucial information about the functionality of the file. Also, finding encrypted strings should make us more alert and should prompt us to find a way to decode it.
