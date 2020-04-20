u"""controlador principañ."""

# libreria odoo web
from odoo import http


# tiene que se en camel case
class Academy(http.Controller):
    """metodo que nos va a servir los datos dentro de una url."""

    @http.route('/academy/academy', auth='public')
    def index(self, **kw):
        """Para la funcion render mandamos el xmlID.

        nombre de la app=carpeta + id del template.
        uso basico de la libreria Qweb
        """
        return http.request.render(
            'academy.index',
            {'teachers': [
                'Diana padilla',
                'Jody Carrol',
                'Lester',
            ]}
        )

    @http.route('/academy/attributes', auth='public')
    def index2(self, **kw):
        """Para la funcion render mandamos el xmlID.

        nombre de la app=carpeta + id del template.
        Atributos Qweb
        """
        return http.request.render(
            'academy.attributes',
            {'teachers': [
                'a',
                'p',
                '<div>Elemento a</div>',
            ]}
        )
