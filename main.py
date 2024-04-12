from zeep import Client
from zeep.transports import Transport

class VerifyIdentityNumber:
    def __init__(self, identity_number, first_name, last_name, birth_year):
        self.identity_number = identity_number
        self.first_name = first_name
        self.last_name = last_name
        self.birth_year = birth_year

    def verify(self):
        # Define the WSDL URL
        wsdl_url = 'https://tckimlik.nvi.gov.tr/Service/KPSPublic.asmx?wsdl'

        # Create a SOAP client
        transport = Transport(timeout=10)
        client = Client(wsdl=wsdl_url, transport=transport)

        # Define parameters for the SOAP request
        parameters = {
            'TCKimlikNo': self.identity_number,
            'Ad': self.first_name,
            'Soyad': self.last_name,
            'DogumYili': self.birth_year
        }

        # Send the SOAP request and get the response
        response = client.service.TCKimlikNoDogrula(**parameters)

        return response

# Example usage
if __name__ == "__main__":
    identity_number = '19451167026'
    first_name = 'Ufuk'
    last_name = 'Çiçek'
    birth_year = 1995

    verifier = VerifyIdentityNumber(identity_number, first_name, last_name, birth_year)
    result = verifier.verify()

    if result:
        print("The identity number is verified.")
    else:
        print("The identity number is not verified.")
