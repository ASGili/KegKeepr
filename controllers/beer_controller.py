import repos.beer_repo as beer_repo
import repos.brewery_repo as brew_repo
import repos.keg_repo as keg_repo
from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.beer import Beer

beer_blueprint = Blueprint("beer", __name__)

@beer_blueprint.route("/beer/")
def edit_master():
    breweries = brew_repo.select_all()
    beers = beer_repo.select_all()
    return render_template("beer/edit.jinja",beers=beers,breweries=breweries, chosen_beer= None)

@beer_blueprint.route("/beer/", methods=["POST"])
def redirect_to_edit():
    beer_id = request.form["beer"]
    return redirect("/beer/" + beer_id + "/edit/")

@beer_blueprint.route("/beer/<id>/edit/")
def edit_page(id):
    breweries = brew_repo.select_all()
    beers = beer_repo.select_all()
    beer = beer_repo.select(id)
    return render_template("/beer/edit.jinja",beers=beers,chosen_beer=beer,breweries=breweries)

@beer_blueprint.route("/beer/new/", methods=["POST"])
def create_or_update():
    if not request.form["beer_id"]:
        beer_name = request.form["name"]  
        abv = request.form["abv"]
        brewery = brew_repo.select(request.form["brewery_id"])
        beer = Beer(beer_name,abv,brewery)
        beer_repo.save(beer)
    else:
        beer = beer_repo.select(request.form["beer_id"])
        print(beer)
        beer.name = request.form["name"]
        beer.abv = request.form["abv"]
        beer.brewery = brew_repo.select(request.form["brewery_id"])
        beer_repo.update(beer)
    return redirect("/beer/")

@beer_blueprint.route("/beer/", methods=["POST"])
def redirect_to_delete():
    beer_id = request.form["beer"]
    return redirect("/beer/" + beer_id + "/delete/")

@beer_blueprint.route("/beer/<id>/delete/", methods=["POST"])
def delete(id):
    beer_repo.delete(id)  
    return redirect("/beer/")