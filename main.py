from bs4 import BeautifulSoup
import requests
import csv

# choisir les filtres
for page in range(1,9):
   brand = "AUDI"
   year_min = 2010
   year_max = 2019
   power_min = 350
   energy = ""


   url = """https://www.lacentrale.fr/listing?energies={energy}&makesModelsCommercialNames={brand}&powerDINMin={power_min}&yearMax={year_max}&yearMin={year_min}&options=&page={page}""".format(
   brand=brand,energy=energy, power_min=power_min, year_min=year_min, year_max=year_max, page=page)


   # Faire une demande GET à l'URL
   response = requests.get(url)

   # Créer un objet BeautifulSoup à partir de la réponse HTML
   soup = BeautifulSoup(response.text, 'html.parser')

   # Trouver tous les éléments searchCard
   searchCard_elements = soup.find_all(class_='searchCard')   

   # Liste pour stocker les données
   data = []

   for result in searchCard_elements:
      brand_and_model = result.find("h3").text
      brand, model = brand_and_model.split(maxsplit=1)
      year = result.find(class_="Text_Text_text Vehiculecard_Vehiculecard_characteristicsItems Text_Text_body2").text
      price = result.find(class_="Text_Text_text Vehiculecard_Vehiculecard_priceContainer Text_Text_body3").text
      motor = result.find(class_="Text_Text_text Vehiculecard_Vehiculecard_subTitle Text_Text_body2").text
      fuel = result.find_all(class_="Text_Text_text Vehiculecard_Vehiculecard_characteristicsItems Text_Text_body2", )[3].text
      mileage = result.find_all(class_="Text_Text_text Vehiculecard_Vehiculecard_characteristicsItems Text_Text_body2")[1]
      if result:
         print("Marque :", brand, "Modèle  :",model, "Année :", year,'\n', "Prix :", price, '\n', "Moteur :", motor, '\n' "Fuel :", fuel, '\n', "Mileage :", mileage.text,)
         data.append([brand, model, year, price, motor, fuel, mileage.text])

   # Écrire les données dans un fichier CSV
   with open("audi.csv", "a", newline="") as fd:
      writer = csv.writer(fd)
      writer.writerow(["Marque", "Modèle", "Année", "Prix", "Moteur", "Fuel", "Mileage"]) # Écrire les en-têtes
      for row in data:
         writer.writerow(row)
         