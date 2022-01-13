# TC 3: Algoritmo de Jaro–Winkler 

## Autores
> Nadia González Fernández C412
>
> Luis Alejandro Lara Rojas C412

## Resumen
El proyecto presenta una automatización del algoritmo Jaro-Winkler distance. 
Este algoritmo es usado para hallar una métrica que permite establecer una comparación de similitud entre dos cadenas de caracteres. 

La solución fue hecha en el lenguaje de programación Python.

## Descripción
### Definición de Similitud de Jaro:

La similitud de Jaro $sim_j$ de dos cadenas $s_1$ y $s_2$ es:
$$sim_j=\begin{cases} 0,&\text{si $m = 0$}\\\frac{1}{3}(\frac{m}{|s_1|} + \frac{m}{|s_2|} + \frac{m-t}{m}),&\text{si $m \neq 0$}\end{cases}$$

Donde:
- $|s_i|$ es la longuitud de la cadea
 $s_i$
 - $m$ es el número de caracteres *coincidentes*
 - $t$ es el número de transposiciones

*Nota:* Dos caracteres de $s_1$ y $s_2$ respectivamente se consideran *coincidentes* solo si son iguales o 
si no distan más de $\lfloor \frac{max(|s_1|, |s_2|)}{2} \rfloor - 1$ caracteres.

### Definición de la Similitud de Jaro-Winkler:

La similitud de Jaro-Winkler $sim_w$ es:

$sim_w =  sim_j + lp(1 - sim_j)$

Donde:
- $sim_j$ es la similitud de Jaro de las cadenas $s_1$ y $s_2$
- $l$ es la longuitud del prefijo común de las cadenas de a lo sumo 4 caracteres
- $p$ es una constante que aumenta cuando las cadenas tienen prefijos comunes. El valor estandar es $p = 0.1$

La **distancia de Jaro-Winkler** $d_w$ se define como:

$d_w = 1- sim_w$

### Ejecutar código

Para correr el código debe insertar en consola dentro de la carpeta `scr`:
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