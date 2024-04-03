from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
import datetime
import requests

class ActionAskTime(Action):
    def name(self) -> Text:
        return "action_ask_time"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        current_time = datetime.datetime.now().strftime("%H:%M")
        dispatcher.utter_message(text=f"Il est actuellement {current_time}.")
        return []

class ActionAskWeather(Action):
    def name(self) -> Text:
        return "action_ask_weather"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        response = requests.get('http://api.openweathermap.org/data/2.5/weather?q=Oujda,MA&appid=a7d492dd77b9e1c1b596f591a3067fb6')
        weather = response.json()['weather'][0]['description']
        dispatcher.utter_message(text=f"Le temps est actuellement {weather}.")
        return []

class ActionAskDate(Action):
    def name(self) -> Text:
        return "action_ask_date"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        current_date = datetime.datetime.now().strftime("%d/%m/%Y")
        dispatcher.utter_message(text=f"Nous sommes le {current_date}.")
        return []

class ActionProvideName(Action):
    def name(self) -> Text:
        return "action_provide_name"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        bot_name = "L7ajBot"
        dispatcher.utter_message(text=f"Mon nom est {bot_name}.")
        return []
class ActionSayPhone(Action):
    def name(self) -> Text:
        return "action_say_phone"
    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        phone = tracker.get_slot("phone")
        if not phone:
            dispatcher.utter_message(text=f"Pardon! je ne sais pas votre num de téléphone.")
        else:
            dispatcher.utter_message(text=f"votre num de téléphone est {phone} !")
        return []
class ActionSayName(Action):
    def name(self) -> Text:
        return "action_say_name"
    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        name = tracker.get_slot("name")
        if not name:
            dispatcher.utter_message(text=f"Pardon! je ne sais pas votre nom.")
        else:
            dispatcher.utter_message(text=f"votre nom est {name} !")
        return []
