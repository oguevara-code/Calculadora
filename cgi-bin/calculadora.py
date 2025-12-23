import cgi
import re

print("Content-Type: text/html\n")

formulario = cgi.FieldStorage()
expresion = formulario.getvalue("expresion")

print("<html>")
print("<head>")
print("<title>Calculadora</title>")
print('<link rel="stylesheet" href="/css/estilos.css">')
print("</head>")
print("<body>")

print("<h2>Resultado de la calculadora</h2>")

patron = r'^[0-9+\-*/(). ]+$'

if expresion and re.match(patron, expresion):
    try:
        resultado = eval(expresion)
        print("<p>Expresión:", expresion, "</p>")
        print("<p>Resultado:", resultado, "</p>")
    except ZeroDivisionError:
        print("<p>Error: división entre cero</p>")
    except:
        print("<p>Error al calcular la expresión</p>")
else:
    print("<p>Expresión no válida</p>")

print("</body>")
print("</html>")