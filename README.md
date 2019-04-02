In order to run the scripts, the user will need to install python v3.

**For OS this can be done using homebrew. See https://www.howtogeek.com/211541/homebrew-for-os-x-easily-installs-desktop-apps-and-terminal-utilities/ for steps to download homebrew
Run the following command** 
`- brew install python`

**For Windows python can be installed using chocolaty. 
Once chocolaty is installed, the user can run the following command to install python:**
`- choco install python
`
**The scripts were written with the following version of python**:
Python 2.7.15

**Install python build tool** 
`pip install pybuilder`

see http://pybuilder.github.io/documentation/tutorial.html#.WxxvzzMzaYU for a tutorial

**To build dependencies, run the following command. For permissions it is required to execute command as sodoer or in Windows as administrator**
`-pyb install_dependencies`

**Static code analysis was preformed using SonarLint plugin for IntelliJ**

csvsql --dialect mysql --snifflimit 100000 VOCS2016-2017-HOUSEHOLD_F1.csv > mytabledef.sql


python CreateInsertQuery.py > textfile.txt
