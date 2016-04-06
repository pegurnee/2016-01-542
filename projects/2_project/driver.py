import os, sys, getopt

from tablemanager import TableManager

def main():
  verbose = False
  if len(sys.argv) != 1:
    opts, args = getopt.getopt(sys.argv[1:], 'i:o:v')

    if len(args) > 0:
      infile = args[0]
      outfile = args[0][ : args[0].rfind('.') + 1] + 'sym'
    if len(args) > 1:
      outfile = args[1]

    for o,a in opts:
      if o == '-i':
        infile = a
        outfile = infile[ : infile.rfind('.') + 1] + 'sym'
      elif o == '-o':
        outfile = a
      elif o == '-v':
        verbose = True

  else:
    infile = input('enter file name: ')

  man = TableManager('test_cases/' + infile)

  if verbose:
    print('Your table is served:')
    print('=' * 40)
    print(man.table)
    print('=' * 40)

  with open(outfile, 'w') as f:
    f.write(str(man))

if __name__ == '__main__':
  main()
