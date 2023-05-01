from db.run_sql import run_sql
from models.brewery import Brewery

def delete_all():
    sql = "DELETE FROM breweries"
    run_sql(sql)

def save(brewery):
    sql = "INSERT INTO breweries (name) VALUES %s RETURNING id"
    values = [brewery.name]
    result = run_sql(sql,values)