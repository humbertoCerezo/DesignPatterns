from adapters import CsvToJsonAdapter
from data_handler import JsonDataHandler, CsvDataHandler

def load_and_display_data(data_handler, file_path):
    data = data_handler.load_data(file_path)
    print(data)

if __name__ == '__main__':
    #JSON HANDLER
    json_handler = JsonDataHandler()
    json_file_path = 'Archivos/archivojson.json'
    load_and_display_data(json_handler, json_file_path)

    #CSV HANDLER WITH ADAPTER
    csv_handler = CsvDataHandler()
    csv_file_path = 'Archivos/archivocsv.csv'
    csv_adapter = CsvToJsonAdapter(csv_handler)
    load_and_display_data(csv_adapter, csv_file_path)
