import repos.beer_repo as beer_repo
import repos.brewery_repo as brew_repo
import repos.keg_repo as keg_repo
from flask import Flask, render_template, request, redirect
from flask import Blueprint

keg_blueprint = Blueprint("keg", __name__)

@keg_blueprint.route("/")
def home():
    return render_template("home.jinja")