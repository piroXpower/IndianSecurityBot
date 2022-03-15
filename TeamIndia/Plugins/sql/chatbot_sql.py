import threading
from sqlalchemy import Column, String
from AliciaRobot.modules.sql import BASE, SESSION
class AliciaChats(BASE):
    __tablename__ = "alicia_chats"
    chat_id = Column(String(14), primary_key=True)

    def __init__(self, chat_id):
        self.chat_id = chat_id

AliciaChats.__table__.create(checkfirst=True)
INSERTION_LOCK = threading.RLock()


def is_alicia(chat_id):
    try:
        chat = SESSION.query(AliciaChats).get(str(chat_id))
        return bool(chat)
    finally:
        SESSION.close()

def set_alicia(chat_id):
    with INSERTION_LOCK:
        aliciachat = SESSION.query(AliciaChats).get(str(chat_id))
        if not aliciachat:
            aliciachat = AliciaChats(str(chat_id))
        SESSION.add(aliciachat)
        SESSION.commit()

def rem_alicia(chat_id):
    with INSERTION_LOCK:
        aliciachat = SESSION.query(AliciaChats).get(str(chat_id))
        if aliciachat:
            SESSION.delete(aliciachat)
        SESSION.commit()


def get_all_alicia_chats():
    try:
        return SESSION.query(AliciaChats.chat_id).all()
    finally:
        SESSION.close()
