# 🔥 SnapStreak-Recovery
we all know how frustrating it can be to recover multiple streaks at the same time, this program eases that for you. All you have to do is write your friends' name (that you can remember) and their **snapchat username** in [credentials.txt](credentials.txt) once and you are all set, just run [main.py](main.py) whenever you need to recover streaks and the program will do the rest for you.


# ⚙️ Prerequisites

- You need to have python installed. You can install it from microsoft store or follow this [guide](https://www.geeksforgeeks.org/how-to-install-python-on-windows/).
- You must have web driver installed. You can download it from [here](https://chromedriver.chromium.org/downloads). Make sure to download the version that matches your chrome version. You can check your chrome version by going to `chrome://settings/help` in your browser. Remember the path where you download the driver because you'll have to add that path in [driver.py's](driver.py) line 18, its usually in `C:\Program Files (x86)\chromedriver.exe`  or  `C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe` </br>

# 🧑‍🏫 How to use

### 1. Download the files
![Download this repo](gifs/download.gif)

### 2. Extract the files
![Extract the files](gifs/extract.gif)

### 3. Edit credentials.txt  

**FOLLOW THE INSTRUCTIONS CAREFULLY**

![Edit credentials.txt](gifs/credentials.gif)

### 4. Install the requirements

- Open the folder in your favourite text editor, I am using [vscode](https://code.visualstudio.com/). </br>
- Run  `pip install npyscreen` and  `pip install selenium`. </br>
- Or simply run  `pip install -r requirements.txt` to install both requirements automagically.

![Install the requirements](gifs/requirements.gif)

### 5. Run main.py

Thats it! You are ready to go. </br>
Just run [main.py](main.py) whenever you need to recover streaks and the program will do the rest for you.

![Run main.py](gifs/final.gif)

# Troubleshooting
If you are facing any problems, feel free to open an issue or contact me on discord: `cocomo#5215` </br>
More often than not, the problem is with the web drivers. Make sure you have the correct version of web drivers installed and you are following the format specified in [credentials.txt](credentials.txt).

# features in futute
If possible, I'll try to add captcha bypass but if you really need an immediate solution, you can use services like [2captcha](https://2captcha.com/).

[![License: MIT](https://img.shields.io/badge/License-MIT-purple.svg)](https://opensource.org/licenses/MIT)
