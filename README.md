# oryx complex macros
Method to add longer keystrokes macros to oryx layouts. Do not put passwords in your persistent macros.

## Purpose
I love ergodox-ez's keyboard layout tool [Oryx](https://configure.ergodox-ez.com/), but the [character limit](https://blog.zsa.io/2003-oryx-macros/) for the macros is holding back this keyboard's potential.

This tool is created so that you can still use the oryx layout tool but still input your own complex macros.

I wanted to add macros that would be used for vim keystrokes so that I wouldn't have to upload/modify vimrc.


## Build and Usage Process
Requires python3 and docker
Note: for now this is only for linux or NIX base systems, pending windows testings

- docker image
- oryx layout with macro identifiers
- update the custom-mapping csv file
- run firmware compiler


## Usage
git clone https://github.com/jonberenguer/oryx-complex-macros.git
cd oryx-complex-macros
python app.py

*pending more steps

