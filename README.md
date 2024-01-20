# learning-python
Este es un repositorio de scripts en lenguaje de programación Python para del Diplomado de Inteligencia Computacional

# Proceso Staging: 

Primer comando: Enviar paquete a staging o a cola
$git add . / $git add --all / git add FILE_NAME.ext / git add FOLDER_NAME

Segundo comando: Anexar mensaje - ¿Qué contiene el paquete?
$git commit -m "Aquí va el mensaje" //-m significa message

Tercer comando: Enviar o desplegar el paquete hacia su destino (RAMA)
$git push origin NOMBRE_RAMA/BRANCH_NAME / $git push

# Comandos para hacer seguimiento al Staging
$git reset FILE_NAME.ext o $git restore --staged FILE_NAME.ext--> Saca el archivo de cola de Staging
$git status --> Verificar el estado del staging del repositorio
$git log --> Ver la trazabilidad o log de cambios realizados