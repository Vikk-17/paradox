#include <stdio.h>
#include <string.h>
#include <stdlib.h>

void decrypt(const char *input) {
    char *token = strtok((char *)input, ","); 

    while (token != NULL) {
        int num = atoi(token);  
        if (num >= 1 && num <= 26) {  
            printf("%c", num + 'a' - 1); 
        }
        token = strtok(NULL, ","); 
    }
}

int main() {
    char input[] = ", , , , , "; // Hidden message
    printf("Flag: SMVIT{");
    decrypt(input);
    printf("}\n");
    return 0;
}
