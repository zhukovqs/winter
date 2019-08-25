from rest_framework.request import Request

from .request_body import RequestBodyAnnotation
from .response_header import ResponseHeaders
from .. import ArgumentResolver
from .. import converters
from ..core import ComponentMethodArgument


class RequestBodyArgumentResolver(ArgumentResolver):

    def is_supported(self, argument: ComponentMethodArgument) -> bool:
        annotation = argument.method.annotations.get_one_or_none(RequestBodyAnnotation)
        if annotation is None:
            return False
        return annotation.argument_name == argument.name

    def resolve_argument(self, argument: ComponentMethodArgument, request: Request, response_headers: ResponseHeaders):
        return converters.convert(request.data, argument.type_)
