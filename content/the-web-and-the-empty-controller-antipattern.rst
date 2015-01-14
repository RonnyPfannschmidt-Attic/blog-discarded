the web and the empty-controller antipattern
============================================

:date: 2008-01-09
:tags: python, web, ruby, antipattern


There is an annoying trend in web-frameworks for dynamic languages.

They group functions which don't share any related data in classes like this:

<pre syntax="python">
class ToolkitController(BaseController):

    def index(self):
        return render('/toolkit/index.html')

    def blog_add(self):
        return render('/toolkit/add.html')

    def blog_add_process(self):
        newpost = BlogEntry(**request.params)
        Session.save(newpost)
        Session.commit()
        redirect_to(controller="blog", action="index")
</pre>
or this:
<pre syntax="ruby">
class ContactsController < ApplicationController
  def list
    @contacts = Contact.find_all
  end
  def show
    @contact = Contact.find(@params['id'])
  end
  def create
    @contact = Contact.new(@params['contact'])
    if @contact.save
      flash['notice'] = 'Contact was successfully created.'
      redirect_to :action => 'list'
    else
      render_action 'new'
    end
  end
end
</pre>

Attentive readers will notice - these methods share no data, which means there is no reason for coupling them as strong as a class does.