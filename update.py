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


def replaceAdmonition(filepath, flags=0):
    adOpen = re.compile(r'\s{0,1}>\s\[!(\w+)\]([-\+\s]*)(.*)', flags)
    adLine = re.compile(r'^\s{0,1}>\s+(?!\[!\w+\])(.*)')

    with open(filepath, 'r') as f:
        contents = f.readlines()
        for i,line in enumerate(contents):
            if m := adOpen.match(line):
                if m.group(3):
                    contents[i] = line.replace(line,f'!!! info "{m.group(3)}"\n')
                else:
                    contents[i] = line.replace(line,f'!!! info\n')
            elif m := adLine.match(line):
                contents[i] = line.replace(line,f'    {m.group(1)}\n')

    f.close()
    f = open(filepath, 'w')
    f.writelines(contents)


def main():
    with open('update_cfg.yaml') as f:
        config = yaml.safe_load(f)

    
    for item in enumerate(config['filecopy']):
        section = item[1]
        for name in config['filecopy'][section]:
            # name is the name of the section and contains
            # a dict with the name, src, and dst paths.
            for key in name:
                if key == 'src':
                    for n, src in enumerate(name[key]):
                        dst = name['dst'][n]
                        print(f"Processing source directory: {src}")
                        
                        # Copy files
                        for filepath in Path(src).rglob('*.md'):
                            print(f"  Copying file: {filepath.name} => {dst}")
                            #replaceAdmonition(filepath)
                            shutil.copy(filepath, dst)

                        # Update admonitions
                        for file in Path(dst).rglob('*.md'):
                            print(f"  Updating admonitions in file: {file.name}")
                            replaceAdmonition(file)
                    
            
        

if __name__ == '__main__':
    print('Starting...')
    main()