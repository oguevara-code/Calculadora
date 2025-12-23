import cgi
import re

formulario = cgi.FieldStorage()
expresion = formulario.getvalue("expresion")

print("<html>")
print("<body>")

patron = "[0-9+*/-]+"

if re.match(patron, expresion):
    resultado = eval(expresion)
    print("Resultado:", resultado)
else:
    print("Error")

print("</body>")
print("</html>")