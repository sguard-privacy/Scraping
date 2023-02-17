from bs4 import BeautifulSoup
import requests
import csv

# Fonction pour formatter l'URL de recherche en fonction des critères spécifiés.
def format_url(page):
    brand = "xcvxvcv"
    year_min = 2010
    year_max = 2019
    power_min = 350
    energy = ""
    
    # Formatage de l'URL
    url = """https://www.lacentrale.fr/listing?energies={energy}&makesModelsCommercialNames={brand}&powerDINMin={power_min}&yearMax={year_max}&yearMin={year_min}&options=&page={page}""".format(
    brand=brand, energy=energy, power_min=power_min, year_min=year_min, year_max=year_max, page=page)
    return url



# Fonction pour scraper la centrale, les informations sur les voitures et les stocker dans un fichier CSV
def main():

    data = []
    
    # SCRAPING de la page 1 à 9 de résultat de recherche pour extraire les informations sur les voitures

    for page in range(1, 10):
        url = format_url(page)

        response = requests.get(url)

        soup = BeautifulSoup(response.text, 'html.parser')

        scrap_Elements = soup.find_all(class_='searchCard')
        
        if not scrap_Elements:
            data.append([f'Page {page} : La marque recherché est introuvable', 'no_data', 'no_data', 'no_data', 'no_data', 'no_data', 'no_data'])
            print(f"{url} : la marque recherché est introuvable")

        # Extraire les informations de chaque voiture de la page.

        for scrap in scrap_Elements:
            brand_and_model = scrap.find("h3").text
            brand, model = brand_and_model.split(maxsplit=1)
            year = scrap.find(
                class_="Text_Text_text Vehiculecard_Vehiculecard_characteristicsItems Text_Text_body2").text
            price = scrap.find(
                class_="Text_Text_text Vehiculecard_Vehiculecard_priceContainer Text_Text_body3").text
            price_int = int(price.replace(" ", "").replace("€", "").replace("oudès", "").replace("/mois", ""))
            motor = scrap.find(
                class_="Text_Text_text Vehiculecard_Vehiculecard_subTitle Text_Text_body2").text
            fuel = scrap.find_all(
                class_="Text_Text_text Vehiculecard_Vehiculecard_characteristicsItems Text_Text_body2", )
            if len(fuel) > 3:
                    fuel = fuel[3].text
            else:
                    fuel = "Aucune info"
                    
            mileage = scrap.find_all(class_="Text_Text_text Vehiculecard_Vehiculecard_characteristicsItems Text_Text_body2")
            if len(mileage) > 1:
                mileage_int = mileage[1].get_text().replace(" ", "").replace("km", "").replace("\xa0", " ")


            if scrap:
                print("Marque :", brand, "Modèle  :", model, "Année :", year, '\n',
                      "Prix :", price_int, '\n', "Moteur :", motor, '\n' "Fuel :", fuel, '\n', "Mileage :", mileage_int,)

                data.append([brand, model, year, price_int, motor, fuel, mileage_int])   
                

    
    # Récolte des données récupérées dans un fichier CSV
    with open("audi.csv", "a", newline="") as fd:
        writer = csv.writer(fd)
        writer.writerow(
            ["Marque", "Modèle", "Année", "Prix", "Moteur", "Fuel", "Mileage"])
        for row in data:
            writer.writerow(row)

# bloc d'exécution conditionnelle (plus sécurisé)
if __name__ == "__main__":
    main()
    

