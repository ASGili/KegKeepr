import repos.beer_repo as beer_repo
import repos.brewery_repo as brew_repo
import repos.keg_repo as keg_repo
from flask import Flask, render_template, request, redirect
from flask import Blueprint

beer_blueprint = Blueprint("beer", __name__)

@beer_blueprint.route("/beer/")
def edit():
    return render_template("beer/edit.jinja")