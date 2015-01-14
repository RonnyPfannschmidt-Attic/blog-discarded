from sqlalchemy import MetaData, Table, select
from pprint import pprint

meta = MetaData(bind='sqlite:///blog.db')
meta.reflect()

posts = meta.tables['posts']
tags = meta.tables['tags']
post_tags = meta.tables['post_tags']
def get_tags(post):
    query = select([tags.c.name], from_obj=tags.join(post_tags)). \
                where(post_tags.c.post_id == post.post_id)
    return ', '.join(x[0] for x in query.execute())


for post in posts.select().execute():
    filename = post.slug.split('/')[-1] + '.rst'

    with open('post/' + filename, 'w') as f:
        f.writelines([
            post.title, '\n',
            '='*len(post.title), '\n\n',
        ])
        f.write(':date: %s\n' % (post.pub_date.date(),))
        if get_tags(post):
            f.write(':tags: ' + get_tags(post) + '\n')

        f.write('\n\n')
        f.write(str(post.text))
    print post.pub_date.date(), post.slug

