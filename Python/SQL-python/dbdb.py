from sqlalchemy import Column, ForeignKey, Integer, String, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker


Base = declarative_base()

class Info(Base):
	__tablename__ = "Info"

	id = Column(Integer, primary_key=True)
	user_info = Column(String(255))
	machine_info = Column(String(255))
	loc = Column(String(255))

	def __repr__(self):
		return "<Info(ID='%d', User='%s', machine_info='%s', location='%s')>" % (
				self.id, self.user_info, self.machine_info, self.loc)

engine = create_engine('sqlite:///info.db')
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
#Session.configure(bind=engine)
session = Session()

session.add_all([
				Info(id=0, user_info="mirkanos", machine_info="linux", loc="izmir"),
				Info(id=1, user_info="siskos", machine_info="PC", loc="sikoland")
				])

# first = Info(id=0, user_info="mirkanos", machine_info="linux", loc="izmir")
# second = Info(id=1, user_info="siskos", machine_info="PC", loc="sikoland")
# session.add(first)
# session.add(second)

# session.commit()

# our_user = session.query(Info).filter_by(user_info='mirkanos').first() 
# print(our_user)

print(Session().query(Info).all())
# print(Session().query(Info).filter_by())