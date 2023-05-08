import repos.keg_repo as keg_repo
import repos.brewery_repo as brew_repo
import repos.beer_repo as beer_repo
from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.keg import Keg

keg_blueprint = Blueprint("keg", __name__)

@keg_blueprint.route("/")
def home():
    return render_template("home.jinja")

@keg_blueprint.route("/keg/")
def edit():
    kegs = keg_repo.select_all()
    beers = beer_repo.select_all()
    return render_template("keg/edit.jinja",kegs=kegs,beers=beers,chosen_keg = None)

@keg_blueprint.route("/keg/all/")
def inventory():
    kegs = keg_repo.select_all()
    return render_template("keg/inventory.jinja",kegs=kegs)

@keg_blueprint.route("/keg/", methods=["POST"])
def redirect_to_edit():
    keg_id = request.form["keg"]
    return redirect("/keg/" + keg_id + "/edit/")

@keg_blueprint.route("/keg/<id>/edit/")
def edit_page(id):
    kegs = keg_repo.select_all()
    keg = keg_repo.select(id)
    beers = beer_repo.select_all()
    return render_template("/keg/edit.jinja",kegs=kegs,chosen_keg=keg,beers=beers)

@keg_blueprint.route("/keg/", methods=["POST"])
def redirect_to_delete():
    keg_id = request.form["keg"]
    return redirect("/keg/" + keg_id + "/delete/")

@keg_blueprint.route("/keg/<id>/delete/", methods=["POST"])
def delete(id):
    keg_repo.delete(id)  
    return redirect("/keg/")

@keg_blueprint.route("/keg/new/", methods=["POST"])
def create_or_update():
    if not request.form["keg_id"]:
        beer = beer_repo.select(request.form["beer_id"])
        fill_level = request.form["fill"]
        capacity = request.form["capacity"]
        cost = request.form["cost"]
        price =request.form["price"]
        keg= Keg(beer,fill_level,capacity,cost,price)
        keg_repo.save(keg)
    else:
        keg = keg_repo.select(request.form["keg_id"])
        keg.beer = beer_repo.select(request.form["beer_id"])
        keg.fill_level = request.form["fill"]
        keg.capacity = request.form["capacity"]
        keg.cost = request.form["cost"]
        keg.price =request.form["price"]
        keg_repo.update(keg)
    return redirect("/keg/")