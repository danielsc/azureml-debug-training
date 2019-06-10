from __future__ import print_function

import argparse
import os
import sys
import socket
from azureml.core import Run

if __name__ == '__main__':
  parser = argparse.ArgumentParser()
  FLAGS, unparsed = parser.parse_known_args()
  # [sys.argv[0]]
  # ['--python_path', sys.executable] 
  ip = socket.gethostbyname(socket.gethostname())
  port = '5678'
  Run.get_context().log('debugger_ip', ip)
  Run.get_context().log('debugger_port', port)

  command_line = ' '.join(['python', '-m ptvsd', '--host', ip, '--port', port, '--wait']+unparsed)
  print('Launching:', command_line)
  os.system(command_line)