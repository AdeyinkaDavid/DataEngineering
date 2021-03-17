import pprint
import veryfi

#To run verfyi we will need the below variables to get the veryfi documents 
client_id = "vrfrhs2b3HNTg64KMkEsFdVKPOHbj06zj3SecW0"
client_secret = "EwEBJT2I0WEjF6nzi0Ao75R1o7iKrfMnYm2p9zc3bll7ZlYgMvVT5nZsDjPn4dEtchfJF1uOI10N9xrrXwKapB9vHGviJMrSKIPYfyL7jT8AVoIp6M4ZzlXPjIFly7GA"
username = "davidisaac905"
api_key = "003e325f2183e2546f292363d10002e7"


#Now we instantiate the client 
client = veryfi.Client(client_id, client_secret, username, api_key)

#Here we want to create a categories of what we want from the documents from veryfi 
categories = ["Travel", "Airfare", "Lodging", "Job Supplies and Materials", "Grocery"]

#Here we get the receipt and invoice processed 
result = client.process_document("files.invoice.pdf", categories)

print(result)

