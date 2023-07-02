from drf_spectacular.extensions import OpenApiAuthenticationExtension
from knox.auth import TokenAuthentication

class KnoxTokenAuthenticationExtension(OpenApiAuthenticationExtension):
    target_class = TokenAuthentication  # Specify the target authentication class

    def get_security_definition(self, auto_schema):
        return {
            'type': 'apiKey',
            'in': 'header',
            'name': 'Authorization',
            'description': 'Token-based authentication',
        }
