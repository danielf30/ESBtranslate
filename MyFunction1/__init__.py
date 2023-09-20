import azure.functions as func
import json
import dicttoxml

def main(myQueueItem: func.ServiceBusMessage, binder: func.Out[str], log: func.Logger):
    # Logging
    data = myQueueItem.get_body().decode('utf-8')
    log.info(f"Mensaje de Service Bus recibido: {data}")

    # Convertir JSON a XML
    json_obj = json.loads(data)
    xml_str = dicttoxml.dicttoxml(json_obj, custom_root="Root", ids=False).decode('utf-8')
    
    # Usar idCiudadano como el nombre del archivo
    file_name = f"{json_obj.get('idCiudadano', 'default')}.xml"

    # Usar binder para escribir en Blob Storage
    output_blob: func.Out[str] = binder.bind(func.Out[str], blobPath=f"output-service-rest/output/{file_name}")
    output_blob.set(xml_str)
