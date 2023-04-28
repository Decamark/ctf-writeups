#include <stdio.h>
#include <unistd.h>

int main(int argc, char** argv)
{
  execv("/bin/sh", NULL);
  execve("/bin/sh", NULL, NULL);
}
