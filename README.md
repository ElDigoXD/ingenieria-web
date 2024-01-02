# Índice

- [Público objetivo](#Público-objetivo)
- [Historias de usuario](#Historias-de-usuario)
- [Iteraciones](#Iteraciones)
- [Instalación](#Instalación)
	- [Desarrollo](##Versión-de-desarrollo)
	- [Producción](##Versión-de-producción)
- [Referencias](#Referencias)
- [Historial](#Historial)
---

Tareas por hacer

- [x] Revisar historias
- [x] Crear iteraciones
- [x] Numerar las historias
- [x] Indicar las historias / requisitos funcionales en las iteraciones
- [ ] Listar los requisitos no funcionales en limpio
- [ ] ---
- [x] Permitir conexiones 0.0.0.0
- [ ] Añadir admin a static
- [ ] Apache https
- [ ] ---
- [ ] Redactar Introducción, Motivación y Objetivos
- [ ] Buscar el estado del arte
- [ ] Definir arquitectura
- [ ] Mapa del sitio web (arbol)
- [ ] Despliegue en VM
- [ ] Conclusiones
- [ ] Bibliografía

---

# Público objetivo

## Visitante / Anónimo

- Ver página de inicio, about me, contacto, etc.


## Cliente / Registrado

- Iniciar sesión
- Consultar dieta
- Consultar evolución
- ¿Añadir seguimiento?
- Contactar con el nutricionista

## Nutricionista / admin

- Iniciar sesión
- Gestionar clientes 
- Proveer nivel de actividad (nulo, moderado, elevado, intenso)
- Generar serie de alimentos para 5 comidas
- Gestionar alimentos
- Consultar histórico dietas
* Evolución del cliente
- Copiar y modificar dietas.

---

# Historias de usuario

Los criterios se validarán junto al usuario en pruebas de funcionalidad.

- 1. **Como** visitante **quiero** ver la pagina de inicio **para** informarme sobre el servicio
	- Criterios:
		- La página de inicio contiene información sobre el servicio
		- Permite acceder a una página de contacto
		- Permite acceder a una página de _about me_

- 2. **Como** visitante **quiero** contactar con el nutricionista **para** obtener más información y/o convertirme en cliente
	- Criterios:
		- La página de contacto proveerá información de contacto del nutricionista
		- También contendrá un correo electrónico con un "mailto:"

- 3. **Como** cliente o nutricionista **quiero** iniciar sesión **para** acceder al servicio
	- Criterios:
		- Todas las páginas accesibles sin iniciar sesión contendrán una manera de hacerlo.
		- Se podrá cerrar sesión desde esas páginas una vez iniciada.

- 4. **Como** cliente **quiero** consultar la dieta **para** alimentarme correctamente
	- Criterios:
		- La página del usuario contiene información sobre su dieta activa

- 5. **Como** cliente o nutricionista **quiero** consultar la evolución **para** comprobar si mejora
	- Criterios:
		- La página del usuario contiene información sobre su evolución

- 6. **Como** cliente **quiero** contactar con el nutricionista **para** consultar mis dudas
	- Prioridad: muy baja
	- Criterios:
		- O existe un formulario para comunicarse con el nutricionista
		- O se realiza todo por teléfono

- 7. **Como** nutricionista **quiero** gestionar clientes **para** dar de alta, dar de baja y modificar los datos de mis clientes 
	- Criterios:
		- Poder dar de alta clientes con su:
			- nombre
			- teléfono
			- peso
			- altura
			- correo
			- nivel de actividad
			- formula de calorías personalizada
		- Poder dar de baja a clientes
		- Poder modificar los datos de los clientes

- 8. **Como** nutricionista **quiero** generar series de alimentos para 5 las comidas del cliente **para** optimizar su ingesta de calorías
	- Criterios:
		- Poder generar una lista de alimentos basada en:
			- grasas
			- proteínas 
			- hidratos de carbono

- 9. **Como** nutricionista **quiero** gestionar los alimentos **para** crear, modificar las propiedades y eliminar alimentos.
	- Criterios:
		- Poder:
			- Crear
			- Modificar las propiedades
			- Y eliminar alimentos

- 10. **Como** nutricionista **quiero** ver dietas anteriores del cliente, copiar y modificar dietas **para** no tener que crearlas desde cero
	- Criterios:
		- Poder ver un historico de dietas del cliente
		- Copiar dietas
		- Modificar dietas

---

# Iteraciones

## Iteración 1

Implementar la página web base funcional que permita a los visitantes anónimos cumplir todas sus historias.

- Historias: 1, 2
- Crear plantilla base de la página
- Implementar página de inicio
- Implementar página about me
- Implementar página contacto

## Iteración 2 (Revisable) 

Implementar login, sesiones y autenticación para diferenciar los roles.

- Historias: 3
- Implementar pagina de login (o modal)
- Implementar botón de logout
- Crear la base para una página "home" personalizada dependiendo del rol

## Iteración 3 (Revisable) 

Implementar la CRUD de las dietas y el seguimiento

- Historias: 4, 5
- Implementar CRUD de dietas para el nutricionista (nutricionista)
- Implementar copia de dietas (nutricionista)
- Implementar consulta de dietas (cliente y nutricionista)
- Implementar seguimiento del cliente (cliente y nutricionista)
- Modificar la página "home" personalizada del rol con las nuevas funcionalidades
- Cargar los alimentos en la BBDD

## Iteración 4 (Revisable) 

- Historias 7, 9
Crear CRUD de los alimentos y de los usuarios (nutricionista)

- Implementar página de gestión de usuarios con posibilidad de CRUD
- Implementar página de gestión de alimentos con posibilidad de CRUD

## Iteración 5 (Revisable) 

A definir. ¿6, 8, 10?


---

Requisitos en sucio:

- bbdd
- web de gestion
- web de usuario
- api rest
- multi-idioma
- gráficas de evolución
- búsquedas autocompletadas
- calculo imc
- calculo % grasa corporal
- generar serie de alimentos para 5 comidas basado en ratios y restricciones
- catalogar alimentos
- dias excepcionales (opcional)
- modificación temporal (opcional)
- crear nuevas dietas y modificar las activas
- histórico de dietas y evoluciones
- copiar dietas
- calcular calorías necesarias
- variar formulas calorías

---

# Instalación

## Versión de desarrollo

1. Instalar python 3.12 y su modulo "venv"
2. Clonar el repositorio y entrar en su carpeta (git clone ...; cd ingeniería-web)
3. Crear un entorno virtual (python3.12 -m venv venv)
4. Activar el entorno virtual (source ./venv/bin/activate)
5. Instalar las dependencias (pip install -r requirements.txt)
6. Ejecutar el servidor de desarrollo (python manage.py runserver)


## Versión de producción

1. Instalar python, dev, apache, dev, mod_wsgi
2. Clonar el repositorio y entrar en su carpeta (git clone ...; cd ingeniería-web)
3. Crear un entorno virtual (python3.12 -m venv venv)
4. Activar el entorno virtual (source ./venv/bin/activate)
5. Instalar las dependencias (pip install -r requirements.txt)
6. Dar permisos a la base de datos y al directorio (chmod o+w ...)
7. Configurar apache con la ruta de la aplicación
8. Reiniciar apache

Fuente: [django](https://docs.djangoproject.com/en/5.0/howto/deployment/wsgi/modwsgi/)

---

# Referencias

- [Django](https://www.djangoproject.com/)
- [htmx](https://htmx.org/)
- [Extensión django-htmx](https://django-htmx.readthedocs.io/)
- [Bootstrap](https://getbootstrap.com/)
- [Plantilla por Start Bootstrap](https://startbootstrap.com/template/modern-business)
- [Generador de personas](https://thispersondoesnotexist.com/)

---

# Historial

20/12/23

- Creación del proyecto Django
- Prueba de la plantilla bs
- Configuración contenido static
- Extensión htmx

21/12/23

- Soporte de traducción estática

22/12/23

- Creación de la plantilla base
- Importación de la pagina de contacto de la plantilla
- htmx boosting
- htmx formularios
- Validación de formularios bs + htmx

29/12/23

- Numerar las historias
- Añadir la numeración de las historias a las iteraciones
- Personalizar el home
- Personalizar la página de contacto (sin funcionalidad)
- Importación de la pagina de _about_ de la plantilla

30/12/23

- Personalizar la pagina de _about_
- Despliegue en apache de la iteración 1
- Implementación del sistema de login

31/12/23

- Editar pagina login cuando se está logeado (¿redireccion en un futuro?)
- Añadir grupos
- Redirección a proto-pagina home por grupo 
- Ampliación about me
- Ampliacion contacto
