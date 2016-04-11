from tablemanager import TableManager

def main():
  test_files = ['p253.c', 'p257.c', 'p267.c', 'p324.c', 'pth-presentable.c']
  for fname in test_files:
    man = TableManager()
    with open('test_cases/' + fname) as f:
      for line in f:
        man.parse_line(line)
    print(man.table)
    print('=' * 40)

if __name__ == '__main__':
  main()
