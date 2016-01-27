from django.contrib import admin
from books.models import Publisher, Author, Book
class AuthorAdmin(admin.ModelAdmin):
	list_display = ('first_name','last_name','email')
	search_fields = ('first_name','last_name','email')

class BookAdmin(admin.ModelAdmin):
	list_display = ('title','publication_date','publiser',)
	list_filter = ('publication_date',)
	fields = ('title','publication_date','authors','publiser')
	filter_horizontal = ('authors',)
	raw_id_fields = ('publiser',)


admin.site.register(Publisher)
admin.site.register(Author,AuthorAdmin)
admin.site.register(Book,BookAdmin)