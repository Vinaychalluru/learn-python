
def get_full_name(first, last):
    """Return a full name."""
    full_name = "{0} {1}".format(first, last)
    return full_name

def get_title_name(first, last):
    """Return a full name in Title case."""
    # return f"{first} {last}".title()
    # Uncomment the above line and comment the below line for a Successful Test case result
    return f"{first.title()} {last}"