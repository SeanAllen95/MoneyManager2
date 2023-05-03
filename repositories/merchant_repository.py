from db.run_sql import run_sql
import psycopg2

from models.tag import Tag
from models.transaction import Transaction
from models.merchant import Merchant

def save(merchant):
    sql = "INSERT INTO merchants (name) VALUES (%s) RETURNING id"
    values = [merchant.name,]
    results = run_sql(sql, values)
    merchant.id = results[0]['id']
    return merchant

def select_all():
    merchants = []
    sql = "SELECT * FROM merchants"
    results = run_sql(sql)
    for row in results:
        merchant = Merchant(row['name'], row['id'])
        merchants.append(merchant)
    
    return merchants

# def select(id):
#     merchant = None
#     sql = "SELECT * FROM merchants WHERE id = %s"
#     values = [id]
#     result = run_sql(sql, values)[0]

#     if result is not None:
#         merchant = Merchant(result['name'], result['category'], result['amount'], result['id'])
#     return merchant

def delete_all():
    sql = "DELETE FROM merchants"
    run_sql(sql)

# def delete(id):
#     sql = "DELETE FROM merchants WHERE id = %s"
#     values = [id]
#     run_sql(sql, values)

# def update(merchant):
#     sql = "UPDATE merchants SET (name, category, amount) = (%s, %s, %s) WHERE id = %s"
#     values = [merchant.name, merchant.category, merchant.amount, merchant.id]
#     run_sql(sql, values)
