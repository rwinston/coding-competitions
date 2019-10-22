#include <stdio.h>
#include <inttypes.h>
#include <stdlib.h>

int main()
{
    uint64_t le = 0x60ef358d6762ac08;
    uint64_t be = _byteswap_uint64(le);

    printf("Little-endian: 0x%" PRIx64 "\n", le);
    printf("Big-endian:    0x%" PRIx64 "\n", be);

   printf("%lu\n", be);
       return 0;
}