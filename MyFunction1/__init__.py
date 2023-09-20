import os
import azure.functions as func
import json
import dicttoxml

blob_storage_conn_str = os.environ["BLOB_STORAGE_CONNECTION_STRING"]
service_bus_conn_str = os.environ["SERVICE_BUS_CONNECTION_STRING"]

def main(myQueueItem: func.ServiceBusMessage, outputBlob: func.Out[str], log: func.Logger):
    try:
        # Logging
        data = myQueueItem.get_body().decode('utf-8')
        log.info(f"Mensaje de Service Bus recibido: {data}")

        json_obj = json.loads(data)
        xml_str = dicttoxml.dicttoxml(json_obj, custom_root="Root", ids=False).decode('utf-8')
        
        outputBlob.set(xml_str)
    except Exception as e:
        log.error(f"Error al procesar el mensaje: {str(e)}")
