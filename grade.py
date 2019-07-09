#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys, time, os, subprocess, time, shutil, json, h5py
import numpy as np

testcases = [
    ('data/interpolation_1.in', 'data/interpolation_1.out'),
    ('data/interpolation_2.in', 'data/interpolation_2.out'),
    ('data/interpolation_3.in', 'data/interpolation_3.out'),
    ('data/interpolation_4.in', 'data/interpolation_4.out'),
]

shape = np.zeros((18, 41))

if __name__ == '__main__':

    if sys.version_info[0] != 3:
        print("Please use python3")
        exit(1)

    program_file = 'interpolation.py'
    if len(sys.argv) > 1: 
        program_file = sys.argv[1]
    
    if not os.path.isfile(program_file):
        print('File {} not present!'.format(program_file))
        exit(1)

    success_count = 0

    for input, output in testcases:
        # remove the output file
        test_filename = 'test.output'
        try:
            os.remove(test_filename)
        except:
            pass
        p = subprocess.Popen([sys.executable, program_file, input, test_filename], stdout=open(os.devnull,'w'), stderr=subprocess.PIPE)
        message = ''
        success = True
        start_time = time.time()
        while p.poll() is None:
            if time.time() - start_time > 2:
                p.terminate()
                message = 'Time limit exceeded'
                success = False
                break
        else:
            if not os.path.isfile(test_filename):
                message = 'No output file found'
                success = False
            else:
                try:
                    inp = json.load(open(input))
                    std = json.load(open(output))
                    ans = json.load(open(test_filename))
                    
                    for a, pre in zip(ans, inp['predict']):
                        if 1 < a and a < 3:
                            shape[9 - round(a * 10)][round(pre * 20) + 20] = 1

                    if np.linalg.norm(np.array(std) - np.array(ans)) > 0.01:
                        message = 'Data mismatch: should be \n\'{}\'\n, get \n\'{}\''.format(std, ans)
                        success = False
                except:
                    message = 'Could not find valid output data'
                    success = False
                    pass
        if success:
            success_count += 1
            if os.isatty(1):
                print('Testcase {}: PASS using {:.2f} seconds'.format(input, time.time() - start_time))
        else:
            if os.isatty(1):
                print('Testcase {}: {}'.format(input, message))
                stdout, stderr = p.communicate(timeout=1)
                if len(stderr) > 0:
                    print('       : your program exited with:')
                    sys.stdout.buffer.write(stderr)

        print('Current shape (if you have implemented correcly, you should see a heart):')
        for row in shape:
            for ele in row:
                if ele > 0:
                    print('#', end = '')
                else:
                    print('.', end = '')
            print()

        
        
    grade = int(100.0 * success_count / len(testcases))
    
    if os.isatty(1):
        print('Total Points: {}/100'.format(grade))
    else:
        print(json.dumps({'grade': grade}))

