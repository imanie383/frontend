u"""controlador principañ."""

# libreria odoo web
from odoo import http


# tiene que se en camel case
class Academy(http.Controller):
    """metodo que nos va a servir los datos dentro de una url."""

    @http.route('/academy/academy', auth='public')
    def index(self, **kw):
        """Hola."""
        return "hola"
