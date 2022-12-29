import os
import platform
from tqdm import tqdm as tq
import time as t

print(f'''System: {platform.system()}
Node: {platform.node()}
Release: {platform.release()}
Version: {platform.version()}
Machine: {platform.machine()}
Processor: {platform.processor()}''')
print('')

for i in tq(range(100), desc="Processing"):
    t.sleep(0.1)

print('')

while exit:
    try:
        a = input(f'{os.getcwd()}> ')
        os.system(f'cmd /k {a}')
    except OSError:
        print('please enter correct and reliable command')