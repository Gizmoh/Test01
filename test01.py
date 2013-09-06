import sqlalchemy
import classes
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///datos.db', echo =False)
engine.execute("select 1").scalar()
Session = sessionmaker(bind=engine)
session = Session()
X = True
Z = ""
classes.user.metadata.create_all(engine)
classes.player.metadata.create_all(engine)
print("Creacion de personajes por usuario: ")
for row in session.query(classes.user).order_by(classes.user.id):
	print (row.name+": ")
	while (Z != ""):
		Z = raw_input("Ingrese nombre: ")
		if(Z != ""):
			Y = input("Ingrese nivel: ")
			A = classes.player(Z,row.id)
			A.level = Y
			session.add(A)
	Z = "0"
session.commit()
usuario = session.query(classes.user).filter_by(name="huehue").first()
print(usuario.name)