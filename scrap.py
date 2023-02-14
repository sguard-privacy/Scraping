from bs4 import BeautifulSoup
import requests
import mechanize
import csv

brand = "AUDI"
year_min = 2010
year_max = 2019
power_min = 350
energy = "ess"

# Créer un navigateur
browser = mechanize.Browser()

# browser.set_handle_redirect(True)

# browser.set_cookiejar(requests.cookies.RequestsCookieJar())

browser.set_handle_robots(False)

def get_annonce_data(brand, year_min, year_max, power_min, energy):
    url = "https://www.lacentrale.fr/listing?energies={energy}&makesModelsCommercialNames={brand}&powerDINMin={power_min}&yearMax={year_max}&yearMin={year_min}".format(
        brand=brand, energy=energy, power_min=power_min, year_min=year_min, year_max=year_max
    )
    response = browser.open(url)

    soup = BeautifulSoup(response.read(), 'html.parser')
    searchCard_elements = soup.find_all(class_='searchCard')   
    data = []

    for annonce in searchCard_elements:
        marque = annonce.find("h3").text
        modele = annonce.find(class_="Text_Text_text Vehiculecard_Vehiculecard_subTitle Text_Text_body2").text
        annee = annonce.find(class_="Text_Text_text Vehiculecard_Vehiculecard_characteristicsItems Text_Text_body2").text
        prix = annonce.find(class_="Text_Text_text Vehiculecard_Vehiculecard_priceContainer Text_Text_body3").text
        motor = annonce.find(class_="Text_Text_text Vehiculecard_Vehiculecard_subTitle Text_Text_body2").text
        data.append({
            "marque": marque,
            "modele": modele,
            "annee": annee,
            "prix": prix,
            "motor": motor,
        })
        print(marque, modele, annee, "Prix :", prix, motor, '\n')

    return data


# Récupérer les données des annonces
try:
    data = get_annonce_data(brand, year_min, year_max, power_min, energy)
except ValueError as e:
    print(e)
    exit()

# Écrire les données dans un fichier CSV
with open("audi.csv", "w", newline="") as fd:
    writer = csv.writer(fd)
    writer.writerow(["Marque", "Modèle", "Année", "Prix", "Motor"])
    for row in data:
        writer.writerow(row)
