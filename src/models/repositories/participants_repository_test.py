import pytest
import uuid
from .participants_repository import ParticipantsRepository
from src.models.settings.db_connection_handler import db_connection_handler

db_connection_handler.connect()
trip_id = str(uuid.uuid4())

@pytest.mark.skip(reason='interacao como banco')
def test_registry_participant():
  conn = db_connection_handler.get_connection()
  participants_repository = ParticipantsRepository(conn)
  
  participant_infos = {
    "id": str(uuid.uuid4()),
    "trip_id": trip_id,
    "emails_to_invite_id": str(uuid.uuid4()),
    "name": "Rose"
  }
  participants_repository.registry_participant(participant_infos)

@pytest.mark.skip(reason='interacao como banco')
def test_find_participants_from_trip():
  conn = db_connection_handler.get_connection()
  participants_repository = ParticipantsRepository(conn)
  
  participants = participants_repository.find_participants_from_trip(trip_id)
  print()
  print(participants)

def test_update_participant_status():
  conn = db_connection_handler.get_connection()
  participants_repository = ParticipantsRepository(conn)
  
  participants_repository.update_participant_status(trip_id)
