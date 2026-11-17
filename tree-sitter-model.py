import tree_sitter_javascript as tsJavascript
from tree_sitter import Language, Parser

JS_Language = Language(tsJavascript.language())

parser = Parser(JS_Language)

with open("input.js", "rb") as file:
  source_code = file.read()

tree = parser.parse(source_code)

root_node = tree.root_node

def print_functions(node):
  function_types = [
        "function_declaration",
        "function_expression",
        "generator_function_declaration",
        "generator_function",
        "method_definition"
    ]

  if(node.type in function_types):
    print("Function type: ", node.type)
    name_node = node.child_by_field_name("name")

    if(name_node):
      function_name = source_code[
        name_node.start_byte:name_node.end_byte
      ].decode("utf8")

      print("Function name: ",function_name)

    else:
      print("Function name: Anonymous or assigned externally")

    parameters = node.child_by_field_name("parameters")
    
    if parameters:
        params = source_code[
            parameters.start_byte:parameters.end_byte
        ].decode("utf8")
    
    print("Parameters:", params)

  if node.type == "arrow_function":
     parent = node.parent
     if(parent and parent.type == "variable_declarator"):
        print("Function name:", node.type)
        name_node = parent.child_by_field_name("name")

        if(name_node):
          function_name = source_code[
            name_node.start_byte:name_node.end_byte
          ].decode("utf8")
    
          print("Function name: ",function_name)

        else:
              print("Function name: Anonymous or assigned externally")


        parameters = node.child_by_field_name("parameters")
    
        if parameters:
            params = source_code[
                parameters.start_byte:parameters.end_byte
            ].decode("utf8")
        
        print("Parameters:", params)

  for child in node.children:
        print_functions(child)
print_functions(root_node)