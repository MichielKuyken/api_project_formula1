# api_project_formula1

## Thema
Ik heb dit thema gekozen omdat ik een grote fan ben van de Fomrule 1. Ik ken er heel veel van en vond dit daarom ook een leuk onderwerp om een API over te maken. Het leek me interessant en leerrijk om zelf een database te maken waaruit mensen dan informatie kunnen halen zoals de coureurs, de grandprix en de standings. 

## API
Mijn API is zo gemaakt dat iedereen gegevens kan toevoegen en opvragen. Ik heb daarom voor elke tabel een get- en post-request gemaakt zodat het mogelijk is om coureurs, grandprix en standings toe te voegen en bekijken. Om de reeds toegevoegde coureurs aan te passen of te verwijderen hebben ze adminprivileges nodig. Er is slechts 1 persoon die een admin kan zijn. Als er al een admin-account is aangemaakt en iemand wil een nieuw account toevoegen, is dit niet meer mogelijk. Het verwijderen van het admin-account is ook enkel mogelijk door de admin zelf. Hiervoor heb ik gebruikgemaakt van Basic Auth. Voor het aanpassen van de gegevens heb ik gebruikgemaakt van een put-request.
Ik heb ook een front-end gemaakt waarop je alle coureurs, grandprix en standings kunt zien. Dit geeft een gestructureerder beeld van de API en het bevat enkel de nodige informatie. De front-end heb ik op een andere GitHub staan en wordt gehost via GitHub Pages. De link naar deze GitHub vindt u hieronder.

[GitHub front-end](https://github.com/MichielKuyken/fomula1_api.github.io)

### [Link API](https://useritem-api-service-michielkuyken.cloud.okteto.net/)

## Postman requests screenshots
Post admin:

![post admin screenshot](/Screenshots/post_admin.png)

Delete admin:

![delete admin screenshot](/Screenshots/delete_admin.png)

Delete admin authentication:

![delete admin authentication screenshot](/Screenshots/delete_admin_auth.png)

Post driver:

![post driver screenshot](/Screenshots/post_driver.png)

Get drivers:

![get drivers screenshot](/Screenshots/get_drivers.png)

Get driver:

![get driver screenshot](/Screenshots/get_driver_by_lastname.png)

Put driver:

![put driver screenshot](/Screenshots/put_driver.png)

Put driver authentication:

![put driver authentication screenshot](/Screenshots/put_driver_auth.png)

Delete driver:

![delete driver screenshot](/Screenshots/delete_driver.png)

Delete driver authentication:

![delete driver authentication screenshot](/Screenshots/delete_driver_auth.png)

Delete driver proof:

![delete driver proof screenshot](/Screenshots/delete_driver_proof.png)

Post grandprix:

![post grandprix screenshot](/Screenshots/post_grandprix.png)

Get grandprix:

![get grandprix screenshot](/Screenshots/get_grandprix.png)

Get specific grandprix:

![get specific grandprix screenshot](/Screenshots/get_grandprix_by_circuitnaam.png)

Put grandprix:

![put grandprix screenshot](/Screenshots/put_grandprix.png)

Put grandprix authentication:

![put grandprix authentication screenshot](/Screenshots/put_grandprix_auth.png)

Delete grandprix:

![delete grandprix screenshot](/Screenshots/delete_grandprix.png)

Delete grandprix authentication:

![delete grandprix authentication screenshot](/Screenshots/delete_grandprix_auth.png)

Delete grandprix proof:

![delete grandprix proof screenshot](/Screenshots/delete_grandprix_proof.png)

Post standings:

![post standings screenshot](/Screenshots/post_standings.png)

Get standings:

![get standings screenshot](/Screenshots/get_standings.png)

Get specific standings:

![get specific standings screenshot](/Screenshots/get_standings_by_lastname.png)

Put standings:

![put standings screenshot](/Screenshots/put_standings.png)

Put standings authentication:

![put standings authentication screenshot](/Screenshots/put_standings_auth.png)

Delete standings:

![delete standings screenshot](/Screenshots/delete_standings.png)

Delete standings authentication:

![delete standings authentication screenshot](/Screenshots/delete_standings_auth.png)

Delete standings proof:

![delete standings proof screenshot](/Screenshots/delete_standings_proof.png)

## OpenAPI docs screenshots
Post admin:

![post admin docs screenshot](/Screenshots/docs_post_admin.png)

Delete admin:

![delete admin docs screenshot](/Screenshots/docs_delete_admin.png)

Post driver:

![post driver docs screenshot](/Screenshots/docs_post_driver.png)

Get drivers:

![get drivers docs screenshot](/Screenshots/docs_get_drivers.png)

Get specific driver:

![get specific driver docs screenshot](/Screenshots/docs_get_specific_driver.png)

Put driver:

![put driver docs screenshot](/Screenshots/docs_put_driver.png)

Delete driver:

![delete driver docs screenshot](/Screenshots/docs_delete_driver.png)

Post grandpirx:

![post grandprix docs screenshot](/Screenshots/docs_post_grandprix.png)

Get grandprix:

![get grandprix docs screenshot](/Screenshots/docs_get_grandprix.png)

Get specific grandprix:

![get specific grandprix docs screenshot](/Screenshots/docs_get_specific_grandprix.png)

Put grandprix:

![put grandprix docs screenshot](/Screenshots/docs_put_grandprix.png)

Delete grandprix:

![delete grandprix docs screenshot](/Screenshots/docs_delete_grandprix.png)

Post standings:

![post standings docs screenshot](/Screenshots/docs_post_standings.png)

Get standings:

![get standings docs screenshot](/Screenshots/docs_get_standings.png)

Get specific standings:

![get specific standings docs screenshot](/Screenshots/docs_get_specific_standings.png)

Put standings:

![put standings docs screenshot](/Screenshots/docs_put_standings.png)

Delete standings:

![delete standings docs screenshot](/Screenshots/docs_delete_standings.png)
