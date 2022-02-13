**catch-me-if-you-can**

**Author: Volk**

**Description**:
We need your technical expertise to analyze this Android project. We tried to compile it, no success, we tried to open it, no success, but we know for sure that the final product had to scope to deliver hidden messages to different attackers worldwide in a form of a mobile game. Flag format: not standard

**Walkthrough/Solution:**

**Part 1**:

Challenge: What is the first code that you should deliver to us? (Points: 50)

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
Hey, hey! Look what we have here! Looks like a flag!

**What does this tell us?**

Always start by looking at the AndroidManifest.xml file whenever you are dealing with Android App Forensics.

**Part 2:**

