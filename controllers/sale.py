u"""controlador principal."""

# libreria odoo web
from odoo import http
# importamos la clase a heredar
from odoo.addons.website_sale.controllers.main import WebsiteSale


# tiene que se en camel case
class WebsiteSaleInherit(WebsiteSale):
    """HELP.

    la ruta puede quedar vacia pero el nombre de la funcion
    debe ser el mimo que el de la clase original y su definicion

    @http.route([
        '/shop',
        '/shop/page/<int:page>',
        '/shop/category/<model("product.public.category"):category>',
        '/shop/category/<model("product.public.category"):category>/page/<int:page>'
    ], type='http', auth="public", website=True)
    def shop(self, page=0, category=None, search='', ppg=False, **post):

    super(self, CLASE).atributo o metodo = python 2
    super() = phyton 3

    """

    @http.route()
    def shop(self, page=0, category=None, search='', ppg=False, **post):
        """HELP.

        No mandar el primer parametro self
        igualar las demas variables a su variable
        el ultimo parametro de deja igual

        dir(res) -- saber todo lo que tirnr
        res.qcontext = valor que nos interesa
        res.qcontext.keys()

        Codigo mas legible
        import pprint; pprint.pprint(res.qcontext);

        """
        # print("herencia de controllers")
        res = super(WebsiteSaleInherit, self).shop(
            page=page,
            category=category,
            search=search,
            ppg=ppg,
            **post
        )

        res.qcontext['search'] = "ipad"
        res.qcontext['categories'] = res.qcontext['categories'].sorted(
            key=lambda r: r.name
        )
        # import ipdb; ipdb.set_trace();
        return res
