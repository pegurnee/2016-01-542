import os, sys

from tablemanager import TableManager

def main():
  fname = input('enter file name: ')
  with open('test_cases/' + fname) as f:
    for line in f:
      man.parse_line(line)

  print('Your table is served:')
  print('=' * 40)
  print(man.table)
  print('=' * 40)

if __name__ == '__main__':
  main()
