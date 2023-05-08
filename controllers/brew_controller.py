import repos.beer_repo as beer_repo
import repos.brewery_repo as brew_repo
import repos.keg_repo as keg_repo
from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.brewery import Brewery

brew_blueprint = Blueprint("brew", __name__)

@brew_blueprint.route("/brew/")
def edit_master():
    breweries = brew_repo.select_all()
    return render_template("brew/edit.jinja", breweries=breweries, chosen_brewery=None)

@brew_blueprint.route("/brew/", methods=["POST"])
def redirect_to_edit():
    brewery_id = request.form["brewery"]
    return redirect("/brew/" + brewery_id + "/edit/")

@brew_blueprint.route("/brew/<id>/edit/")
def edit_page(id):
    breweries = brew_repo.select_all()
    brewery = brew_repo.select(id)
    return render_template("/brew/edit.jinja",breweries=breweries,chosen_brewery=brewery)

@brew_blueprint.route("/brew/new/", methods=["POST"])
def create_or_update():
    if not request.form["brewery_id"]:
        brewery_name = request.form["name"]  
        brewery = Brewery(brewery_name)
        brew_repo.save(brewery)
    else:
        brewery = brew_repo.select(request.form["brewery_id"])
        print(brewery)
        brewery.name = request.form["name"]
        brew_repo.update(brewery)
    return redirect("/brew/")

@brew_blueprint.route("/brew/", methods=["POST"])
def redirect_to_delete():
    brewery_id = request.form["brewery"]
    return redirect("/brew/" + brewery_id + "/delete/")

@brew_blueprint.route("/brew/<id>/delete/", methods=["POST"])
def delete(id):
    brew_repo.delete(id)  
    return redirect("/brew/")