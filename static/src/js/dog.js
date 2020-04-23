/*Heredando la clase animal*/
odoo.define('academy.dog', function(require) {
	'use strict';

	var Animal = require('academy.animal');

	var Dog = Animal.extend({
		move: function () {
			this.bark();
			/*
			this._super() = para llamar al método original
			aplply, ejecuta la funcion en el this
			arguments es una variable local a la función

			*/
			/*Pasa los argumentos a la clase padre*/ 
			this._super.apply(this, arguments);
		},
		bark: function () {
			console.log('Woof');
		},

	});

	var dog = new Dog();
	dog.move();

	/* Si en return marca error rejected  de load module*/
	return Dog;

}); 