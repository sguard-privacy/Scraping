import requests
from bs4 import BeautifulSoup


def scrap_listing():
    
    
    url = "https://www.lacentrale.fr/listing?energies={energy}&makesModelsCommercialNames={brand}&mileageMax={km_max}&mileageMin={km_min}&priceMax={price_max}&priceMin={price_min}&yearMax={year_max}&yearMin={year_min}".format(brand="AUDI", year_min="2010", year_max="2020", km_min="0", km_max="200000", energy="ess", price_min="1000", price_max="150000")

    requete = requests.get(url)    
    return requete.text
    
# if url.status_code == 200:
        
if __name__ == '__main__':
    
    for i in range (1,9):
        body = scrap_listing(brand="AUDI", year_min="2010", year_max="2020", km_min="0", km_max="200000", energy="ess", price_min="1000", price_max="150000")
        scrap = BeautifulSoup(body, 'html')
        cars = scrap.find_all(class_="Vehiculecard_Vehiculecard_cardBody")
        
        for scrap in cars:
            technical_sheet = scrap.find_all(class_='Text_Text_text Vehiculecard_Vehiculecard_characteristicsItems Text_Text_body2')
            
            price = cars.find(class_='Text_Text_text Vehiculecard_Vehiculecard_price Text_Text_subtitle2')
            
            brand = cars.find(class_='Text_Text_text Vehiculecard_Vehiculecard_title Text_Text_subtitle2')
            
            energy = cars.find(class_='Text_Text_text Vehiculecard_Vehiculecard_subTitle Text_Text_body2')
            
            print(brand.text)

            
            
            
      
    

  