from db.run_sql import run_sql
from models.keg import Keg

def delete_all():
    sql = "DELETE FROM breweries"
    run_sql(sql)