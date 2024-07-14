// Include dice que se incluirá la librería stdio.h
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

void variables();
void colecciones();
void estructures();

// void main(int argc, char *argv[])
void main(int argc, char **argv)
{
    printf("Hello %s. %d arguments were passed\n", argv[1], argc);
    for (int i = 0; i < argc; i++)
    {
        printf("Argument %d: %s\n", i, argv[i]);
    }
    // argc guarda el número de argumentos pasados
    // argv guarda los argumentos pasados
    // Llamado a función variables
    // variables();
    // colecciones();
    estructures();
}

void variables()
{
    // Declaración de todas variables en C
    int a0 = 10; // Tiene bytes de 4

    long a1 = 1000000000; // Tiene bytes de 4
    printf("El valor de a es %d\n", a0);
    float b = 10.5;
    char c = 'H';
    char d[] = "Hello";

    // Declaración de punteros
    int *p;
    p = &a0;
    // Declaración de constantes
    const int e = 10;
    // Declaración de variables globales
    extern int f;
    // Declaración de variables estáticas
    static int g = 10;
    // Declaración de variables volátiles
    volatile int h = 10;
    // Declaración de variables de registro
    register int i = 10;
    // Declaración de variables de tipo definido por el usuario
    typedef int entero;
    entero j = 10;
    // Declaración de variables de tipo definido por el usuario
    enum color
    {
        rojo,
        verde,
        azul
    };
    enum color k = rojo;
    // Declaración de variables de tipo definido por el usuario
    union numero
    {
        int l;
        float m;
    };
    union numero n;
    n.l = 10;
    n.m = 10.5;

    // Declaración de variables de tipo definido por el usuario
    struct persona
    {
        char nombre[50];
        int edad;
    };
    struct persona o;
    o.edad = 10;
}

void colecciones()
{
    int a[5] = {1, 2, 3, 4, 5};
    printf("El valor de a[0] es %d\n", a[0]);
    printf("El valor de a[1] es %d\n", a[1]);
    printf("El valor de a[2] es %d\n", a[2]);
    printf("El valor de a[3] es %d\n", a[3]);
    printf("El valor de a[4] es %d\n", a[4]);
    printf("El valor de a[5] es %d\n", a[5]); /* No debería  star */
}

void estructures()
{
    struct persona
    {
        char nombre[50];
        int edad;
    };
    struct persona p;
    p.edad = 10;
    strcpy(p.nombre, "Juan");
    printf("\nEl valor de p.nombre es %s y p.edad es %d\n", p.nombre, p.edad);
}