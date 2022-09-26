#!/usr/bin/env python3

from pathlib import Path
import shutil
import yaml
import re
import colorama

def progressBar(value, endvalue, bar_length=20):
    percent = float(value) / endvalue
    arrow = '-' * int(round(percent * bar_length)-1) + '>'
    spaces = ' ' * (bar_length - len(arrow))

    print("Progress: [{0}] {1}%".format(arrow + spaces, int(round(percent * 100))), end='\r')