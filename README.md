This is a test for Appium framework


### How to install:

## Create virtual environment 
  ```
python -m venv venv 
  ```
### Activate virtual environment pip
  ```
.\venv\scripts\activate  
  ```
### Install all packages in your IDE,  type in  Terminal command:
  ```
pip install -r requirements.txt
  ```


### Download Microsoft Build of OpenJDK: 
https://learn.microsoft.com/ru-ru/java/openjdk/download

### Download Node.js: 
https://nodejs.org/en/download/package-manager


### Installing Appium is as easy as running a single NPM command in  Terminal  :
Documentation:
https://appium.io/docs/en/2.1/quickstart/install/

  ```
npm i --location=global appium
  ```

### Download Android Studio : 
https://developer.android.com/studio?hl=ru

### Install the UiAutomator2 Driver in  Terminal:
  ```
appium driver install uiautomator2
  ```

## How Run Test:

### Start Android Studio:

### Run Appium in  Terminal:
  ```
appium 
  ```


### Run test in IDE:
 ```
pytest -v 
  ``` 


## Make sure you have proper  System environment variables in your OS ! 

## Use adb utility to find out appActivity and appPackage

 ```
adb shell
dumpsys window windows | grep -E 'mTopActivityComponent
  ``` 

 








