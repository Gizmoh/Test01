import sqlalchemy
import classes
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///datos.db', echo =True)
engine.execute("select 1").scalar()
Session = sessionmaker(bind=engine)
derp = classes.user("Mordekaiser")
print (derp.name)
session = Session()
session.add(derp)
session.commit()