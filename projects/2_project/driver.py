import os, sys, getopt

from tablemanager import TableManager

def main():
  if len(sys.argv) == 2:
    infile = sys.argv[1]
    outfile = sys.argv[1][ : sys.argv[1].rfind('.') + 1] + 'sym'
  elif len(sys.argv) == 3:
    infile = sys.argv[1]
    outfile = sys.argv[2]
  else:
    infile = input('enter file name: ')

  man = TableManager('test_cases/' + infile)

  print('Your table is served:')
  print('=' * 40)
  print(man.table)
  print('=' * 40)

  with open(outfile, 'w') as f:
    f.write(str(man))

if __name__ == '__main__':
  main()
