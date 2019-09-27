import graphene
from graphene_django import DjangoObjectType

from .models import Link


class LinkType(DjangoObjectType):
    class Meta:
        model = Link


class Query(graphene.ObjectType):
    links = graphene.List(LinkType)

    def resolve_links(self, info, **kwargs):
        return Link.objects.all()


# query {
#   links {
#     id
#     url
#   }
# }


######################################################################################


# 1: Defines a mutation class. Right after, you define the output of the mutation, ...
# the data the server can send back to the client. The output is defined field by field for ...
# learning purposes. In the next mutation you’ll define them as just one.
class CreateLink(graphene.Mutation):
    id = graphene.Int()
    url = graphene.String()
    description = graphene.String()

    # 2 Defines the data you can send to the server, in this case, the links’ url and description.

    class Arguments:
        url = graphene.String()
        description = graphene.String()

    # 3 Actual resolve happen here
    # the server returns the CreateLink class with the data just created. See how this matches the parameters set on #1.
    def mutate(self, info, url, description):
        link = Link(url=url, description=description)
        link.save()

        # here you should pass argument as they expresses in #1 section
        return CreateLink(
            id=link.id,
            url=link.url,
            description=link.description,
        )


class Mutation(graphene.ObjectType):
    create_link = CreateLink.Field()

# mutation hello{
#   createLink(url: "http://snn.ir", description: "salam snn") {
#     id
#   }
# }
