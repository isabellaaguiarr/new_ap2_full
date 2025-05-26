class EscolaRouter:
    """
    Um router para direcionar operações do app 'escola' para o banco de dados 'config_escola'.
    """

    app_label_escola = 'administracao'

    def db_for_read(self, model, **hints):
        if model._meta.app_label == self.app_label_escola:
            return 'config_escola'
        return None

    def db_for_write(self, model, **hints):
        if model._meta.app_label == self.app_label_escola:
            return 'config_escola'
        return None

    def allow_relation(self, obj1, obj2, **hints):
        if (
            obj1._meta.app_label == self.app_label_escola or
            obj2._meta.app_label == self.app_label_escola
        ):
            return True
        return None

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        if app_label == self.app_label_escola:
            return db == 'config_escola'
        return db == 'default'


