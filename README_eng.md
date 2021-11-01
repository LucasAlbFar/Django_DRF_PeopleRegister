[<img src="https://img.shields.io/badge/author-Lucas Faria-yellow?style=flat-square"/>](https://github.com/LucasAlbFar)

# API Django REST Framework People Register

API that simulates a people records controller, allowing the client to:

* Register categories in which a person can be registered;
* Register and update data of a new person in the system;
* Upload an identification file of a specific registered person;
* View all media loaded in the system or filter these records by each person registered in the system;
* Consult the audit of additions and updates of a person's data or the system audit list;

## Endpoints:
*  /admin/ -> site administration
* /type/ -> view and register a person's category;
* /mediatype/ -> view the types of identification media allowed in the system;
* /person/ -> register and view the people registered in the system;
* /media/ -> register and view each person's identification files;
* /audit/ -> view all system audits;
* /listaudit/int:pk/ -> list all audits for a given person in the system;
* /listperson/int:cpf/ -> list a person by their cpf;
* /listmedia/int:pk/ -> list all media through the registered person's ID key;
* /swagger/ -> API documentation
* /redoc/ -> API documentation

## Operations:
When starting the application, the PERSON TYPE and MEDIA TYPE data will be automatically loaded with some default values, and the client will be able to include new categories in the PERSON TYPE table through the POST command. 
With the system loaded, it will be possible to register a new person in the system, informing NAME, CPF, COMPANY and PERSON TYPE as mandatory data and PHONE as optional data. 
After registration, it is possible to view the audit record in '/audit/' or '/listaudit/int:pk/' through the PERSON table ID, all people registered through '/person/' or list only the data of a person through '/listperson/int:cpf/', informing the desired CPF. 
Using the PACTH command, it will be possible to update a person's record data. If there is an update of the CPF,the same will be recorded in the audit, or when there is an update with the person's record, the audit database will also be updated. With the registration of an individual completed, 
it will be possible to include an identification medium (photo or biometrics). The upload is done through the URL '/media/', informing which person the image will be linked to and the application will convert the image to base64. 
The media query can be performed by '/listmedia/int:pk/' informing the PERSON table ID.informing to which registered person the image will be linked and the application will convert the image to base64. 


## Strategies:
* For usability reasons, the application itself converts to a 256kb file;
* To limit the number of media types (MEDIA TYPE), an endpoint to perform POST on this table was not provided;

## Environment information:
[requirements.txt](https://github.com/LucasAlbFar/Django_DRF_PeopleRegister/blob/main/api/requirements.txt)

## Contact:
[<img src="https://img.shields.io/badge/LucasFaria-0A66C2?style=flat-square&logo=linkedin&logoColor=white" />](https://www.linkedin.com/in/lucasalbfar/)
[<img src="https://img.shields.io/badge/lucasalbfar@gmail.com-EA4335?style=flat-square&logo=Gmail&logoColor=white" />](mailto:lucasalbfarw@gmail.com)
