# Definir el compilador
CC = gcc

# Definir las opciones del compilador
CFLAGS = -Wall -Wextra -Werror

# Definir el nombre del archivo ejecutable
TARGET = main

# Definir los archivos fuente
SRCS = main.c

# Definir los archivos objeto (el mismo nombre que los archivos fuente pero con extensión .o)
OBJS = $(SRCS:.c=.o)

# Regla por defecto: compilar, ejecutar y limpiar el programa
all: $(TARGET) run clean

# Regla para compilar el archivo ejecutable
$(TARGET): $(OBJS)
	$(CC) $(CFLAGS) -o $(TARGET) $(OBJS)

# Regla para compilar los archivos objeto
%.o: %.c
	$(CC) $(CFLAGS) -c $< -o $@

# Regla para ejecutar el programa
run: $(TARGET)
	./$(TARGET)

# Regla para limpiar los archivos generados
clean:
	del $(OBJS) $(TARGET).exe