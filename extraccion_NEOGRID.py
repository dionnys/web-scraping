#IMPORTAR LIBRERIAS
from selenium import webdriver
import time
import pandas as pd
from datetime import date, timedelta
from selenium.webdriver.common.action_chains import ActionChains


url = 'https://id.neogrid.com/identity/login'
usuario = 'bidavila@scj.com'
password = 'Neogrid@678'
#INDICAR LA RUTA DONDE ESTA INSTALADO EL WEBDRIVER
driver_path = "C:/webdrivers_scraping/Chrome Driver/"  
#INDICAR LA RUTA DONDE SE DESCARGARAN LOS ARCHIVOS
download_path="C:\Extraccion_neogrid_scj_br\Descarga_b2b_scj_br"


def extraer_datos():

	#0. EJECUCION DE WEBDRIVER Y SELECCION DE DIRECTORIO DE DESCARGA.
	options = webdriver.ChromeOptions()
	options.add_argument("--start-maximized")
	prefs = {"profile.default_content_settings.popups": 0,
				 "download.default_directory": 
				  download_path+"\\",
				 "directory_upgrade": True}
	options.add_experimental_option("prefs", prefs)
	browser=webdriver.Chrome(driver_path+'chromedriver.exe', options=options)
	browser.implicitly_wait(2000)
	
	#1. INGRESO EN LA PAGINA
	browser.get(url) 
	time.sleep(2)

	#try:
	#browser.refresh()

	browser.delete_all_cookies()
	
	
    #1. LOGIN EN LA PAGINA
	 
	#boton_cookies = browser.find_element_by_id('CybotCookiebotDialogBodyLevelButtonAccept')
	
	#print("Opción cookies encontrado acciÓn OK", '\n')

	#boton_cookies.click()

	time.sleep(1)
	
	tx_usuario = browser.find_element_by_id('email').send_keys(usuario)
	tx_password = browser.find_element_by_id('password').send_keys(password)
	boton_ingresar = browser.find_element_by_class_name('button-primary').click()
	

	#2. CERRAR BANNER Y ENTRAR
	time.sleep(2)

	boton_ingresar = browser.find_element_by_xpath('/html/body/div[4]/table/tbody/tr/td[2]/div[2]/div[3]/table/tbody/tr/td[1]/div/table/tbody/tr/td[2]').click()

	#3. ACCEDER A RETAIL INSIGHTS
	time.sleep(4)

	boton_retail_insights = browser.find_element_by_xpath('/html/body/div[2]/div[3]/div/div[2]/div/div/div[2]/div[3]/div/div/div/div/div[18]').click()

	time.sleep(4)
	boton_rita = browser.find_elements_by_class_name('mstrLargeIconViewItemLink')[0].click()

	#4. GENERAR DATOS STOCK (4) / VENTAS (6)
	time.sleep(2)

	#id_reporte = 6

	boton_stock = browser.find_elements_by_class_name('mstrLargeIconViewItemLink')[id_reporte].click()
	time.sleep(4)
	boton_run_dashboard1 = browser.find_element_by_xpath('/html/body/div[2]/table/tbody/tr/td[2]/div[2]/div[1]/div/div/table/tbody/tr[3]/td/input[1]').click()
	time.sleep(2)

	#dias = 2

	fecha = date.today() - timedelta(dias)
	fecha = fecha.strftime("%m/%d/%Y")
	print("SELECCIONAR FECHA: "+str(fecha))

	print("SELECCIONAR FECHA DESDE:"+str(fecha))
	fecha_desde = fecha


	selector_fecha_desde = browser.find_element_by_xpath('//*[@id="id_mstr60"]/div[2]/div/div/div[2]/div/a[4]')
	selector_fecha_desde.click()

	time.sleep(1)
	input_fecha_desde = browser.find_element_by_xpath('//*[@id="id_mstr74_txt"]')
	input_fecha_desde.clear()
	input_fecha_desde.send_keys(fecha_desde)

	boton_fecha_desde = browser.find_element_by_xpath('//*[@id="id_mstr77"]')
	boton_fecha_desde.click()

	print("SELECCIONAR FECHA HASTA:"+str(fecha))
	fecha_hasta = fecha


	selector_fecha_hasta = browser.find_element_by_xpath('//*[@id="id_mstr60"]/div[2]/div/div/div[2]/div/a[5]')
	selector_fecha_hasta.click()

	time.sleep(1)
	input_fecha_hasta = browser.find_element_by_xpath('//*[@id="id_mstr85_txt"]')
	input_fecha_hasta.clear()
	input_fecha_hasta.send_keys(fecha_hasta)

	boton_fecha_hasta = browser.find_element_by_xpath('//*[@id="id_mstr88"]')
	boton_fecha_hasta.click()

	print("GENERAR DATOS\n")
	boton_run_dashboard2 = browser.find_element_by_id('id_mstr63').click()

	#5. DESCARGAR DATOS

	print("ABRIR MENU POPUP Y PRESIONAR EXPORTAR\n")

	#EJECUTAR HOVER "MOSTRAR MENU" Y LUEGO CLICK "MOSTRAR MENU"
	boton_hover = browser.find_element_by_xpath('/html/body/div[1]/div[5]/div[4]/div/div/div/div[1]/div[3]/div/div/div/div[2]/div/div/div/div[2]/div/div[1]/div[1]/div[1]/div[5]')
	boton_click = browser.find_element_by_xpath('/html/body/div[1]/div[5]/div[4]/div/div/div/div[1]/div[3]/div/div/div/div[2]/div/div/div/div[2]/div/div[1]/div[1]/div[1]/div[5]')
	hover = ActionChains(browser).move_to_element(boton_hover).move_to_element(boton_click)
	hover.click().perform()

	time.sleep(2)
	

	#EJECUTAR HOVER "EXPORTAR" Y LUEGO CLICK "EXPORTAR"
	boton_hover = browser.find_element_by_xpath('/html/body/div[4]/div/div[1]/a[17]/div[3]')
	boton_click = browser.find_element_by_xpath('/html/body/div[4]/div/div[1]/a[17]/div[3]')
	hover = ActionChains(browser).move_to_element(boton_hover).move_to_element(boton_click)
	hover.click().perform()

	time.sleep(2)


	#EJECUTAR CLICK "EXCEL" (1) / "PDF" (2) / "CSV" (3)
	boton_exportar = browser.find_element_by_xpath('/html/body/div[5]/div/div[1]/a[1]').click()

	print("FIN PROCESO\n")
	time.sleep(20)
	browser.close()

#def ftp_transfer()

#for dias in range(108,292):
for dias in range(9,16):
	print("DIAS:", dias)
#4. GENERAR DATOS STOCK (4) / VENTAS (6)
	id_reporte = 4
	print("EXTRAER STOCK\n")
	extraer_datos()
	time.sleep(60)
	
	id_reporte = 6
	print("EXTRAER VENTAS\n")
	extraer_datos()
	time.sleep(60)
   