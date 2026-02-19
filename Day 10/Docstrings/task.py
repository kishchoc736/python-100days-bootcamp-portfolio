def format_name(f_name, l_name):
    """Take a first and last name and return a formatted name."""
    formated_f_name = f_name.title()
    formated_l_name = l_name.title()
    return f"{formated_f_name} {formated_l_name}"


formatted_name = format_name("AnGeLa", "YU")

length = len(formatted_name)


example_string = ("Hello "
                  "World "
                  "How are you")
print(example_string)
