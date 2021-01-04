#!/bin/env python3

import zipfile
from os import listdir, path
from custom_macros import new_mapping


wrkdir = "."
zsa_kbs = ("ergodox_ez", "ergodox_ez_glow", "ergodox_ez_shine", "planck_ez", "planck_ez_glow", "moonlander")
csvmappingfile = "custom-mapping.csv"


def is_exist_mapping():
    return path.exists(path.join(wrkdir, csvmappingfile))


def get_zsa_sources():
    files = listdir(wrkdir)
    return [x for x in files if any(word in x for word in zsa_kbs)]


def extract(zipsource, dest):
    with zipfile.ZipFile(zipsource, 'r') as zip_ref:
        zip_ref.extractall(dest)


def get_keymap_files(dest):
    return [path.join(path.join(dest, x), "keymap.c") for x in listdir(dest) if "_source" in x]


def generate_csv():

    while True:
        idmap = input("idmap: ")
        macro = input("macro: ")

        with open("custom-mapping.csv","a") as mfile:
            mfile.write(new_mapping.new_macro(idmap,macro) + "\n")

        if (input("type break to stop: ")) == "break":
            break



def main():
    if is_exist_mapping():
        pass
    else:
        print("csv is missing")
        generate_csv()
        exit(1)


    source_files = get_zsa_sources()
    print(source_files)

    dest = path.join(wrkdir, "datasets")
    for sfile in source_files:
        #extract(sfile, dest)
        pass

    keymap_files = get_keymap_files(dest)
    new_mapping.update_keymap(csvmappingfile, keymap_files[0])
    new_mapping.post_fix(keymap_files[0])
    print(keymap_files[0])






if __name__ == "__main__":
    main()
