def colors():
    all_colors = ["white", "red", "blue", "white", "purple", "red", "black", "white", "black"] 

    count = 0
    for color in all_colors:
        print(colors)

        if color == "white" or color == "black":
            count += 1

    print("The result is " + str(count))

colors()



# look up Rest api
#http method http codes
#get post put patch delete / 200 300 400 500 

# py -m venv venv
# venv\Scripts\activate
# py server.py
# deactivate

# remember to deactivate auto save for python, it will cause problems