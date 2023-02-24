import graphene
import graphql_jwt

import links.schema


# From the tutorial it is written that in the hackernews/schema.py we import import users.schema and I think this might be the problem. Try importing the user schema this way instead ---from .users import schema--- and reference it in both the Query and Mutation class as ---schema.Query--- and ---schema.Mutation---

# import users.schema

from .users import schema as usersSchema


class Query(usersSchema.Query, links.schema.Query, graphene.ObjectType):
    pass


class Mutation(usersSchema.Mutation, links.schema.Mutation, graphene.ObjectType,):
    token_auth = graphql_jwt.ObtainJSONWebToken.Field()
    verify_token = graphql_jwt.Verify.Field()
    refresh_token = graphql_jwt.Refresh.Field()


schema = graphene.Schema(query=Query, mutation=Mutation)
