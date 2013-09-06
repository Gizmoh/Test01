import sqlalchemy
import classes
from sqlalchemy import create_engine

engine = create_engine('sqlite:///:memory:', echo =True)
engine.execute("select 1").scalar()
derp = classes.user("Mordekaiser")
print (derp.name)