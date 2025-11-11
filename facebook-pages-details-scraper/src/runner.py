thonimport json
from extractors.facebook_parser import parse_facebook_page
from outputs.exporters import export_to_json
from config.settings import SETTINGS

def main():
    # Load the sample input file
    with open(SETTINGS['input_file'], 'r') as f:
        pages = f.readlines()

    data = []

    for page in pages:
        page_data = parse_facebook_page(page.strip())
        if page_data:
            data.append(page_data)

    # Export the data to a JSON file
    export_to_json(data, SETTINGS['output_file'])

if __name__ == "__main__":
    main()