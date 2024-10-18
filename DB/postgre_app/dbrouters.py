# class MyRouter:
#     def allow_migrate(self, db, app_label, model_name=None, **hints):
#         if "target_db" in hints:
#             return db == hints["target_db"]
#         return True

    # def allow_migrate(self, db, app_label, model_name=None, **hints):
    #         """
    #         Make sure the auth and contenttypes apps only appear in the
    #         'auth_db' database.
    #         """
    #         if app_label in self.route_app_labels:
    #             return db == "postgres_db"
    #         return None