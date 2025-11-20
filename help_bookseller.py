def stock_list(lista_de_libros, categorias):
    if not lista_de_libros or not categorias:
        return ""
    
    total_por_categoria = {categoria: 0 for categoria in categorias}
    
    for libro in lista_de_libros:
        codigo, cantidad_texto = libro.split()
        if codigo[0] in total_por_categoria:
            total_por_categoria[codigo[0]] += int(cantidad_texto)
    
    return " - ".join(f"({categoria} : {total_por_categoria[categoria]})" for categoria in categorias)