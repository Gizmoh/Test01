import sqlalchemy
import classes
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///datos.db', echo =False)
engine.execute("select 1").scalar()
Session = sessionmaker(bind=engine)
session = Session()
X = True
classes.user.metadata.create_all(engine)
while (X == True):
	Z = raw_input("Inserte nombre: ")
	A = classes.user(Z)
	session.add(A)
	if Z == "":
		X = False
session.commit()
for row in session.query(classes.user).order_by(classes.user.id):
	print row.name
print(session.query(classes.user).count())