from lxml import etree
import os

def extract_jugador_ids(xml_files):
    for xml_file in xml_files:
        jugador_ids = {}
        total_jugador_ids = 0
        output_file = os.path.splitext(xml_file)[0] + "_jugador_ids.txt"

        with open(output_file, "w") as out_file:
            context = etree.iterparse(xml_file, events=("end",))

            for event, elem in context:
                if elem.tag.endswith("JugadorId"):
                    jugador_id = elem.text.strip() if elem.text else None
                    jugador_ids.setdefault(elem.tag, []).append(jugador_id)
                    total_jugador_ids += 1
                    out_file.write(f"{jugador_id}\n")

                elem.clear() # limpiar buffer cada vez que se lee un archivo

        print(f"Total de JugadorId encontrados en {xml_file}: {total_jugador_ids}")

def main():
    xml_folder = r"./TODOS"  # Especifica la ruta de tu directorio de XML
    xml_files = [os.path.join(xml_folder, file) for file in os.listdir(xml_folder) if file.endswith('.xml')]
    
    extract_jugador_ids(xml_files)

if __name__ == "__main__":
    main()
