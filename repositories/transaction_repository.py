from db.run_sql import run_sql
import psycopg2

from models.tag import Tag
from models.transaction import Transaction
from models.merchant import Merchant

# get help with this save function

def save(transaction):
    sql = "INSERT INTO transactions (amount, merchant_id, tag_id) VALUES (%s, %s, %s) RETURNING id"
    values = [transaction.amount, transaction.merchant_id, transaction.tag_id]
    results = run_sql(sql, values)
    transaction = results[0]['id']
    return transaction

def select_all():
    transactions = []
    sql = "SELECT * FROM transactions"
    results = run_sql(sql)
    for row in results:
        transaction = Transaction(row['amount'], row['merchant_id'], row['tag_id'], row['id'])
        transactions.append(transaction)
    
    return transactions

def select(id):
    transaction = None
    sql = "SELECT * FROM transactions WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]

    if result is not None:
        transaction = Transaction(result['amount'], result['merchant_id'], result['tag_id'], result['id'])
    return transaction

def delete_all():
    sql = "DELETE FROM transactions"
    run_sql(sql)

def delete(id):
    sql = "DELETE FROM transactions WHERE id = %s"
    values = [id]
    run_sql(sql, values)

def update(transaction):
    sql = "UPDATE transactions SET (amount, merchant_id, tag_id) = (%s, %s, %s) WHERE id = %s"
    values = [transaction.amount, transaction.merchant_id, transaction.tag_id, transaction.id]
    run_sql(sql, values)

def find_transaction_total():
    sql = "SELECT SUM(amount) FROM transactions"
    result = run_sql(sql)
    return result[0][0]

# def get_real_names():
#     sql = "SELECT transactions.amount, merchants.name, tags.category FROM transactions JOIN merchants ON transactions.merchant_id = merchants.id JOIN tags ON transactions.tag_id = tags.id"
#     real_names_result = run_sql(sql)
#     return real_names_result

# def join_merchants():
#     sql = "SELECT name FROM transactions INNER JOIN merchants ON transactions.merchant_id = merchants.id"
#     result = run_sql(sql)
#     print(result)

# def join_tags():
#     sql = "SELECT category FROM transactions INNER JOIN tags ON transactions.tag_id = tags.id"
#     result = run_sql(sql)
#     print(result)

def join_tables():
    sql = "SELECT transactions.amount, transactions.id, merchants.name, tags.category FROM transactions JOIN merchants ON transactions.merchant_id = merchants.id JOIN tags ON transactions.tag_id = tags.id"
    result = run_sql(sql)
    return result

