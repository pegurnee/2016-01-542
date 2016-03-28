int fib(int n) {
  int x = 1;
  int y = 1;
  int z = 1;
    while(n > 1)
       z = x + y;
       x = y;
       y = z;
       n = n - 1;
  return z;
}
