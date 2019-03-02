#!/usr/bin/python3
from glob import glob
import sys
import os
import shutil


def main():
    if (len(sys.argv) < 2):
        print("Please specify a directory for output files")
        print("Usage: ./clean.py <directory>")
        return 1
    else:

        years = [o for o in glob(sys.argv[1] + "/*") if os.path.isdir(o)]
        for y in years:
            subdirs = [o for o in glob(y + "/*") if os.path.isdir(o)]
            print(subdirs)
            for s in subdirs:
                print("Cleaning", s)
                if os.path.exists(s + "/pdf"):
                    shutil.rmtree(s + "/pdf")
                if os.path.exists(s + "/html"):
                    shutil.rmtree(s + "/html")
                xml_files = glob(s + "/*.xml")
                for x in xml_files:
                    os.remove(x)
        return 0


if __name__ == "__main__":
    main()
