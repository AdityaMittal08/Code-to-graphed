TREE- SITTER Model

1. Reading the input.js as binary such that it can be parsed with the help of tree-sitter and create a tree.
2. We have mentioned all types of functions which can be present in a javascript file and then pass it as a node and if the node.type is equal to the list we made, then
3. we check for the name of the child, and grab the details we need, such as function name, parameters, return statements, etc.
4. we also need to decode firstly to understand what is actually written in the source code as it was read as binary.
5. For the arrow functions, it is a bit different and hence we need to apply for it separately.

Updated:

1. Arrow function case is still handled differently but instead of separating it completely, it is now present in if else with others.
2. Return expressions are obtained with the help of tree-sitter. Firstly we need a check whether body is present or it the function is defined empty. Then we store all the return expression in a list.
3. For now all the test javascript files are stored in folder js_files.
4. In tree-sitter-model.py, for loop covers all the files present in the js_files and parse through each them.
5. All the derived expressions are stored in a dictionary which is then converted to a JSON file.
