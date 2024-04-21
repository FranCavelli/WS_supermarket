from bs4 import BeautifulSoup
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import TimeoutException
import time

from la_anonima.LA_carniceria import extraerCarniceria
from la_anonima.LA_frutasVerduras import extraerFrutasVerduras
from la_anonima.LA_congelados import extraerCongelados
from la_anonima.LA_bebidas import extraerBebidas
from la_anonima.LA_frescos import extraerFrescos
from la_anonima.LA_almacen import extraerAlmacen