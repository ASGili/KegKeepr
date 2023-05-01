from db.run_sql import run_sql
from models.brewery import Brewery
import repos.beer_repo as beer_repo
import repos.brewery_repo as brew_repo
import repos.keg_repo as keg_repo

def delete_all():
    sql = "DELETE FROM breweries"
    run_sql(sql)

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
        result = results[0]
        brewery = Brewery(result['name'],result['id'])
    return brewery

def select_all():
    breweries = []
    sql = "SELECT * FROM breweries"
    results = run_sql(sql)
    for row in results:
        brewery = Brewery(row['name'],row['id'])
        breweries.append(brewery)
    return breweries