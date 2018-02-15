class MemberStore:
    members = []
    last_id = 1

    def add(self, member):
        member.id = MemberStore.last_id

        MemberStore.members.append(member)

        MemberStore.last_id += 1

    def get_all(self):
        return MemberStore.members

    def get_by_id(self, id):
        for member in MemberStore.members:
            if id == member.id:
                return member
        return None


class PostStore:
    posts = []
    last_id = 1

    def add(self, post):
        post.id = PostStore.last_id

        PostStore.posts.append(post)

        PostStore.last_id += 1

    def get_all(self):
        return PostStore.posts

    def get_by_id(self, id):
        for post in PostStore.posts:
            if id == post.id:
                return post
        return None
