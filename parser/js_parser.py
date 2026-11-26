def parse_file(file_path, parser):
  with open(file_path, "rb") as file:
    source_code = file.read()

  tree = parser.parse(source_code)

  return tree, source_code