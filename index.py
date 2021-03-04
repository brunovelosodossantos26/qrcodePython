import pyqrcode

link = 'https://ieeexplore-ieee-org.ez3.periodicos.capes.gov.br/Xplore/home.jsp'
pyqrcode.create(link).svg('qrcode.svg', scale=10)