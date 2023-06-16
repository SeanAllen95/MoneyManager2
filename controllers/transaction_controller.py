import db
from flask import Flask, render_template, request, redirect, url_for
from flask import Blueprint
from models.transaction import Transaction
from models.merchant import Merchant
from models.tag import Tag

import repositories.tag_repository as tag_repository
import repositories.merchant_repository as merchant_repository
import repositories.transaction_repository as transaction_repository

transaction_blueprint = Blueprint("transaction", __name__)

@transaction_blueprint.route("/transactions")
def transaction():
    transactions = transaction_repository.join_tables()
    all_transactions = transaction_repository.select_all()
    transaction_total = transaction_repository.find_transaction_total()
    # merchants = transaction_repository.join_merchants()
    # tags = transaction_repository.join_tags()
    return render_template("transactions/index.html", transactions = transactions, transaction_total = transaction_total, all_transactions = all_transactions)

# @merchant_blueprint.route("/merchant/transactions")
# def transactions():
#     merchant = merchant_repository.select_all()
#     return render_template("merchant/transactions.html", merchant = merchant)

# @merchant_blueprint.route("/merchant/new")
# def new_merchant():
#     merchants = merchant_repository.select_all()
#     return render_template("merchant/new_merchant.html", merchants = merchants)

@transaction_blueprint.route("/transaction/new_transaction")
def new_transaction():
    transactions = transaction_repository.select_all()
    tags = tag_repository.select_all()
    merchants = merchant_repository.select_all()
    return render_template("transactions/new_transaction.html", transactions = transactions, tags = tags, merchants = merchants)

@transaction_blueprint.route("/transaction",  methods=['POST'])
def create_transaction():
    amount = request.form['amount']
    merchant_id = request.form['merchant']
    tag_id = request.form['tag']
    transaction = Transaction(amount, merchant_id, tag_id, id)
    transaction_repository.save(transaction)
    return redirect('/transactions')

@transaction_blueprint.route("/transaction/<id>/edit", methods=['GET'])
def edit_transaction(id):
    transaction = transaction_repository.select(id)
    merchants = merchant_repository.select_all()
    tags = tag_repository.select_all()
    return render_template('/transactions/edit_transaction.html', transaction = transaction, merchants = merchants, tags = tags)

@transaction_blueprint.route("/transaction/<id>", methods=['POST'])
def update_method(id):
    amount = request.form['amount']
    name = request.form['merchant']
    category = request.form['tag']
    transaction = Transaction(amount, name, category, id)
    name = Merchant(name, id)
    category = Tag(category, id)
    transaction_repository.update(transaction)
    merchant_repository.update(name)
    tag_repository.update(category)
    return redirect('/transactions')

# @merchant_blueprint.route("/merchant/<id>/view", methods=['GET'])
# def view_merchant(id):
#     merchant = merchant_repository.select(id)
#     return render_template("merchant/view.html", merchant = merchant)

@transaction_blueprint.route("/transaction/<id>/delete", methods=['POST'])
def delete_transaction(id):
    transaction_repository.delete(id)
    return redirect('/transactions')
