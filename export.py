from sqlalchemy import MetaData, Table, select, func
from pprint import pprint

meta = MetaData(bind='sqlite:///blog.db')
meta.reflect()

posts = meta.tables['posts']
tags = meta.tables['tags']
post_tags = meta.tables['post_tags']

query = select([
    posts.c.title,
    posts.c.slug,
    posts.c.pub_date,
    posts.c.text,
    func.group_concat(tags.c.name, ', ').label('tags')
],
from_obj=posts.outerjoin(post_tags).outerjoin(tags)).group_by(posts.c.slug)
print query
for post in meta.bind.execute(query):
    filename = post.slug.split('/')[-1] + '.rst'

    with open('post/' + filename, 'w') as f:
        f.writelines([
            post.title, '\n',
            '='*len(post.title), '\n\n',
        ])
        f.write(':date: %s\n' % (post.pub_date.date(),))
        if post.tags:
            f.write(':tags: ' + post.tags + '\n')

        f.write('\n\n')
        f.write(str(post.text))
    print post.pub_date.date(), post.slug

