import db
from flask import Flask, render_template, request, redirect, url_for
from flask import Blueprint
from models.merchant import Merchant

import repositories.tag_repository as tag_repository
import repositories.merchant_repository as merchant_repository
import repositories.transaction_repository as transaction_repository

merchant_blueprint = Blueprint("merchant", __name__)

@merchant_blueprint.route("/merchants")
def merchant():
    merchants = merchant_repository.select_all()
    return render_template("merchants/index.html", merchants = merchants)

# @merchant_blueprint.route("/merchant/transactions")
# def transactions():
#     merchant = merchant_repository.select_all()
#     return render_template("merchant/transactions.html", merchant = merchant)

@merchant_blueprint.route("/merchant/new_merchant")
def new_merchant():
    merchants = merchant_repository.select_all()
    return render_template("merchants/new_merchant.html", merchants = merchants)

# @merchant_blueprint.route("/merchant/new_transaction")
# def new_transaction():
#     merchants = merchant_repository.select_all()
#     return render_template("merchant/new_transaction.html", merchants = merchants)

@merchant_blueprint.route("/merchant/new",  methods=['POST'])
def create_merchant():
    name = request.form['name']
    merchant = Merchant(name)
    merchant_repository.save(merchant)
    return redirect('/merchants')

@merchant_blueprint.route("/merchant/<id>/edit", methods=['GET'])
def edit_merchant(id):
    merchant = merchant_repository.select(id)
    return render_template('merchants/edit_merchant.html', merchant = merchant)

@merchant_blueprint.route("/merchant/<id>", methods=['POST'])
def update_method(id):
    name = request.form['name']
    merchant = Merchant(name, id)
    merchant_repository.update(merchant)
    return redirect('/merchants')

# @merchant_blueprint.route("/merchant/<id>/view", methods=['GET'])
# def view_merchant(id):
#     merchant = merchant_repository.select(id)
#     return render_template("merchant/view.html", merchant = merchant)

@merchant_blueprint.route("/merchant/<id>/delete", methods=['POST'])
def delete_merchant(id):
    merchant_repository.delete(id)
    return redirect('/merchants')
