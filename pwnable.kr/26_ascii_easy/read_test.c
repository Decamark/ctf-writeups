#include <stdio.h>
#include <unistd.h>

int main()
{
  char buf[100];
  read(0, buf, 100);
  printf("%s", buf);
}
