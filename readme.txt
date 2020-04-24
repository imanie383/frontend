Javascript de odoo esta partido en 3 partes
1.-Cliente web: parte privada(back) aplicación single page
Es una instancia de una de WebClinet, y el se encarga de tidas las opciones

2.-Website - parte publica, tienda , cliente el blog, el help desk y las static's

3.-EL punto de venta

El sistema de modulos esta inspirado en AMD.js refine - require

El modulo es un Codigo que se va a ejecutar tan rápido como se pueda - ya que cumpla las dependencias

No soporta nombres de modelos iguales
No soporta dependencias circulares

Un modulo = un archivo

Para definir un modulo necesitamos 3 argumentos principales

1.- Nombre del modulo = unico

	NombreModulo.Quehace = web.widget

2.- Dependencia puede o no ser una lista de otros modelos

3.- Una funcion que regrese un valor de clase


ERRORES COMUNES

Missin dependencies: te faltan dependencias o tienes type

Fail module: Error de javascript

Reject modules: el modulo se rechaza voluntariamente porque no se cumplen ciertas características 

Return defered de query.rejected

Non load modules

ASYNCHRONOS MODULES

Se cargan hasta que se realiza un opcional


MEJORES PRACTICAS

Declaras todas las dependencias al inicio del modulo orden alfabético

Declarar al final todos los valores exportados, no tratar de exportar muchas variables generar solo regresar la clase

Con web.dom_ready estas seguro que tu modulo se carga que que todo esta cargado/listo

No tratar de hacer mas de un modulo en un solo archivo


PRUEBAS

1.- UNITARIAS:
	Probar el metodo aislado
2.- PRUEBAS DE INTEGRACION
	Probar varios métodos simulando un escenario
3.- PRUEBAS END-TO-END
	Simular a un usuario haciendo cosas