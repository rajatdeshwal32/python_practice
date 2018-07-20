birthdays = {'raman': '19/05/1989', 'rohit': '10/09/1985',
              'manish': '13/04/1993', 'neha': '01/07/1991', 
              'rajat': '01/11/1995'}

name = input("enter the name who's birthday you are looking for : ")
if name in birthdays:
    print('{} birthday is on {}'.format(name, birthdays[name]))
else:
    print('Sorry, we don''t have birthday saved.'.format(name))
