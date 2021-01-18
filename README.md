# oryx complex macros
Method to add longer keystrokes macros to oryx layouts. Do not put passwords in your persistent macros.

## Purpose
I love ergodox-ez's keyboard layout tool [Oryx](https://configure.ergodox-ez.com/), but the [character limit](https://blog.zsa.io/2003-oryx-macros/) for the macros is holding back this keyboard's potential.

This tool is created so that you can still use the oryx layout tool but still input your own complex macros.

I wanted to add macros that would be used for vim keystrokes so that I wouldn't have to upload/modify vimrc.


## Overall Build and Usage Process
Requires python3 and Docker.
Note: For now this is only for linux base systems, pending windows testings

Simply create a macro in oryx with a unique 4 key macro: MM11. The script will reference the custom-mapping.csv file to find and replace the macro identifiers.

- docker image, either build or download from github
- establish oryx layout with macro identifiers
- use the app.py to create and update custom-mapping.csv
- run firmware compiler


## Usage
Download docker container `docker pull jonberenguer/zsa-qmk` or build the container

Then clone the repository and run the app
```
git clone https://github.com/jonberenguer/oryx-complex-macros.git
cd oryx-complex-macros
python app.py
```

*pending more steps


# Checklist
- [ ] currently for alpha, numeric and space chars. need support for special chars
- [ ] detailed print screen of steps
- [ ] more steps for postfix for example macros with an enter at the end
