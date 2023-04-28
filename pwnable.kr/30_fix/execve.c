#include <unistd.h>

int main() {
  execve("/bin/sh", 0);
}
