# Biblioteca API - Gestión de Libros y Usuarios

## Descripción

Este proyecto implementa una API para la gestión de bibliotecas usando **FastAPI**, un framework web moderno y rápido para crear APIs en Python. Con esta API, los usuarios pueden gestionar libros, usuarios y préstamos. A lo largo de este proyecto, aprenderás a trabajar con rutas HTTP, manejar datos con Python y utilizar `FastAPI` para crear endpoints RESTful.

## Requisitos

### Gestión de Libros

- **Añadir un nuevo libro**
  - **Método**: `POST`
  - **Endpoint**: `/book`
  - **Body**:
    ```json
    {
      "title": "Clean Code"
    }
    ```
  - **Respuesta exitosa - ejemplo**:
    ```json
    {
      "id": 1,
      "title": "Clean Code",
      "status": 1
    }
    ```
  - **Error (falta de título) - ejemplo**:
    ```json
    {
      "detail": "Title is required"
    }
    ```


- **Eliminar un libro existente**
  - **Método**: `DELETE`
  - **Endpoint**: `/book/{id}`
  - **Parámetros**: `id` (ID del libro)

- **Actualizar la información de un libro**
  - **Método**: `PUT`
  - **Endpoint**: `/book/{id}`
  - **Body**:
    ```json
    {
      "title": "string"
    }
    ```

- **Leer detalles del libro**
  - **Método**: `GET`
  - **Endpoint**: `/book/{id}`
  - **Respuesta**:
    ```json
    {
      "id": "int",
      "title": "string",
      "status": "int"  // 1 = available, 2 = lent
    }
    ```

### Gestión de Usuarios

- **Añadir un nuevo usuario**
  - **Método**: `POST`
  - **Endpoint**: `/user`
  - **Body**:
    ```json
    {
      "firstName": "string",
      "lastName": "string"
    }
    ```

- **Eliminar un usuario existente**
  - **Método**: `DELETE`
  - **Endpoint**: `/user/{id}`
  - **Parámetros**: `id` (ID del usuario)

- **Actualizar la información del usuario**
  - **Método**: `PUT`
  - **Endpoint**: `/user/{id}`
  - **Body**:
    ```json
    {
      "firstName": "string",
      "lastName": "string"
    }
    ```

- **Recuperar datos del usuario**
  - **Método**: `GET`
  - **Endpoint**: `/user/{id}`
  - **Respuesta**:
    ```json
    {
      "id": "int",
      "firstName": "string",
      "lastName": "string"
    }
    ```

### Gestión de Préstamos

- **Prestar un libro a un usuario**
  - **Método**: `POST`
  - **Endpoint**: `/loan`
  - **Body**:
    ```json
    {
      "idUser": "int",
      "idBook": "int",
      "lendDate": "2024-01-01T10:00:00"
    }
    ```

- **Devolver un libro de un usuario**
  - **Método**: `PUT`
  - **Endpoint**: `/loan/{id}`
  - **Body**:
    ```json
    {
      "returnDate": "2024-01-01T10:00:00"
    }
    ```
Nota: Variables Date en formato ISO 8601 (es decir, "YYYY-MM-DDTHH:MM:SS").
## Estructura de Datos

### Book
```json
{
  "id": "int",
  "title": "string",
  "status": "int"  // 1 = available, 2 = lent
}
```

### User
```json
{
  "id": "int",
  "firstName": "string",
  "lastName": "string"
}
```

### Loan
```json
{
  "id": "int",
  "idUser": "int",
  "idBook": "int",
  "lendDate": "DateTime",
  "returnDate": "DateTime"
}
```

Nota: Los libros o usuarios no se pueden eliminar si tienen préstamos pendientes.

### Lógica de Eliminación
- **Regla 1**: Un libro no puede ser eliminado si está prestado (status = 2).
- **Regla 2**: Un usuario no puede ser eliminado si tiene algún préstamo activo.

Esta lógica asegura que los datos críticos no se pierdan o eliminen accidentalmente. Para eliminar un libro o un usuario, primero debe asegurarse de que no esté asociado a ningún préstamo activo.

# Sobre el código
## Dependencias necesarias
```
pip install fastapi uvicorn pydantic
```

## Ejecución del Proyecto
```
uvicorn app.main:app --reload
```