from mysqlconnection import connectToMySQL
class User:
    DB = "users_schema_rev"
    def __init__(self, data):
        self.id = data["id"]
        self.first_name = data["first_name"]
        self.last_name = data["last_name"]
        self.email = data["email"]
        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]

    @classmethod
    def get_all(cls):
        query = """
                    SELECT *
                    FROM users;
                """
        results = connectToMySQL(cls.DB).query_db(query)
        users = []
        for dict_row in results:
            users.append(cls(dict_row))
        return users