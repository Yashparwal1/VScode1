// #include<stdio.h>
// #include<conio.h>

// int main(int argc, char const *argv[])
// {
//     printf("hello world");
//     printf("\x03");
//     return 0;
// }

#include <stdio.h>
#include <gmp.h>

int main() {
    mpz_t a, b, result;
    mpz_init(a);
    mpz_init(b);
    mpz_init(result);

    // Set the values of a and b to two 100-digit numbers
    mpz_set_str(a, "1234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890", 10);
    mpz_set_str(b, "9876543210987654321098765432109876543210987654321098765432109876543210987654321098765432109876543210", 10);

    // Multiply a and b and store the result in result
    mpz_mul(result, a, b);

    // Print the result
    gmp_printf("%Zd\n", result);

    // Clear the memory used by a, b, and result
    mpz_clear(a);
    mpz_clear(b);
    mpz_clear(result);

    return 0;
}