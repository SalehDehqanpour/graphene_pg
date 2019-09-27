import graphene
import graphql_jwt

import links.schema
import users.schema


class Mutation(users.schema.Mutation, links.schema.Mutation, graphene.ObjectType,):
    token_auth = graphql_jwt.ObtainJSONWebToken.Field()
    verify_token = graphql_jwt.Verify.Field()
    refresh_token = graphql_jwt.Refresh.Field()

class Query(users.schema.Query,links.schema.Query, graphene.ObjectType):
    pass


schema = graphene.Schema(query=Query, mutation=Mutation)



# examples of mutations
# mutation {
#   tokenAuth(username: "saleh", password: "123") {
#     token
#   }
# }





# mutation{
#     verifyToken(token:"eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VybmFtZSI6InNhbGVoIiwiZXhwIjoxNTY5NjExODE2LCJvcmlnSWF0IjoxNTY5NjExNTE2fQ.uccoMbCR9nm_K1_6-enkecqHWtEkfsN3Sn-p0zpM18o"){
#         payload
#     }
# }
# in response:
# {
#     "data": {
#         "verifyToken": {
#             "payload": {
#                 "username": "saleh",
#                 "exp": 1569611816,
#                 "origIat": 1569611516 # "originally issued at "
#             }
#         }
#     }
# }

