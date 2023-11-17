from odoo import api, models, fields

class videojuego(models.Model):
    _name = "videojuegos.videojuego"
    _rec_name = "titulo"
    titulo = fields.Char()
    fecha_salida = fields.Date()
    clasificacion = fields.Char()
    publisher = fields.Char()
    genero = fields.Many2many(comodel_name="videojuegos.genero", string="Genero")
    copias = fields.One2many(comodel_name="videojuegos.copia", inverse_name="videojuego")

class genero(models.Model):
    _name ="videojuegos.genero"
    _rec_name = "genero"
    genero = fields.Char()

class copia(models.Model):
    _name = "videojuegos.copia"
    id = fields.Integer()
    videojuego = fields.Many2one(comodel_name="videojuegos.videojuego", string="Videojuego")
    precio_compra = fields.Float()
    precio_venta = fields.Float()
    margen_beneficio = fields.Float(compute="_calcular_margen", store=True, string="Porcentaje de beneficio")
    es_segunda_mano = fields.Boolean()

    @api.depends('precio_compra', 'precio_venta')
    def _calcular_margen(self):
        for record in self: #no preguntes va así
            if record.precio_compra <= 0 or record.precio_venta <= 0:
                record.margen_beneficio = 0
            else:
                record.margen_beneficio = (record.precio_venta - record.precio_compra) / record.precio_compra * 100

