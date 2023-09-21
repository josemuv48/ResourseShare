


def generate_count_list(cat_cnts):
    result = ''
    for cat_cnt in cat_cnts:
        result += f"<li>{cat_cnt['cat_id__cat']}: {cat_cnt['cnt']}</li>"
        
    return result