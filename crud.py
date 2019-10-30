import requests

class crud():
    def __init__(self, base_url = 'http://pulse-rest-testing.herokuapp.com/',
                   book_data1 = {'title': 'Происхождение видов', 'author': 'Чарльз Дарвин'},
                   book_data2 = {'title': 'Война миров', 'author': 'Герберт Уэллс'}):
        self.base_url = base_url
        self.book_data1 = book_data1
        self.book_data2 = book_data2
        self.book_id = None

    def create(self):
        create = requests.post(self.base_url + 'books/', self.book_data1)
        self.book_id = create.json()['id']
        return create.json()

    def read(self):
        read = requests.get(self.base_url+'books/' + str(self.book_id) + '/')
        return read.json()

    def update(self):
        update = requests.put(self.base_url+'books/' + str(self.book_id) + '/', self.book_data2)
        return update.json()

    def delete(self):
        delete = requests.delete(self.base_url + 'books/' + str(self.book_id))
        return delete.status_code


    def debug_printer(self):

        print ('create', self.create())
        print('read', self.read())
        print('update', self.update())
        print('delete', self.delete())

if __name__ == '__main__':
    a = crud()
    a.create()
    a.read()
    a.update()
    a.delete()
    a.debug_printer()


# base_url = 'http://pulse-rest-testing.herokuapp.com/'
# data1 = {'title':'Происхождение видов', 'author':'Чарльз Дарвин'}
#
# r_post = requests.post(base_url+'books/', data1) #Создаём книгу POST /books/, вы запоминаете его id.
# id = r_post.json()['id']
# print(id)
#
# r_get = requests.get(base_url+'books/' + str(id) + '/') #Проверяете, что она создалась и доступна по ссылке GET/books/[id]
# print(r_post.json())
# print(r_post.json() == r_get.json())
# print(r_post.json()['title'] == 'Происхождение видов')
# print(r_post.json()['author'] == 'Чарльз Дарвин')
# print(r_get.json()['id'] == r_post.json()['id'])
#
# r_get_all_books = requests.get(base_url+'books/') #Проверяете, что она есть в списке книг по запросу GET /books/
# print(r_post.json() in r_get_all_books.json())
#
# put_data =  {'title':'Война миров', 'author':'Герберт Уэллс'}
# r_post1 = requests.put(base_url+'books/' + str(id) + '/', put_data)       #Изменяете данные этой книги методом PUT /books/[id]/
# print(r_post1.status_code)
#
# r_get1 = requests.get(base_url+'books/' + str(id) + '/') #Проверяете, что она изменилась и доступна по ссылке /books/[id]
# print(r_get1.status_code)
# print(r_get1.json())
# print(r_post1.json() == r_get1.json())
# print(r_get1.json()['title'] == 'Война миров')
# print(r_get1.json()['author'] == 'Герберт Уэллс')
# print(r_get1.json()['id'] == r_post1.json()['id'])
#
#
# r_get_all_books_2 = requests.get(base_url+'books/') # Проверяете, что она есть в списке книг по GET /books/ с новыми данными.
# print(r_post1.json() in r_get_all_books_2.json())
#
# r_delete = requests.delete(base_url+'books/' + str(id)) # Удаляете эту книгу методом DELETE /books/[id].
# r_get_deleted = requests.get(base_url + 'books/' + str(id) + '/')
# print(r_get_deleted.status_code)