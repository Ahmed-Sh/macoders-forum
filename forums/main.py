from models import Member, Post
from stores import MemberStore, PostStore


member1 = Member("Ahmed", 20)
member2 = Member("Mahmoud", 32)
member3 = Member("Anosa", 20)

post1 = Post("Post1", "Content1")
post2 = Post("Post2", "Content2")
post3 = Post("Post3", "Content3")
post4 = Post("Post4", "Content4")

# Member Store

member_store = MemberStore()

member_store.add(member1)
member_store.add(member2)
member3.id = 2
member_store.update(member3)

print(member_store.get_all())
print(member_store.get_by_id(2))

# Post Store

post_store = PostStore()

post_store.add(post1)
post_store.add(post2)
post_store.add(post3)

post_store.delete(1)

print(post_store.get_all())
print(post_store.get_by_id(2))
print(post_store.entity_exists(post4))
