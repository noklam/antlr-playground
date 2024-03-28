1. Download grammar from https://github.com/antlr/grammars-v4/tree/master/python/python3
2. Download the Base class
3. Run `tranforms_grammar.py` to fix the grammar
4. `antlr4 -Dlanguage=Python3 *.g4` to generator the Parser, Listener, Lexer (or visitor too with the flag)
