import sqlalchemy
import classes
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///datos.db', echo =False)
engine.execute("select 1").scalar()
Session = sessionmaker(bind=engine)
session = Session()
classes.user.metadata.create_all(engine)
for row in session.query(classes.user).order_by(classes.user.id):
	print row.name
print(session.query(classes.user).count())
session.add_all([
	classes.user("Omegadurr"),
	classes.user("XRebirth"),
	])
session.commit()