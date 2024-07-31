import json
def singin_singup() :
    with open('kharidar.json', 'r') as kharidar_file:
        kharidars_list = json.load(kharidar_file)
    with open('seller.json', 'r') as seller_file:
        sellers_list = json.load(seller_file)
    

    print('welcome')

    approach_inp = input('1 - sign in \n 2 - signup')

    if approach_inp == '1':
        identity = input('1 - kharidar \n2 - foroshande')
        if identity == '1':
            username_inp = input('enter your username : ')
            password_inp = input('enter your password : ')
            for kharidar in kharidars_list :
                if username_inp == kharidar[0] and password_inp == kharidar[1]:
                    print("sign in was successful")
                    return username_inp , password_inp
            print('unsuccessful attempt')
            raise IndentationError

        if identity == '2':
            username_inp = input('enter your username : ')
            password_inp = input('enter your password : ')
            for seller in sellers_list :
                if username_inp == seller[0] and password_inp == seller[1]:
                    print("sign in was successful")
                    return username_inp , password_inp
            print('unsuccessful attemt')
            raise IndentationError
            
        elif identity == '2':
            pass
            
