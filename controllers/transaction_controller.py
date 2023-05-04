import db
from flask import Flask, render_template, request, redirect, url_for
from flask import Blueprint
from models.transaction import Transaction

import repositories.tag_repository as tag_repository
import repositories.merchant_repository as merchant_repository
import repositories.transaction_repository as transaction_repository

transaction_blueprint = Blueprint("transaction", __name__)

@transaction_blueprint.route("/transactions")
def transaction():
    transactions = transaction_repository.select_all()
    tags = tag_repository.select_all()
    merchants = merchant_repository.select_all()
    transaction_total = transaction_repository.find_transaction_total()
    real_names = transaction_repository.get_real_names()
    return render_template("transactions/index.html", transactions = transactions, transaction_total = transaction_total, tags = tags, merchants = merchants, real_names = real_names)

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
    return render_template('/transactions/edit_transaction.html', transaction = transaction)

@transaction_blueprint.route("/transaction/<id>", methods=['POST'])
def update_method(id):
    amount = request.form['amount']
    merchant_id = request.form['merchant_id']
    tag_id = request.form['tag_id']
    transaction = Transaction(amount, merchant_id, tag_id, id)
    transaction_repository.update(transaction)
    return redirect('/transactions')

# @merchant_blueprint.route("/merchant/<id>/view", methods=['GET'])
# def view_merchant(id):
#     merchant = merchant_repository.select(id)
#     return render_template("merchant/view.html", merchant = merchant)

# @merchant_blueprint.route("/merchant/<id>/delete", methods=['POST'])
# def delete_merchant(id):
#     merchant_repository.delete(id)
#     return redirect('/merchant')
