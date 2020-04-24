/*Scirpt Phantom*/
odoo.define('academy.academy_tour', function(require) {
	'use strict';

	var tour = require('web_tour.tour'),
		base = require('web_editor.base');

	// Nos crea un nuevo tour (Nombre, ConfDelTour )
	tour.register('tour_show_biographies',{
		test: true,
		url: '/academy/teacher',
		wait_for: base.ready()
	},
	//lista de pasos
	[
		{
			content: 'Click on firs teacher', //Texto que va a mostra el paso
			trigger: 'p[data-teacher-id="1"] a', //selector
			//run
		},
		{
			content: 'Click on second teacher', //Texto que va a mostra el paso
			trigger: 'p[data-teacher-id="2"] a', //selector
			extra_trigger: '.s_image_text', //que esperamos en el dom este renderizado
			//run
		}

	]);

}); 