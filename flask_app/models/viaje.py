
# TODAS LAS CLASES IMPORTAN MYSQLCONNECTION
from flask_app.config.mysqlconnection import connectToMySQL


class Viaje:

    # Metodo constructor
    def __init__(self, data):
        self.id = data.get('id')
        self.destino = data.get('destino')
        self.fecha_inicio = data.get('fecha_inicio')
        self.fecha_fin = data.get('fecha_fin')
        self.itinerario = data.get('itinerario')
        self.created_at = data.get('created_at')
        self.updated_at = data.get('updated_at')

    # Para guardar un registro
    @classmethod
    def save(cls, data):
        query = """
            INSERT INTO viajes
            (destino, fecha_inicio, fecha_fin, itinerario, created_at, updated_at)
            VALUES (%(destino)s, %(fecha_inicio)s, %(fecha_fin)s,
                    %(itinerario)s, NOW(), NOW());
        """
        return connectToMySQL('intento_2').query_db(query, data)

    # Metodo para ver todos los registros
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM viajes;"
        viajes_en_bd = connectToMySQL('intento_2').query_db(query)

        viajes = []

        if viajes_en_bd:
            for viaje in viajes_en_bd:
                viajes.append(cls(viaje))

        return viajes

    # Metodo para ver un registro
    @classmethod
    def get_one(cls, datos):
        query = "SELECT * FROM viajes WHERE id = %(id)s;"
        viajes_en_db = connectToMySQL('intento_2').query_db(query, datos)

        if not viajes_en_db:
            return None

        return cls(viajes_en_db[0])

    # Metodo para editar un registro
    @classmethod
    def update(cls, datos):
        query = """
            UPDATE viajes
            SET destino = %(destino)s,
                fecha_inicio = %(fecha_inicio)s,
                fecha_fin = %(fecha_fin)s,
                itinerario = %(itinerario)s,
                updated_at = NOW()
            WHERE id = %(id)s;
        """
        return connectToMySQL('intento_2').query_db(query, datos)

    # Metodo para eliminar un registro
    @classmethod
    def delete(cls, datos):
        query = "DELETE FROM viajes WHERE id = %(id)s;"
        return connectToMySQL('intento_2').query_db(query, datos)

    # Metodo para vincular un usuario con un viaje
    @classmethod
    def vincular_usuario(cls, datos):
        query = """
            INSERT INTO usuarios_has_viajes (usuario_id, viaje_id)
            VALUES (%(usuario_id)s, %(viaje_id)s);
        """
        return connectToMySQL('intento_2').query_db(query, datos)
