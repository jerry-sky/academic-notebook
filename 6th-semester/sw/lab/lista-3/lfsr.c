#include <stdio.h>
#include <stdlib.h>
#include "shift_lfsr.h"

int main(int argc, char** argv)
{

    long max = 1;

    if(argc != 2) {
        printf("exactly one argument needed\n");
        return 1;
    }

    char *p;
    max = strtol(argv[1], &p, 10);

    const unsigned int init = 10;
    unsigned int v = init;

    int i = 0;

    do {
        v = shift_lfsr(v);
        i++;
        putchar(((v & 1) == 0) ? '0' : '1');
        printf("\n");
    } while (i < max * 8);
    // } while (v != init);

    return 0;
}
