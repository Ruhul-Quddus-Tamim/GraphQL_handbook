from graphene import ObjectType, String, Int, Field, Schema
import psycopg2

# Database connection
conn = psycopg2.connect(
    dbname="your_db_name",
    user="your_username",
    password="your_password",
    host="localhost"
)

# GraphQL types
class Customer(ObjectType):
    id = Int()
    name = String()
    email = String()
    phone = String()

# Queries
class Query(ObjectType):
    customer = Field(Customer, id=Int(required=True))

    def resolve_customer(self, info, id):
        cursor = conn.cursor()
        cursor.execute("SELECT id, name, email, phone FROM customers WHERE id = %s", (id,))
        row = cursor.fetchone()
        if row:
            return Customer(id=row[0], name=row[1], email=row[2], phone=row[3])
        return None

# Schema
schema = Schema(query=Query)

from flask import Flask
from flask_graphql import GraphQLView

app = Flask(__name__)
app.add_url_rule(
    '/graphql',
    view_func=GraphQLView.as_view(
        'graphql',
        schema=schema,
        graphiql=True  # Enables the GraphQL UI for testing
    )
)

if __name__ == "__main__":
    app.run(debug=True)
