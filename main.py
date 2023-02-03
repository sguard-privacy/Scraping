Energy = "ess"
Brand= "AUDI"
MaxKm = "100000"
MaxPrice= "28000"
MinYear= "2010"
url = "https://www.lacentrale.fr/listing?energies={Energy}&makesModelsCommercialNames={Brand}&mileageMax={MaxKm}&priceMax={MaxPrice}&yearMin={MinYear}" .format(Energy=Energy, Brand=Brand, MaxKm=MaxKm, MaxPrice=MaxPrice, MinYear=MinYear)
print(url)


"""
"""