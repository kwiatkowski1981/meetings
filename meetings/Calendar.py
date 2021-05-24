from datetime import datetime, timedelta
from meetings.Meeting import Meeting


class Calendar:
    def __init__(self):
        self.meetings = {}

    def is_available(self, date: datetime):
        return date not in self.meetings

    def add_meeting(self, meeting: Meeting):
        if self.is_available(meeting.date):
            self.meetings[meeting.date] = meeting

    def next_available_slot(self, date: datetime):
        meeting_date = date
        while not self.is_available(meeting_date):
            meeting_date += timedelta(minutes=60)
        return meeting_date

# TODO 1- dodac funkcje w menu glownym sprawdzanie dostepnosci nastepnego wolnego terminu
# TODO 2- sprawdzenie czy konkretna godzina jest dostepna
# TODO metody sa juz napisane powyzej, tylko dodac opcje do menu glownego w klasie main.py
