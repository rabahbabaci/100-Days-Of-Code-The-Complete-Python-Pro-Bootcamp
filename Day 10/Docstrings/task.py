def format_name(f_name, l_name):
    """
    Takes first and last name and format it to
    return the title case version of the name.
    :param f_name: first name
    :param l_name: last name
    :return: full name in title case
    """
    formated_f_name = f_name.title()
    formated_l_name = l_name.title()
    return f"{formated_f_name} {formated_l_name}"


formatted_name = format_name("AnGeLa", "YU")

length = len(formatted_name)



