/*Mixin - Heredando 2 clases*/
odoo.define('academy.hamster', function(require) {
	'use strict';

	/*Instanciamos animal*/
	var Animal = require('academy.animal');

	/*Creamos una nueva clase*/
	var DanceMixin = {
		dance: function(){
			console.log('Dancing');
		},

	};

	/* Hacemos el mixin */
	var Hamster = Animal.extend(DanceMixin,{
		sleep: function(){
			console.log('sleeping');
		} 

	});

	var hamster = new Hamster();
	hamster.dance();
	hamster.sleep();

	/* Si en return marca error rejected  de load module*/
	return Hamster;

}); 