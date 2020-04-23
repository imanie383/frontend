/*
 la funcin anonima simepre lleva como parametro require 
 
*/
odoo.define('academy.animal', function (require){
	'use strict';

	// Comprobar que se cargo la libreria
	console.log('Libreria cargada')

	//la clase base de odoo se encuentra en web
	var Class = require('web.Class');

	var Animal = Class.extend({
		/* Inicializa la clase */
		init: function () {
			this.x = 0;
			this.hunger = 0; 

		},
		move: function () {
			this.x = this.x + 1;
			this.hunger = this.hunger + 1;
			console.log(this);
		},
		eat: function () {
			this.hunger = 0;
			console.log(this);
		}

	});

	var animal = new Animal();
	animal.move();
	animal.move();
	animal.eat();

}); 