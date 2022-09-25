import re
from pathlib import Path

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
    for filepath in Path('./docs').rglob('*.md'):
        print('Processing: ', filepath)
        replaceAdmonition(filepath)
        
if __name__ == '__main__':
    print('Starting...')
    main()