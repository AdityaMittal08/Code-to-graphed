import tree_sitter_javascript as tsJavascript
from tree_sitter import Language, Parser
from pathlib import Path
import json

from parser.js_parser import parse_file

from extractors.function_extractor import extract_functions

JS_Language = Language(tsJavascript.language())

parser = Parser(JS_Language)

folder = Path(__file__).parent / "js_files"

for file_path in folder.glob("*.js"):
  tree, source_code = parse_file(file_path, parser)

  root_node = tree.root_node

  function_findings = extract_functions(root_node, source_code)
  

