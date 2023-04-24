#include <stdio.h>
#include <stdint.h>
#include <stdlib.h>
#include <limits.h>
#include "mystring.h"

int64_t mystrlen(const char *nptr) {
    int64_t count = 0;

    if(nptr == NULL) {
        return 0;
    }

    while(1) {
        if(nptr[count] != '\0') {
            count++;
        }
        else {
            break;
        }
    }

    return count;
}

char *mystrchr(const char *s, int c) {
    int64_t count = mystrlen(s);

    char str[count];

    for(int64_t i = 0;i < count;i++) {
        str[i] = 0;
        str[i] = s[i];
    }

    for(int64_t i = 0;i < count;i++) {
        if(str[i] == (char)c) {
            return (char*) s+i;
        }
    }

    return NULL;
}

char *mystrrchr(const char *s, int c) {
    int64_t count = mystrlen(s);

    char str[count];

    for(int64_t i = 0;i < count;i++) {
        str[i] = 0;
        str[i] = s[i];
    }

    for(int64_t i = count - 1;i >= 0;i--) {
        if(str[i] == (char)c) {
            return (char*)s + i;
        }
    }

    return NULL;
}

size_t mystrspn(const char *s, const char *accept)
{
    int64_t sCount = mystrlen(s);
    int64_t aCount = mystrlen(accept);

    int check = 0;

    for(int64_t i = 0;i < sCount;i++) {
        check = 0;

        for(int64_t j = 0;j < aCount;j++) {
            if(s[i] == accept[j]) {
                check = 1;
            }
        }

        if(check == 0) {
            return i;
        }
    }

    return aCount - 1;
}

size_t mystrcspn(const char *s, const char *reject) {
    int64_t sCount = mystrlen(s);
    int64_t rCount = mystrlen(reject);

    int64_t i = 0;

    for(i = 0;i < sCount;i++) {
        for(int64_t j = 0;j < rCount;j++) {
            if(s[i] == reject[j]) {
                return i;
            }
        }
    }

    return i;
}

char *mystrpbrk(const char *s, const char *accept) {
    int64_t sCount = mystrlen(s);
    int64_t aCount = mystrlen(accept);

    for(int64_t i = 0;i < sCount;i++) {
        for(int64_t j = 0;j < aCount;j++) {
            if(s[i] == accept[j]) {
                return (char*)s + i;
            }
        }
    }

    return NULL;
}

char *mystrstr(const char *haystack , const char *needle) {
    int64_t hCount = mystrlen(haystack);
    int64_t nCount = mystrlen(needle);

    for(int64_t i = 0;i < hCount - nCount + 1;i++) {
        int check = 0;
        for(int64_t j = 0;j < nCount - 1;j++) {
            if(haystack[i] == needle[j]) {
                check++;
            }
            else {
                break;
            }
        }

        if(check == nCount - 1) {
            return (char*)haystack + i;
        }
    }

    return NULL;
}

char *mystrtok(char *str, const char *delim) {
    static char* new;

    if(str == NULL && new != NULL) {
        str = new;
    }
    else if(str == NULL && new == NULL) {
        return NULL;
    }

    size_t spn = mystrspn(str,delim);

    str += spn;

    size_t cspn = mystrcspn(str,delim);

    if(spn > 0 && cspn == 0) {
        return NULL;
    }

    *(str + cspn) = '\0';
    new = str + cspn + 1;
    
    if(*new == '\0') {
        new = NULL;
    }

    return str;
}