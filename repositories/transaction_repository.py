from db.run_sql import run_sql
import psycopg2

from models.tag import Tag
from models.transaction import Transaction
from models.merchant import Merchant

def save(transaction):
    sql = "INSERT INTO transactions (amount, merchant_id, tag_id) VALUES (%s, %s, %s) RETURNING id"
    values = [transaction.amount, transaction.merchant_id.id, transaction.tag_id.id]
    results = run_sql(sql, values)
    transaction.id = results[0]['id']
    return transaction

def select_all():
    transactions = []
    sql = "SELECT * FROM transactions"
    results = run_sql(sql)
    for row in results:
        transaction = Transaction(row['amount'], row['merchant_id'], row['tag_id'], row['id'])
        transactions.append(transactions)
    
    return transactions

# def select(id):
#     merchant = None
#     sql = "SELECT * FROM merchants WHERE id = %s"
#     values = [id]
#     result = run_sql(sql, values)[0]

#     if result is not None:
#         merchant = Merchant(result['name'], result['category'], result['amount'], result['id'])
#     return merchant

def delete_all():
    sql = "DELETE FROM transactions"
    run_sql(sql)

# def delete(id):
#     sql = "DELETE FROM merchants WHERE id = %s"
#     values = [id]
#     run_sql(sql, values)

# def update(merchant):
#     sql = "UPDATE merchants SET (name, category, amount) = (%s, %s, %s) WHERE id = %s"
#     values = [merchant.name, merchant.category, merchant.amount, merchant.id]
#     run_sql(sql, values)
