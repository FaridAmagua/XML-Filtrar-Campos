from lxml import etree

# DEF TAG <JugadorId>"Value"</JugadorId>
def extract_jugador_ids(xml_file, output_file):
    jugador_ids = {}
    total_jugador_ids = 0
    context = etree.iterparse(xml_file, events=("end",))

    with open(output_file, "w") as out_file:
        for event, elem in context:
            if elem.tag.endswith("JugadorId"):
                jugador_id = elem.text.strip() if elem.text else None
                print(f"Elemento: {elem.tag}, Texto: {jugador_id}")
                jugador_ids[elem.tag] = jugador_id
                total_jugador_ids += 1
                out_file.write(f"{jugador_id}\n")

            elem.clear()  # clear buffer

    return jugador_ids, total_jugador_ids

def main():
    xml_file = "test.xml"
    output_file = "jugador_ids.txt"

    jugador_ids, total_jugador_ids = extract_jugador_ids(xml_file, output_file)

    print(jugador_ids)
    print("Total de JugadorId encontrados:", total_jugador_ids)

if __name__ == "__main__":
    main()
