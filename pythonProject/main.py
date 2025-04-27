from PyQt6.QtWidgets import QApplication, QMainWindow, QListWidgetItem
from PyQt6.QtCore import QDate
from ui_event_tracker import Ui_MainWindow
import sys
import json
import os

DATA_FILE = "events.json"

class EventTracker(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.addButton.clicked.connect(self.add_event)
        self.events = []
        self.load_events()
        self.refresh_event_list()

    def add_event(self):
        name = self.ui.eventName.text().strip()
        event_date = self.ui.eventDate.date()

        if not name:
            return

        event = {
            "name": name,
            "date": event_date.toString("yyyy-MM-dd")
        }

        self.events.append(event)
        self.refresh_event_list()
        self.ui.eventName.clear()

    def refresh_event_list(self):
        self.ui.eventList.clear()
        today = QDate.currentDate()

        # Оставим только события, дата которых сегодня или позже
        self.events = [e for e in self.events if QDate.fromString(e["date"], "yyyy-MM-dd") >= today]

        for event in self.events:
            event_date = QDate.fromString(event["date"], "yyyy-MM-dd")
            days_left = today.daysTo(event_date)
            item_text = f"{event['name']} - {event['date']} ({days_left} дн.)"
            self.ui.eventList.addItem(QListWidgetItem(item_text))

    def closeEvent(self, event):
        self.save_events()
        event.accept()

    def save_events(self):
        with open(DATA_FILE, "w", encoding="utf-8") as f:
            json.dump(self.events, f, ensure_ascii=False, indent=2)

    def load_events(self):
        if os.path.exists(DATA_FILE):
            try:
                with open(DATA_FILE, "r", encoding="utf-8") as f:
                    content = f.read().strip()
                    if content:
                        self.events = json.loads(content)
                    else:
                        self.events = []
            except json.JSONDecodeError:
                print("Ошибка чтения JSON. Файл повреждён.")
                self.events = []
        else:
            self.events = []

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = EventTracker()
    window.show()
    sys.exit(app.exec())
