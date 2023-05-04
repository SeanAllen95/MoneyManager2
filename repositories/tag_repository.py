from db.run_sql import run_sql
import psycopg2

from models.tag import Tag
from models.transaction import Transaction
from models.merchant import Merchant

def save(tag):
    sql = "INSERT INTO tags (category) VALUES (%s) RETURNING id"
    values = [tag.category]
    results = run_sql(sql, values)
    tag.id = results[0]['id']
    return tag

def select_all():
    tags = []
    sql = "SELECT * FROM tags"
    results = run_sql(sql)
    for row in results:
        tag = Tag(row['category'], row['id'])
        tags.append(tag)
    
    return tags

def select(id):
    tag = None
    sql = "SELECT * FROM tags WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]

    if result is not None:
        tag = Tag(result['category'], result['id'])
    return tag

def delete_all():
    sql = "DELETE FROM tags"
    run_sql(sql)

# def delete(id):
#     sql = "DELETE FROM merchants WHERE id = %s"
#     values = [id]
#     run_sql(sql, values)

def update(tag):
    sql = "UPDATE tags SET category = %s WHERE id = %s"
    values = [tag.category, tag.id]
    run_sql(sql, values)
