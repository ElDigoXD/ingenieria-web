# Índice

- [Público objetivo](#Público-objetivo)
- [Historias de usuario](#Historias-de-usuario)
- [Iteraciones](#Iteraciones)

---

Tareas por hacer

- [x] Revisar historias
- [x] Crear iteraciones
- [ ] Numerar las historias
- [ ] Indicar las historias / requisitos funcionales en las iteraciones
- [ ] Listar los requisitos no funcionales en limpio
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

- **Como** visitante **quiero** ver la pagina de inicio **para** informarme sobre el servicio
	- Criterios:
		- La página de inicio contiene información sobre el servicio
		- Permite acceder a una página de contacto

- **Como** visitante **quiero** contactar con el nutricionista **para** obtener más información y/o convertirme en cliente
	- Criterios:
		- La página de contacto proveerá información de contacto del nutricionista
		- También contendrá un correo electrónico con un "mailto:"

- **Como** cliente o nutricionista **quiero** iniciar sesión **para** acceder al servicio
	- Criterios:
		- Todas las páginas accesibles sin iniciar sesión contendrán una manera de hacerlo.
		- Se podrá cerrar sesión desde esas páginas una vez iniciada.

- **Como** cliente **quiero** consultar la dieta **para** alimentarme correctamente
	- Criterios:
		- La página del usuario contiene información sobre su dieta activa

- **Como** cliente o nutricionista **quiero** consultar la evolución **para** comprobar si mejora
	- Criterios:
		- La página del usuario contiene información sobre su evolución

- **Como** cliente **quiero** contactar con el nutricionista **para** consultar mis dudas
	- Prioridad: muy baja
	- Criterios:
		- O existe un formulario para comunicarse con el nutricionista
		- O se realiza todo por teléfono

- **Como** nutricionista **quiero** gestionar clientes **para** dar de alta, dar de baja y modificar los datos de mis clientes 
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

- **Como** nutricionista **quiero** generar series de alimentos para 5 las comidas del cliente **para** optimizar su ingesta de calorías
	- Criterios:
		- Poder generar una lista de alimentos basada en:
			- grasas
			- proteínas 
			- hidratos de carbono

- **Como** nutricionista **quiero** gestionar los alimentos **para** crear, modificar las propiedades y eliminar alimentos.

- **Como** nutricionista **quiero** ver dietas anteriores del cliente, copiar y modificar dietas **para** no tener que crearlas desde cero

---

# Iteraciones

## Iteración 1

Implementar la página web base funcional que permita a los visitantes anónimos cumplir todas sus historias.

- Crear plantilla base de la página
- Implementar página de inicio
- Implementar página about me
- Implementar página contacto

## Iteración 2 (Revisable) 

Implementar login, sesiones y autenticación para diferenciar los roles.

- Implementar pagina de login (o modal)
- Implementar botón de logout
- Crear la base para una página "home" personalizada dependiendo del rol

## Iteración 3 (Revisable) 

Implementar la CRUD de las dietas y el seguimiento

- Implementar CRUD de dietas para el nutricionista (nutricionista)
- Implementar copia de dietas (nutricionista)
- Implementar consulta de dietas (cliente y nutricionista)
- Implementar seguimiento del cliente (cliente y nutricionista)
- Modificar la página "home" personalizada del rol con las nuevas funcionalidades
- Cargar los alimentos en la BBDD

## Iteración 4 (Revisable) 

Crear CRUD de los alimentos y de los usuarios (nutricionista)

- Implementar página de gestión de usuarios con posibilidad de CRUD
- Implementar página de gestión de alimentos con posibilidad de CRUD

## Iteración 5 (Revisable) 

A definir.

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
