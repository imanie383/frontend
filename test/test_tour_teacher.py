# -*- coding: utf-8 -*-
import odoo.test


# Para que no se corra cuando se instala
@odoo.tests.common.at_ install(False)
@odoo.tests.common.post_install(True)
class TestUiTeachers(odoo.test.HttpCase):
    def test_01_admin_teachers_tour(self):
        self.phantom_js(
            '/',
            'odoo.__DEBUG__.services["web_tour.tour"].run("tour_show_biographies")',
            'odoo.__DEBUG__.services["web_tour.tour"].tours.tour_show_biographies.ready',
            login='admin',
        )
