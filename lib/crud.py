from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from lib.db.models import Base, User, Quest

engine = create_engine("sqlite:///quest.db")
Session = sessionmaker(bind=engine)

def create_user(name, email=None, preferences=None):
    with Session() as session:
        user = User(name=name, email=email, preferences=preferences)
        session.add(user)
        session.commit()
        return user.id
    
def delete_user(user_id):
    with Session() as session:
        user = session.quesry(User).get(user_id)
        if not user:
            raise ValueError(f"Did not delete. Reason: User {user_id} not found")
        session.delete(user)
        session.commit()

def get_all_users():
    with Session() as session:
        return session.query(User).all()
    
def find_user_by_id(user_id):
    with Session() as session:
        user = session.query(User).get(user_id)
        if not user:
            raise ValueError(f"User {user_id} not found")
        return user
    
