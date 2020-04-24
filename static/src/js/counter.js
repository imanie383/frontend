/* Nuevo widget */
odoo.define('odoo.counter',function (require){
	'use strict';

	/*Requerimos un widget = que es el constructor de todos los elemntos vizuales*/
	var Widget = require('web.Widget'); 
	/*Requerir el core*/
	var core = require('web.core'); 
	/*Modulo asyncrono = document.ready()*/
	require('web.dom_ready');

	/*
	Para ser un Widget debde de tener:
		init:
		start:
	*/
	var Counter = Widget.extend({
		/*Que eventos va a escuchar*/
		events:{
			// Envento - Elemento : Metodo a ejecutar
			'click' : '_onClick',
			/*
			'click'
			'click .clase1'
			*/ 
		},
		/*Parent = elemento que lo contiene*/
		init: function(parent, value){
			//cuando sobrescrives el init de un widget deves mandar _super(parent)
			this._super(parent);
			this.count = value;

		},
		_onClick: function(){
			this.count++;
			this.$('.value').text(this.count);
		},
		start: function(){
			return this._super.apply(this, arguments);
		},

	});

	/* Hacemos el binding con el objeto*/
	var counter_list = [];
	$('.counter').each(function (idx){
		var counter = new Counter(this, 1);
		counter.setElement($(this)).start();
		counter_list.push(counter);
	});

});