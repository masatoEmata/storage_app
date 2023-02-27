def save_svg(file_path: str, svg_data: str):
    with open(file_path, "w", encoding="utf-8") as svg_file:
        svg_file.write(svg_data)
