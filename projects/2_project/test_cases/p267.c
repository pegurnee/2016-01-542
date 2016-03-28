static int max = 0;

void A(int b, int e)
{
  int a, c, d, p;
  a = B(b);

  if (b > 100) {
    c = a + b;
    d = c * 5 + e;
  }
  else
    c = a * b;
  *p = c;
  C(&p);
}

int B(int k)
{
  int x, y;
  x = pow(2, k);
  y = x * 5;
  return y;
}

void C(int *p)
{
  if (*p > max)
    max = *p;
}
