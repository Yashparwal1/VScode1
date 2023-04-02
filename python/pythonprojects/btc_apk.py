
"""
import requests
from kivy.app import App
from kivy.core.audio import SoundLoader
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout


class BitcoinPriceAlert(App):
    def build(self):
        layout = GridLayout(cols=2)
        layout.add_widget(Label(text='Bitcoin Price Alert:'))
        self.price_label = Label(text='Fetching...')
        layout.add_widget(self.price_label)
        self.alert_button = Button(text='Set Alert')
        self.alert_button.bind(on_press=self.set_alert)
        layout.add_widget(self.alert_button)
        return layout

    def fetch_price(self):
        url = 'https://api.coinmarketcap.com/v1/ticker/bitcoin/'
        response = requests.get(url)
        data = response.json()
        price_usd = float(data[0]['price_usd'])
        return price_usd

    def set_alert(self, instance):
        price = self.fetch_price()
        if price >= 50000:
            sound = SoundLoader.load('alert.mp3')
            sound.play()
        self.price_label.text = f'${price:,.2f}'

if __name__ == '__main__':
    BitcoinPriceAlert().run()

-------------------------

buildozer init

----------------------------
Edit the buildozer.spec file and add the following lines to specify the dependencies:

requirements = python3,kivy,requests
android.permissions = INTERNET
android.permissions = WRITE_EXTERNAL_STORAGE

-------------------------
build apk

buildozer android debug

This will create a new APK file in the bin directory with the name BitcoinPriceAlert-0.1-debug.apk.
"""