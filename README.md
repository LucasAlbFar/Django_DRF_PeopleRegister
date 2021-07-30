[<img src="https://img.shields.io/badge/author-Lucas Faria-yellow?style=flat-square"/>](https://github.com/LucasAlbFar)

# API Django REST Framework People Register

API que simula um controlador de registros de pessoas, permitindo ao client:
 * Cadastrar categorias em que uma pessoa poderá ser cadastrada;
 * Cadastrar e atualizar dados de uma nova pessoa no sistema;
 * Fazer upload de um arquivo de identificação de determinada pessoa cadastrada;
 * Visualizar todas as medias carregadas no sistema ou filtrar esses registros por cada pessoa registrada no sistema;
 * Consultar a auditoria das inclusões e atualizaçõe dos dados de uma pessoa ou a lista de auditoria do sistema;

## Endpoints:
* /admin/ -> administração site
* /type/ -> visualizar e cadastrar as categoria de uma pessoa;
* /mediatype/ -> visualizar os tipos de media de identificação permitidas no sistema;
* /person/ -> cadastrar e visualizar as pessoas registradas no sistema;
* /media/ -> cadastrar e visualizar os arquivos de identificação de cada pessoa;
* /audit/ -> vusualizar todas as auditorias do sistema;
* /listaudit/<int:pk>/ -> listar todas as auditorias para uma determinada pessoa do sistema;
* /listperson/<int:cpf>/ -> listar uma pessoa através do seu cpf;
* /listmedia/<int:pk>/ -> listar todas as medias através da chave ID da pessoa cadastrada;
* /swagger/ -> documentação da API 
* /redoc/ -> documentação da API 

## Informações de ambiente:
[requirements.txt](https://github.com/LucasAlbFar/Django_DRF_PeopleRegister/blob/main/api/requirements.txt)

## Contato:
[<img src="https://img.shields.io/badge/LucasFaria-0A66C2?style=flat-square&logo=linkedin&logoColor=white" />](https://www.linkedin.com/in/lucasalbfar/)
[<img src="https://img.shields.io/badge/lucasalbfar@gmail.com-EA4335?style=flat-square&logo=Gmail&logoColor=white" />](mailto:lucasalbfarw@gmail.com)
