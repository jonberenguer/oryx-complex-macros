import re
import csv
from pathlib import Path

def wrapper(x):
    if x.isupper():
        return "SS_LSFT(SS_TAP(X_{})) SS_DELAY(100) ".format(x.upper())
    elif x == " ":
        return "SS_TAP(X_SPACE) SS_DELAY(100) "
    else:
        return "SS_TAP(X_{}) SS_DELAY(100) ".format(x.upper())

def outputidmap(string):
    concat_macro = ""

    for x in string:
        concat_macro += wrapper(x)

    # removes the list delay code
    return "{}".format(concat_macro[:-15])

def outputmacro(string):
    concat_macro = ""

    for x in string:
        concat_macro += wrapper(x)

    return "      SEND_STRING({});".format(concat_macro[:-1])


def new_macro(idmap, string):
    key = outputidmap(idmap)
    value = outputmacro(string)
    return "{}\t{}".format(key, value)


def update_keymap(customcsv, keymapfile):
    keymap = Path(keymapfile)
    keymaptxt = keymap.read_text()
    csvfile = Path(customcsv).read_text()
    reader = csv.reader(csvfile.splitlines(), delimiter='\t')

    for row in reader:
        escword = re.escape("{}".format(row[0]))
        keymaptxt = re.sub(r'.*' + escword + r'.*' , row[1], keymaptxt)
        #print("replaced: {}".format(row[0]))

    keymap.write_text(keymaptxt)

def post_fix(keymapfile):
    keymap = Path(keymapfile)
    keymaptxt = keymap.read_text()
    escword = re.escape("SEND_STRING(SS_LSFT(SS_TAP(X_SCOLON))")
    keymaptxt = re.sub(escword, "SEND_STRING(SS_TAP(X_ESCAPE) SS_DELAY(100) SS_LSFT(SS_TAP(X_SCOLON))", keymaptxt)

    keymap.write_text(keymaptxt)




