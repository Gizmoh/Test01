import sqlalchemy
import classes
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///datos.db', echo =False)
engine.execute("select 1").scalar()
Session = sessionmaker(bind=engine)
session = Session()
session.add_all([
	classes.user("derp"),
	classes.user("huehue"),
	classes.user("nerfPl0x")
	])
session.commit()