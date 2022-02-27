## Vet for your pet 
![](https://raw.githubusercontent.com/AnitaSafar/Vet_app_project/main/demo/small_Vetlogo.png)

## About 
A vet management app for veterinary practice to help them manage their animals and vets. The user can assign multiple animals to a vet, but an animal can only be registered with one vet. The user is able to register new animals, look at their details, update the details and delete animals if necessary.

## Home 
![](https://raw.githubusercontent.com/AnitaSafar/Vet_app_project/main/demo/home.png)

## Pets
![](https://raw.githubusercontent.com/AnitaSafar/Vet_app_project/main/demo/clan.png)

## Adding pet
![](https://raw.githubusercontent.com/AnitaSafar/Vet_app_project/main/demo/add_pet.png)

## Pet's details
![](https://raw.githubusercontent.com/AnitaSafar/Vet_app_project/main/demo/pet_details.png)

## Updating pet
![](https://raw.githubusercontent.com/AnitaSafar/Vet_app_project/main/demo/pet_update.png)

## Vets
![](https://raw.githubusercontent.com/AnitaSafar/Vet_app_project/main/demo/vets.png)

## Adding vet
![](https://raw.githubusercontent.com/AnitaSafar/Vet_app_project/main/demo/add_vet.png)

## Vet's details
![](https://raw.githubusercontent.com/AnitaSafar/Vet_app_project/main/demo/vet_details.png)

## Updating vet
![](https://raw.githubusercontent.com/AnitaSafar/Vet_app_project/main/demo/vet_update.png)


## How to Run

### Client:
Start the application in development mode. 
Running this command will open ( http://localhost:5000 ) in a browser to view the application:
flask run

### Creating the database:
To get the application to connect to the database, you will need to create that database:
createdb -d vet_management

Then creating the tables within the database:
psql -d vet_management -f db/vet_management.sql

## Built with
- Python
- Flask
- PostgreSQL

## Future plans
- Mark owners as being registered/unregistered with the Vet. Unregistered owners won't be able to add any more animals.
- Be able to add multiple pets to an owner, keep track of owners' details without repetition.
- Handle check-in / check-out dates.
- Be able to add appointments, including pricing and billing.