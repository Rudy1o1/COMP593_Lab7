def main():

    #Intialize the complex data strcture 
    personal_info ={
        'name': 'Rudy',
        'student_id' : 10254128,
        'pizza_toppings':[
            'Fresh Garlic',
            'Tomato',
            'Extra Cheese',
        ],
        'movies':[
            {
                'title':'Arrival',
                'genre':'Sci-Fi'
            },
            {
                'title':'Death On The Nile',
                'genre':'suspense'
            }
        ]
    }
    #Append New movie into the list
    new_movie = {'title':'Twilight','genre':'romance'}  
    personal_info['movies'].append(new_movie)

    #Add a tuple of new pizza topings
    new_pizza_topings_1 = input("Enter Your first favourite pizza topings:")
    new_pizza_topings_2 = input("Enter Your Secondonine favourite pizza topings:")

    new_pizza_topings = (new_pizza_topings_1,new_pizza_topings_2)
    add_pizza_topings(personal_info,new_pizza_topings)

    #Print the Personal Information line 1
    print_line1(personal_info)

    
    #Print the Personal Information line 2
    print_line2(personal_info)

    #Print The line 3
    print_line3(personal_info)

    #Print The line 4
    print_line4(personal_info)

def add_pizza_topings(info,topings):

    """
        Add tuple of toppings into data stracture
    """

    for pizza_info in topings:
        info['pizza_toppings'].append(pizza_info)

def print_line1(info):
    
    line1 = 'Hi Joe, my name is ' + info['name'] + ',' + ' and my student ID is ' + str(info['student_id'])+ '.'
    print(line1)

def print_line2(info):
    
    line2 = 'My Ideal pizza has '

   
    for i,g in enumerate(info['pizza_toppings']):
        
        line2+=g

        if i< 3:
            line2+=', '

        elif i == 4:
            line2+=' and '
        elif i==5:
            line2+='.'
    print(line2)

def print_line3(info):

    line3 = 'I like to watch '

    for i,g in enumerate(info['movies']):
        
        line3+=g['genre']

        if i< len(info['movies'])-1:
            line3+=', '

        else:
            line3+=' movies.'
    
    print(line3)

def print_line4(info):
    
    line4 = 'Some of my favourites are '

    for i,g in enumerate(info['movies']):
        
        line4+=g['title']

        if i< len(info['movies'])-1:
            line4+=', '

        else:
            line4+='!'
    
    print(line4)
main()