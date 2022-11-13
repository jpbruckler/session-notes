#!/usr/bin/env python3

from pathlib import Path
import shutil
import yaml
import re
import os
import colorama

def progressBar(value, endvalue, bar_length=20):
    percent = float(value) / endvalue
    arrow = '-' * int(round(percent * bar_length)-1) + '>'
    spaces = ' ' * (bar_length - len(arrow))

    print("Progress: [{0}] {1}%".format(arrow + spaces, int(round(percent * 100))), end='\r')


def replaceAdmonition(filepath, flags=0):
    MATERIAL_SUPPORTED_ADMONITIONS = {
        'note',
        'abstract',
        'info',
        'tip',
        'success',
        'question',
        'warning',
        'failure',
        'danger',
        'bug',
        'example'}
    # regex matches the opening syntax for obsidian admonitions
    adOpen = re.compile(r'\s{0,1}>\s?\[!(\w+)\][-\+\s]*(.*)', flags)

    # regex matches lines starting with '>' without an admonition
    # starter following.
    adLine = re.compile(r'^\s{0,1}>+(?!\[!\w+\])(.*)')


    with open(filepath, 'r') as f:
        contents = f.readlines()
        for i,line in enumerate(contents):
            if m := adOpen.match(line):
                # m.group(1) - the type of admonition it is
                # m.group(2) - a title, if one exists
                if m.group(1) == 'aside':
                    contents[i] = line.replace(line,f'!!! info inline end\n')
                elif m.group(1) in MATERIAL_SUPPORTED_ADMONITIONS:
                    if m.group(2):
                        contents[i] = line.replace(line,f'!!! {m.group(1)} "{m.group(2)}"\n')
                    else:
                        contents[i] = line.replace(line,f'!!! {m.group(1)}\n')
                else:
                    contents[i] = line.replace(line,f'!!! info\n')
            elif m := adLine.match(line):
                # m.group(1) - the line
                string = m.group(1).strip()

                if re.match('^#{1,8}', string):
                    # lines that start with a header character need a blank line
                    # for them to show up properly in mkdocs
                    contents[i] = line.replace(line,f'\n    {string}\n')
                else:
                    contents[i] = line.replace(line,f'    {string}\n')
    f.close()
    f = open(filepath, 'w')
    f.writelines(contents)
    f.close()


def main():
    EXTENSIONS = {'.md', '.jpg','.jpeg', '.png', '.gif'}
    
    with open('update_cfg.yaml') as f:
        config = yaml.safe_load(f)

    
    for item in enumerate(config['filecopy']):
        section = item[1]
        for item in config['filecopy'][section]:
            srcDir = os.path.join(config['base_dir'], item['src'][0])
            dstDir = item['dst'][0]

            for filepath in Path(srcDir).glob(r'**/*'):
                # Run through all the files in srcDir that have a file
                # extension in EXTENSIONS. Copy to the defined destination
                if filepath.suffix in EXTENSIONS:
                    print(f"  Copying file: {filepath.name} => {dstDir}")
                    try:
                        shutil.copy(filepath, dstDir)
                    except shutil.SameFileError:
                        print("Source and destination file are the same.")
                    except PermissionError:
                        print("Permission denied.")
                    except:
                        print("An error occurred while copying a file.")

            # Update admonitions
            for file in Path(dstDir).rglob('*.md'):
                print(f"  Updating admonitions in file: {file.name}")
                replaceAdmonition(file)  


if __name__ == '__main__':
    print('Starting...')
    main()