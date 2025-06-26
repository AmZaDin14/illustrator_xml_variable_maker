import os
import logging
from xml.etree.ElementTree import Element, SubElement, indent, ElementTree, register_namespace
from .file_utils import read_csv_or_xlsx, sanitize_xml_tag

def csv_to_xml(input_file: str, output_file: str, var_set_name: str) -> str | None:
    try:
        header, rows = read_csv_or_xlsx(input_file)
        if not header:
            logging.error("Input file is empty or missing header.")
            return None

        root = Element('svg', attrib={...})  # Same as before
        variable_sets = SubElement(root, 'variableSets')
        variable_set = SubElement(variable_sets, 'variableSet', attrib={
            'locked': 'none', 'varSetName': var_set_name
        })
        variables = SubElement(variable_set, 'variables')

        for col_name in header:
            safe_name = sanitize_xml_tag(col_name)
            SubElement(variables, 'variable', attrib={'trait': 'textcontent', 'varName': safe_name})

        register_namespace('v', 'v')
        sample_data_sets = SubElement(variable_set, 'v:sampleDataSets', attrib={'xmlns:v': 'v'})

        seen = set()
        for row_num, row in enumerate(rows, start=2):
            if not row or len(row) != len(header): continue
            name = row[0]
            if name in seen: continue
            seen.add(name)
            data_set = SubElement(sample_data_sets, 'v:sampleDataSet', {'dataSetName': name})
            for idx, value in enumerate(row):
                tag = sanitize_xml_tag(header[idx])
                p = SubElement(SubElement(data_set, tag), 'p')
                p.text = value

        os.makedirs(os.path.dirname(output_file), exist_ok=True)
        tree = ElementTree(root)
        indent(tree, space="  ", level=0)
        tree.write(output_file, encoding='utf-8', xml_declaration=True)
        return output_file

    except Exception as e:
        logging.error(f"Conversion failed: {e}")
        return None
