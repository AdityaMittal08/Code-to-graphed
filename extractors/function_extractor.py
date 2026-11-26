findings ={
  "functions": [],
}

function_types = [
  "function_declaration",
  "function_expression",
  "generator_function_declaration",
  "generator_function",
  "method_definition",
  "arrow_function"
]

def extract_functions(node, source_code):
  if node.type in function_types:
    function_name = None
    params = None

    name_node = node.child_by_field_name("name")

    if(name_node):
      function_name = source_code[
        name_node.start_byte:name_node.end_byte
      ].decode("utf8")
    elif(node.type == "arrow_function"):
      parent = node.parent

      if parent and parent.type == "variable_declarator":
        name_node = parent.child_by_field_name("name")

        if(name_node):
          function_name = source_code[
            name_node.start_byte:name_node.end_byte
          ].decode("utf8")

    parameters = node.child_by_field_name("parameters")

    if parameters:
      params = source_code[
        parameters.start_byte:parameters.end_byte
      ].decode("utf8")
    else:
      parameter = node.child_by_field_name("parameter")

      if parameter:
        params = source_code[
          parameter.start_byte:parameter.end_byte
        ].decode("utf8")


    findings["functions"].append({
      "name": function_name,
      "function_type": node.type,
      "parameters": params,
    })

    for child in node.children:
      extract_functions(child)

    return findings

