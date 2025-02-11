# Proyecto API Diccionario

Este proyecto consiste en una API que proporciona funcionalidades de diccionario, junto con una página web que sirve como interfaz de usuario. La web es completamente dinámica, interactuando con la API para obtener datos y mostrar definiciones, sin necesidad de recargar la página.

## Descripción

El objetivo principal de este proyecto es proporcionar un servicio en línea para consultar definiciones y demás de palabras en varios idiomas. La API expone endpoints para la consulta de palabras y sus definiciones, mientras que la web utiliza esos endpoints para mostrar los resultados de manera interactiva.

### Arquitectura del Proyecto

El proyecto está compuesto por dos partes principales:

1. **API (Backend)**
   - La API está construida para manejar peticiones HTTP RESTful.
   - Los endpoints permiten consultar definiciones de palabras, obtener información sobre sinónimos, antónimos, etc.
   - La API devuelve los resultados en formato JSON para que la web pueda procesarlos fácilmente.
   
2. **Web (Frontend)**
   - La web es una aplicación dinámica construida con tecnologías como HTML, CSS y JavaScript.
   - La web realiza peticiones a la API para obtener los datos.
   - Los resultados se presentan al usuario de manera intuitiva y visualmente atractiva, sin recargar la página, gracias a la manipulación dinámica del DOM mediante JavaScript.

### Flujo de Trabajo

1. El usuario ingresa una palabra en el campo de búsqueda de la web.
2. La web envía una solicitud a la API para obtener la definición de la palabra.
3. La API procesa la solicitud y responde con un objeto JSON que contiene la información solicitada (por ejemplo, definición, ejemplos de uso, sinónimos).
4. La web recibe la respuesta y actualiza el contenido de la página sin necesidad de recargarla, mostrando los resultados de manera dinámica.

## Tecnologías Utilizadas
  
- **HTML, CSS y JavaScript** para la estructura y el diseño de la página.
- **Python + Flask** para manejar la API.
- **MongoDB** para manejar la base de datos.

## Instalación

### Backend (API)

1. **Clonar el repositorio**:
    Si aún no tienes el repositorio en tu máquina, clónalo usando Git:
    ```bash
    git clone https://github.com/usuario/diccionario-api.git
    ```

2. **Instalar Python**:
    Si no tienes python, para instalarlo tienes que irte a la página oficial:
    https://python.org

3. **Instalar requisitos e iniciar la API**:
    Para iniciar la API, tienes que seguir los siguientes pasos:
    ```bash
    cd API
    pip install -r requirements.txt
    python app.py
    ```

4. **Preparar la base de datos (MongoDB)**:
    Para hacer esto, simplemente entras en app.py, y en la linea 14 cambias la string URL de conexión por la que sea funcional.

## Créditos

Para que este proyecto haya salido a la luz, se han usado previamente otro repositorio el cual ha servido como ayuda para que funcione de forma correcta (aunque de este mismo han sido modificados algunos endpoints para adaptarlo a las necesidades del proyecto):

https://github.com/oswandor/APIDiccionario

