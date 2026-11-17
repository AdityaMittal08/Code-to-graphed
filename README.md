TREE- SITTER Model

1. Reading the input.js as binary such that it can be parsed with the help of tree-sitter and create a tree.
2. We have mentioned all types of functions which can be present in a javascript file and then pass it as a node and if the node.type is equal to the list we made, then
3. we check for the name of the child, and grab the details we need, such as function name, parameters, return statements, etc.
4. we also need to decode firstly to understand what is actually written in the source code as it was read as binary.
5. For the arrow functions, it is a bit different and hence we need to apply for it separately.
6.
