import bs4 as bs
import sys
import urllib.request
from PyQt5.QtWebEngineWidgets import QWebEnginePage
from PyQt5.QtWidgets import QApplication
from PyQt5.QtCore import QUrl

from datetime import datetime, timedelta

# Class to handle downloading of webpage with javascript content
class Page(QWebEnginePage):
    def __init__(self, url):
        self.app = QApplication(sys.argv)
        QWebEnginePage.__init__(self)
        self.html = ''
        self.loadFinished.connect(self._on_load_finished)
        self.load(QUrl(url))
        self.app.exec_()

    def _on_load_finished(self):
        # set the html attribute which will later be used by BS parsing
        self.html = self.toHtml(self.Callable)

    def Callable(self, html_str):
        self.html = html_str
        self.app.quit()


checkInDate = (datetime.now() + timedelta(days=30)).strftime("%m%d%y")
checkoutDate = (datetime.now() + timedelta(days=32)).strftime("%m%d%y")
hotelName = 'The Chancery Pavilion'
print(checkInDate, checkoutDate)

def main():
    page = Page('https://www.makemytrip.com/mmthtl/site/hotels/detail?checkin=06102018&checkout=06242018&roomStayQualifier=2e0e&city=BLR&area=&areaId=undefined&searchText=The%20Chancery%20Pavilion,%20Bangalore&country=IN&hotelId=200701121638544369')
    soup = bs.BeautifulSoup(page.html, 'html5lib')
    print(soup)
    # js_test = soup.find('p', class_='mboxDefault')
    # print (js_test.text)

if __name__ == '__main__':
    main()