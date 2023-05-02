from db.run_sql import run_sql
from models.brewery import Brewery
import repos.beer_repo as beer_repo
import repos.brewery_repo as brew_repo
import repos.keg_repo as keg_repo

def delete_all():
    sql = "DELETE FROM breweries"
    run_sql(sql)

def delete(id):
    sql="DELETE FROM breweries WHERE id = %s"
    values = [id]
    run_sql(sql,values)

def save(brewery):
    sql = "INSERT INTO breweries (name) VALUES (%s) RETURNING id"
    values = [brewery.name]
    result = run_sql(sql,values)
    brewery.id = result[0]['id']
    return brewery

def select(id):
    sql = "SELECT * FROM breweries WHERE id = %s"
    values = [id]
    results = run_sql(sql,values)
    if results:
        row = results[0]
        brewery = Brewery(row['name'], row['id'])
    return brewery

def select_all():
    breweries = []
    sql = "SELECT * FROM breweries"
    results = run_sql(sql)
    for row in results:
        brewery = Brewery(row['name'],row['id'])
        breweries.append(brewery)
    return breweries

def update(brewery):
    sql = "UPDATE breweries SET name = %s WHERE id = %s"
    values= [brewery.name ,brewery.id]
    run_sql(sql, values)