//Ejemplo de un RPC
odoo.define('academy.demo_rpc', function (require){
	'use strict';

	/*Requerir el core*/
	var core = require('web.core'),
		Widget = require('web.Widget'),
		rpc = require('web.rpc');

	//para que el modulo se carge hasta que el dom este listo
	require('web.dom_ready');

	var RpcButton = Widget.extend({
		events:{
			'click .rpc-Button': 'onClick',
			'click .rpc-Button-a': 'onClicka'
		},
		init: function(parent, options){
			//cuando sobrescrives el init de un widget deves mandar _super(parent)
			//this._super(parent); //cuando no lleva
			//cuando lleva argumentos uso apply
			this._super.apply(this, arguments);
			// _.extend(destination, *sources)   = copia source a destino y regresa destino 
			this.options = _.extend(options || {}, {}); 
		},
		onClick: function(ev){
			/*Manda a buscar todos los maestros*/
			console.log('Clicked');
			rpc.query({
				/*Trae el array de los maestros*/
				model: 'academy.teacher',
				//method: 'search', //regresa los ID
				method: 'search_read', //regresa el objeto
				args: [
					[], //domain vacio
					['id', 'name', 'biography'], //fields
				],
			}).then(function(data){
				if(data.length){
					console.log(data);
				}

			});
		},
		onClicka: function(){
			console.log('Clicked-a');
			rpc.query({
				/*Trae el array de los maestros*/
				model: 'academy.teacher',
				//method: 'search', //regresa los ID
				method: 'search_read', //regresa el objeto
				args: [
					// this.$el = Contiene el elemento jquery en el cual se hace el binding = todos los p
					[['id','=',this.$el.data('teacher-id')]], //domain vacio
					['biography'], //fields
				],
			}).then(function(data){
				if(data.length){
					console.log(data);
					$('.biography').html(data[0].biography);
				}

			});

		},
		ejemplo: function(){
			pc.query({
				/*Trae el array de los maestros*/
				model: 'academy.teacher',
				method: 'search', //regresa los ID
				args: [
					[['id','=','1']], //domain
				],
			});
		}

	});

	/*Rejected voluntario !0 = true */
	if(!$('.rpc-container').length){
		return $.Defferred().reject('Dom does not cotain rpc-container');
	}
	//bindea  el boton
	$('.rpc-container').each(function (idx){
		var elem = $(this);
		var button = new RpcButton(null, elem.data());
		button.attachTo(elem); 
	});

	//buindea los href
	$('.rpc-container-a').each(function (idx){
		var elem = $(this);
		var button = new RpcButton(null, elem.data());
		button.attachTo(elem); 
	});

	return RpcButton;

}); 