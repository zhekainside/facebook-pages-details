thonimport json

def export_to_json(data, output_file):
    with open(output_file, 'w') as f:
        json.dump(data, f, indent=4)