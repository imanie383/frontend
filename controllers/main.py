u"""controlador principañ."""

# libreria odoo web
from odoo import http


# tiene que se en camel case
class Academy(http.Controller):
    """metodo que nos va a servir los datos dentro de una url.

    #EN DADO CASO QUE 2 FUNCIONES TENGAN LA MISMA RUTA EJECUTA
    SOLO LA PRIMERA EN ORDEN ALFABETICO
    """

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

    # website indica que el controlador es parte del modulo website
    # si no lo pones no podras usar las plantillas del lyout
    @http.route('/academy/teacher', auth='public', website=True)
    def teacher(self, **kw):
        """Para la funcion render mandamos el xmlID.

        nombre de la app=carpeta + id del template.
        Atributos Qweb
        """
        teachers = http.request.env['academy.teacher']
        return http.request.render(
            'academy.teacher',
            {'teachers': teachers.search([])}
        )

    # RUTAS DINAMICA
    @http.route('/a#cademy/<name>', auth='public', website=True)
    def ruta_dinamica(self, name):
        """Uso de rutas dinamicas."""
        return '<h1>{}</h1>'.format(name)
        # no usar format en injecion de cadenas

    # RUTAS DINAMICAS CON VALIDACION DE TIPO
    # ayuda: https://werkzeug.palletsprojects.com/en/1.0.x/routing/
    @http.route('/academy/<int:id>', auth='public', website=True)
    def int_teacher(self, id):
        """USO DE RUTAS DINAMICAS CON VALIDACION DE TIPO.

        __name__ = obtiene el nombre de cualquier clase en python
        type(id) = regresa el tipo de objeto = regresa un objeto
        type(id).__name__ = regresa el nombre tipo de objeto (str)
        """
        return '<h1>{} ({})</h1>'.format(id, type(id).__name__)
        # no usar format en injecion de cadenas

    # CONVERTIDOR DE MODELOS
    # ligas /academy/fernando-padilla-1
    # /academy/1 y te redirecciona al de arriba
    @http.route('/academy/<model("academy.teacher"):teacher>',
                auth='public', website=True)
    def model_teacher(self, teacher):
        """Convertidor de modelos.

        model('MODELO'):VARIABLE
        """
        return http.request.render('academy.biography', {'person': teacher})

    # RPC A UN CONTROLADOR
    # Por defecto el type = http
    @http.route('/academy/search_teacher', type='json',
                auth='public', website=True)
    def search_teacher(self, **kw):
        """Para la funcion render mandamos el xmlID.

        nombre de la app=carpeta + id del template.
        Atributos Qweb
        """
        teacher_obj = http.request.env['academy.teacher']
        teachers = teacher_obj.search_read(
            [('id', '=', kw.get('teacher_id'))],
            fields=['biography'],
        )
        # print(teachers)
        return teachers
