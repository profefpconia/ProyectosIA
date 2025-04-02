import feedparser
import datetime
import os
import re

def sanitize_html(html_content):
    """
    Elimina etiquetas meta obsoletas y las reemplaza con las recomendadas
    """
    # Reemplazar etiqueta obsoleta con la versión recomendada
    html_content = re.sub(
        r'<meta\s+name="apple-mobile-web-app-capable"\s+content="yes">',
        '<meta name="mobile-web-app-capable" content="yes">',
        html_content
    )
    return html_content

def parse_rss_to_html(rss_url):
    """
    Parsea un feed RSS y devuelve su contenido en formato HTML
    """
    # Obtenemos los datos del feed
    feed = feedparser.parse(rss_url)
    
    # Creamos el contenido HTML 
    html_content = f"""
    <!DOCTYPE html>
    <html lang="es">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <meta name="mobile-web-app-capable" content="yes">
        <title>{feed.feed.title}</title>
        <style>
            body {{
                font-family: Arial, sans-serif;
                line-height: 1.6;
                max-width: 1200px;
                margin: 0 auto;
                padding: 20px;
                background-color: #f5f5f5;
            }}
            header {{
                background-color: #1a365d;
                color: white;
                padding: 20px;
                text-align: center;
                margin-bottom: 20px;
                border-radius: 5px;
            }}
            .article {{
                background-color: white;
                padding: 20px;
                margin-bottom: 20px;
                border-radius: 5px;
                box-shadow: 0 2px 5px rgba(0,0,0,0.1);
            }}
            .article h2 {{
                margin-top: 0;
                color: #1a365d;
            }}
            .article .meta {{
                color: #666;
                font-size: 0.9em;
                margin-bottom: 10px;
            }}
            .article a {{
                color: #1a365d;
                text-decoration: none;
            }}
            .article a:hover {{
                text-decoration: underline;
            }}
            footer {{
                text-align: center;
                margin-top: 20px;
                color: #666;
                font-size: 0.9em;
            }}
        </style>
    </head>
    <body>
        <header>
            <h1>{feed.feed.title}</h1>
            <p>{feed.feed.subtitle if 'subtitle' in feed.feed else ''}</p>
        </header>
        
        <main>
    """
    
    # Agregamos cada artículo
    for entry in feed.entries:
        # Intentamos obtener la fecha de publicación
        try:
            date = datetime.datetime.strptime(entry.published, "%a, %d %b %Y %H:%M:%S %z")
            date_str = date.strftime("%d/%m/%Y %H:%M")
        except:
            date_str = "Fecha no disponible"
        
        # Obtenemos la descripción o el resumen y limpiamos etiquetas obsoletas
        description = entry.description if 'description' in entry else entry.summary if 'summary' in entry else "No hay descripción disponible"
        description = sanitize_html(description)
        
        html_content += f"""
            <article class="article">
                <h2><a href="{entry.link}" target="_blank">{entry.title}</a></h2>
                <div class="meta">Publicado: {date_str}</div>
                <div class="content">
                    {description}
                </div>
                <p><a href="{entry.link}" target="_blank">Leer más</a></p>
            </article>
        """
    
    # Cerramos el HTML
    html_content += f"""
        </main>
        
        <footer>
            <p>Generado el {datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")}</p>
            <p>Feed RSS: <a href="{rss_url}" target="_blank">{rss_url}</a></p>
        </footer>
    </body>
    </html>
    """
    
    # Sanitizamos todo el contenido HTML final
    html_content = sanitize_html(html_content)
    
    return html_content

def save_html(content, output_file="rss_noticias.html"):
    """
    Guarda el contenido HTML en un archivo
    """
    with open(output_file, "w", encoding="utf-8") as file:
        file.write(content)
    
    return os.path.abspath(output_file)

def main():
    # URL del feed RSS
    rss_url = "https://e00-elmundo.uecdn.es/elmundo/rss/portada.xml"
    
    print(f"Descargando feed RSS desde {rss_url}...")
    html_content = parse_rss_to_html(rss_url)
    
    output_file = save_html(html_content)
    print(f"Archivo HTML generado exitosamente en: {output_file}")
    
    # Abrir el archivo HTML en el navegador predeterminado (opcional)
    try:
        import webbrowser
        webbrowser.open('file://' + output_file)
        print("Abriendo archivo en el navegador...")
    except:
        print("No se pudo abrir el navegador automáticamente.")

if __name__ == "__main__":
    main()
