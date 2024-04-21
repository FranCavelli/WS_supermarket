
from bs4 import BeautifulSoup
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import TimeoutException
import time

archivo_txt = 'la_anonima/frutasVerduras.txt'

with open(archivo_txt, 'w'):
    pass

LA_frutasVerduras = []

website = "https://supermercado.laanonimaonline.com/frutas-y-verduras/n1_7/"

driver = webdriver.Chrome(r"C:\Users\Francisco\Desktop\scrap\chromedriver.exe")

driver.get(website)

time.sleep(2)
select1 = Select(driver.find_element(By.ID, "sel_provincia"))
select1.select_by_value("1")
time.sleep(2)

select2 = Select(driver.find_element(By.ID, "sel_localidad_1"))
select2.select_by_value("26")

time.sleep(2)
select3 = Select(driver.find_element(By.ID, "sel_sucursal_26"))
select3.select_by_value("88")

boton = driver.find_element(By.CLASS_NAME, "btn-confirmar")
boton.click()

time.sleep(5)

haypaginas = 'true'
pagina_actual = 1
def extraerFrutasVerduras():
    global haypaginas
    global pagina_actual
    while haypaginas == 'true':
        try:
            print("Buscar frutas y verduras")
            content = driver.page_source

            soup = BeautifulSoup(content, 'html.parser')
            
            divs_productos = soup.find_all('div', id=lambda element_id: element_id and element_id.startswith('prod_'))

            print("Pagina "+str(pagina_actual))
            
            for div_producto in divs_productos:

                segundaColumna = div_producto.find('div', class_='col2_listado')
                precio_complemento  = segundaColumna.find('div', class_='precio_complemento aux1')
                precio_final  = precio_complemento.find('div', class_='precio semibold aux1').text.strip()

                imagen = div_producto.find('img')

                if imagen:
                    src_imagen = imagen.get('data-src')
                    nombrE_producto = imagen.get('title')

                bebida_actual = {}
                
                bebida_actual['id'] = div_producto['id']
                bebida_actual['nombre'] = str(nombrE_producto)
                bebida_actual['precio'] = str(precio_final)
                bebida_actual['imagen'] = str(src_imagen)
                
                LA_frutasVerduras.append(bebida_actual)

                with open(archivo_txt, 'a') as archivo:
                    archivo.write(str(LA_frutasVerduras))

            time.sleep(5)
            
            try:
                elemento_pag_siguiente = WebDriverWait(driver, 10).until(
                    EC.visibility_of_element_located((By.CSS_SELECTOR, 'a span.icono.pag_siguiente'))
                )

                if elemento_pag_siguiente.is_displayed():
                    pagina_actual += 1
                    print("Pasando a la pagina "+str(pagina_actual))
                    elemento_pag_siguiente.click()
                else:
                    haypaginas = 'false'
                    print("No hay más páginas")
                    return 
                
            except TimeoutException:
                haypaginas = 'false'
                print("No hay más páginas")
                return 

        except Exception as e:
            print(f"Error: {e}")

extraerFrutasVerduras()

driver.quit()