# El compilador
CC = gcc

# Opciones del compilador
CFLAGS = -Wall -g

# Archivos de origen
SRCS = main.c

# Archivos de cabecera
HEADERS = variables.h

# Nombre del ejecutable
TARGET = main

# Regla por defecto
all: $(TARGET)

# Regla para compilar el ejecutable
$(TARGET): $(SRCS) $(HEADERS)
    $(CC) $(CFLAGS) $(SRCS) -o $(TARGET)

# Regla para limpiar archivos generados
clean:
    rm -f $(TARGET)