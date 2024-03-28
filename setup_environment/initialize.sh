#!/bin/bash

### Installs Python3.9
### Initalizes virtual environment
### Installs required dependencies
### Activates venv

### view system information
# uname -a    
# bash --version

###
### TO BE DONE: check if script has already been run
###             or requirements have already been fulfilled
###

echo -e "\n\n*********************************************************"
echo -e "Welcome to the Budget Analyzer initialization script!"
echo "NOTE: YOU WILL BE PROMPTED FOR SUDO PASSWORD BY HOMEBREW"
echo -e "*********************************************************\n\n"

echo "Here's a quick runthrough of what is to come:"
echo -e "\t- Homebrew Installation (a lightweight package manger)"
echo -e "\t- Python3.9 Installation"
echo -e "\t- Create a virtual environment (to isolate packages from global)"
echo -e "\t- Install packages & activate virtual environment!\n"

read -n 1 -p "Do you wish to continue? (Y/n): " docontinue; echo ""

### Parse User Response
# If 'y' or 'Y' continue, else quit script
awk -vs1='y' -vs2=${docontinue} 'BEGIN {
    if ( tolower(s1) == tolower(s2) ){ 
        exit 0 # continue
    } else {
        exit 2 # do not continue
    }
}'

if [ $? == 0 ]; then
    echo "continueing"
else
    echo "Quitting"
    exit 2
fi

# echo "We continued"



### Homebrew Installation (a lightweight package manger)
command -v brew >/dev/null 2>/dev/null
if [ $? == 0 ]
then
    echo -n "✅︎ "
    brew --version
else
    echo "❌ Homebrew not installed"
    /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
    brew update
fi

### Python3.9 Installation
command -v python3.9 >/dev/null
if [ $? == 0 ]
then
    echo -n "✅︎ "
    python3.9 --version
else
    echo "❌ Python3.9 not installed"
    sudo apt install python3.9-venv

### Create a virtual environment (to isolate packages from global)"
mkdir -p ~/.venvs/  # useful to keep track of venvs
python3.9 -m venv ~/.venvs/finance
source ~/.venvs/finance/bin/activate    # activate venv
# pip install --upgrade pip   # update pip

### Install packages & activate virtual environment
# pip install wheel
# pip install matplotlib numpy pandas PyPDF2
python install -r requirements.txt

echo -e "\n\n\n"
print("We did it!! Woohoo!!!")