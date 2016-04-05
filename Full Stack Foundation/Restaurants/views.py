import utils


def get_restaurant_list_template():
    """
    :return: message that lists the name of the restaurants
    """
    restaurants = utils.get_restaurants()
    message = "<html><body>"
    message += "</br></br> Click <a href ='/restaurants/new'>here</a> to create a new restaurant.</br></br>"
    message += "The list of restaurant available are:</br></br>"
    for restaurant in restaurants:
        message += restaurant.name
        message += "</br>"
        message += "<a href ='#'>Edit</a>   "
        message += "<a href ='#'>Delete</a>"
        message += "</br></br></br>"
    message += "</body></html>"
    return message


def get_create_new_restaurant_form():
    """
    :return: template to be rendered on create new restaurant page
    """
    message = "<html><body>"
    message += "<h4> To create a new restaurant fill this form and click 'Create' </h4>"
    message += "<form method = 'POST' enctype='multipart/form-data' action = '/restaurants/new'>"
    message += "<input name = 'name' type = 'text' placeholder = 'New Restaurant Name' > "
    message += "<input type='submit' value='Create'>"
    message += "</form></body></html>"
    return message