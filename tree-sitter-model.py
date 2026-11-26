import tree_sitter_javascript as tsJavascript
from tree_sitter import Language, Parser
from pathlib import Path
import json

JS_Language = Language(tsJavascript.language())

parser = Parser(JS_Language)

folder = Path(__file__).parent / "js_files"

for file_path in folder.glob("*.js"):

  with open(file_path, "rb") as file:
    source_code = file.read()

  tree = parser.parse(source_code)

  root_node = tree.root_node

  findings ={
    "file": file_path.name,
    "functions": [],
    "imports": [],
    "function calls": [],
  }

  function_types = [
    "function_declaration",
    "function_expression",
    "generator_function_declaration",
    "generator_function",
    "method_definition",
    "arrow_function"
  ]

  def getReturnStatment(node, returns):
    if node.type == "return_statement":
      if node.named_children:
        return_node = node.named_children[0]

        expression = source_code[
          return_node.start_byte:return_node.end_byte
        ].decode("utf8")

        returns.append(expression)
      return
    
    if node.type in function_types:
      return

    for child in node.children:
      getReturnStatment(child, returns)   

  def print_functions(node):

    if(node.type in function_types):

      function_name = None
      params = None
      returns = []

      name_node = node.child_by_field_name("name")

      if(name_node):

        function_name = source_code[
          name_node.start_byte:name_node.end_byte
        ].decode("utf8")

      elif(node.type == "arrow_function"):
         parent = node.parent

         if parent and parent.type == "variable_declarator":
            name_node = parent.child_by_field_name("name")

            if name_node:
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


      body = node.child_by_field_name("body")

      if body:
        if node.type == "arrow_function" and body.type != "statment_block":

          expression = source_code[
              body.start_byte:body.end_byte
          ].decode("utf8")

          returns.append(expression)
        else:
         getReturnStatment(node, returns)

      findings["functions"].append({
         "name": function_name,
         "function_type": node.type,
         "parameters": params,
         "returns": returns
      })

    for child in node.children:
          print_functions(child)

  print_functions(root_node)

  # def print_imports(node):
  #     if(node.type == "import_statement"):
  #       import_info = {
  #           "source": None,
  #           "imports": []
  #       }

  #       source_node = node.child_by_field_name("source")

  #       if source_node:
  #         source = source_code[
  #           source_node.start_byte:source_node.end_byte
  #         ].decode("utf8")

  #         import_info["source"] = source[1:-1]

  #     source_node = node.child_by_field_name("source")

  with open("findings.json", "w") as file:
     json.dump(findings, file, indent=2)