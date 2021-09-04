import os
import sys


file_handle = open('config.txt', mode='w')
file_handle.write(os.getcwd())
file_handle.close()
file_handle = open('config.txt', mode='a')
file_handle.write('/file')
file_handle.close()

print ('Auto setup successfully!')

sys.exit(0)