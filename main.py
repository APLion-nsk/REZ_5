import sys
import os

if __name__ == "__main__":
    classname = sys.argv[1]
    ans = set()
    comm = f'javap -c {classname} | grep invokevirtual > dump'
    os.system(comm)
    with open('dump', 'r') as in_file:
        for line in in_file:
            line = line.strip()
            line = line[line.rfind(' ') + 1:]
            line = line.split(':')
            classname = line[0]
            if '.' in classname:
                classname = classname[:classname.rfind('.')]
                if '/' in classname:
                    classname = classname[classname.rfind('/') + 1:]
                ans.add(classname)
            arguments = line[1]
            brackets = arguments[:arguments.rfind(')') + 1]
            arguments = arguments[arguments.rfind(')') + 1:]
            if arguments[-1] == ';':
                arguments = arguments[:-1]
            if '/' in arguments:
                arguments = arguments[arguments.rfind('/') + 1:]
            ans.add(arguments)
            brackets = brackets[1:-1].split(';')
            for cl in brackets:
                if cl == '':
                    continue
                if '/' in cl:
                    cl = cl[cl.rfind('/') + 1:]
                ans.add(cl)
    print(*ans, sep='\n')
    os.system('rm dump')


