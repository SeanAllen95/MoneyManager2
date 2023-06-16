import db
from flask import Flask, render_template, request, redirect, url_for
from flask import Blueprint
from models.merchant import Merchant
from models.tag import Tag

import repositories.tag_repository as tag_repository
import repositories.merchant_repository as merchant_repository
import repositories.transaction_repository as transaction_repository

tag_blueprint = Blueprint("tag", __name__)

@tag_blueprint.route("/tags")
def tag():
    tags = tag_repository.select_all()
    return render_template("/tags/index.html", tags = tags)

@tag_blueprint.route("/tag/new_tag")
def new_tag():
    tags = tag_repository.select_all()
    return render_template("/tags/new_tag.html", tags = tags)

@tag_blueprint.route("/tag",  methods=['POST'])
def create_tag():
    category = request.form['category']
    tag = Tag(category)
    tag_repository.save(tag)
    return redirect('/tags')

@tag_blueprint.route("/tag/<id>/edit", methods=['GET'])
def edit_tag(id):
    tag = tag_repository.select(id)
    return render_template('/tags/edit_tag.html', tag = tag)

@tag_blueprint.route("/tag/<id>", methods=['POST'])
def update_method(id):
    category = request.form['category']
    tag = Tag(category, id)
    tag_repository.update(tag)
    return redirect('/tags')

@tag_blueprint.route("/tag/<id>/delete", methods=['POST'])
def delete_tag(id):
    tag_repository.delete(id)
    return redirect('/tags')
