#!/bin/env python3

import zipfile
from os import listdir, path, mkdir, replace
from custom_macros import new_mapping


wrkdir = "."
zsa_kbs = ("ergodox_ez", "ergodox_ez_glow", "ergodox_ez_shine", "planck_ez", "planck_ez_glow", "moonlander")
csvmappingfile = "datasets/custom-mapping.csv"


def is_exist_mapping():
    return path.exists(path.join(wrkdir, csvmappingfile))


def get_zsa_sources():
    files = listdir(wrkdir)
    return [x for x in files if any(word in x for word in zsa_kbs)]


def extract(zipsource, dest):
    with zipfile.ZipFile(zipsource, 'r') as zip_ref:
        #zip_ref.extractall(dest)

        # extract only the necessary files
        targetfiles = ("config.h", "keymap.c", "rules.mk")
        zipfiles = zip_ref.namelist()

        for zf in zipfiles:
            for tf in targetfiles:
                if tf in zf:
                    zip_ref.extract(zf, dest)

        returnvalues = []
        #moves all extracted files/dir to generic directory
        for d in listdir(dest):
            sd = path.join(dest,d)
            kbtype = [x for x in zsa_kbs if x in d]
            if len(kbtype) > 1:
                genericpath = path.join(dest, (kbtype[1] + "_personalized_source"))
                #mkdir(genericpath)
                replace(sd,genericpath)
                returnvalues.append((kbtype[1], genericpath))
            else:
                genericpath = path.join(dest, (kbtype[0] + "_personalized_source"))
                #mkdir(genericpath)
                replace(sd,genericpath)
                returnvalues.append((kbtype[0], genericpath))

        return returnvalues

def get_keymap_files(source):
    return [path.join(path.join(source, x), "keymap.c") for x in listdir(source) if "_source" in x]


def generate_csv():
    while True:
        idmap = input("idmap: ")
        macro = input("macro: ")

        with open(csvmappingfile, "a") as mfile:
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

    dest = path.join(wrkdir, "temp")

    extracted = []
    for sfile in source_files:
        if ".zip" in sfile:
            extracted = extract(sfile, dest)

    keymap_files = get_keymap_files(dest)

    for kf in keymap_files:
        new_mapping.update_keymap(csvmappingfile, kf)
        new_mapping.post_fix(kf)


    print("Verify the changes in the source keymap files, then run the commands below:")

    for kbtype, srcpath in extracted:
        print("./build-custom-fw {}".format(kbtype))


if __name__ == "__main__":
    main()
