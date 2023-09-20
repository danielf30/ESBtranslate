import azure.functions as func
import json
import dicttoxml

def main(myQueueItem: func.ServiceBusMessage, outputBlob: func.Out[str]) -> None:
    # Decodificar el mensaje del Service Bus
    data = myQueueItem.get_body().decode('utf-8')
    
    # Convertir el mensaje en un objeto JSON
    json_obj = json.loads(data)

    # Convertir el JSON a XML
    xml_str = dicttoxml.dicttoxml(json_obj, custom_root="Root", ids=False).decode('utf-8')

    # Escribir el XML en Blob Storage
    outputBlob.set(xml_str)
