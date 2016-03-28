int Sub(int i, int j) {
  return i - j;
}
int Mul(int i, int j) {
  return i * j;
}
int Delta(int a, int b, int c) {
  return Sub(Mul(b, b), Mul(Mul(4, a), c));
}
void main() {
 int a, b, c, delta;
 scanf("%d %d %d", &a, &b, &c);
 delta = Delta(a, b, c);
 if (delta == 0)
   puts("Two equal roots");
 else if (delta > 0)
   puts("Two different roots");
 else
   puts("No root");
}
