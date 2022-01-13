# TC 3: Algoritmo de Jaro–Winkler 

## Autores
> Nadia González Fernández C412
>
> Luis Alejandro Lara Rojas C412

## Resumen
El proyecto presenta una automatización del algoritmo Jaro-Winkler distance. Para ello se ha tomado como referencia 
la definición del algoritmo dada en: https://en.wikipedia.org/wiki/Jaro–Winkler_distance. La solución fue hecha en el 
leguaje de programación Python.

## Descripción
### Ejecutar código

Para correr el código debe insertar en consola en la carpeta `scr`:
```
python3 run.py 
```

En pantalla aparecerá un diálogo. Inserte la información requerida:

```
Please insert your first string and then press enter:
>> MARTHA
Please insert your second string and then press enter:
>> MARHTA
```

Como resultado obtendrá:
```
Similarity was:  0.9611111111111111
```

### Aplicaciones del algoritmo Jaro-Winkler distance:
El algoritmo implementado puede ser utilizado para:
- Buscar personas en bases de datos. Es común que los sistemas tengan errores en los nombres de las personas,
 ya sea por faltas de ortografía o por errores de tipografía. Este algoritmo puede ayudar a encontar a la 
 persona registrada aun cuando la entrada no exista exactamente así en la base de datos.
- La implementación de correctores ortográficos. Normalmente las palabras insertadas con errores otrográficos varían
en pocas letras con la deseada. Analizando la palabra insertada el programa reconoce que no 
existe en su diccionario y aplicando el algoritmo puede buscar palabras que se escriban de forma similar y con alta probabilidad
sugerir la correcta.
- Cuantificar las distancias linguísticas o cuán distintos son dos idiomas.
- Saber cuán parecidos son dos documentos distintos. Actualmente existe mucha documentación en internet, lo cual permite un mayor 
acceso a información. Por otro lado, esto facilita el plagio. Este algoritmo puede ser utilizado para detectar plagios en estudios
y documentos. Tambien puede ser usado para analizar exámenes de distintos alumnos y según la similitud
 concluir si se ha hecho fraude.

## Referencias bibliográficas

- https://en.wikipedia.org/wiki/Jaro–Winkler_distance