import abc

from winter.core import get_injector
from .interceptor import InterceptorRegistry
from .interceptor import interceptor_registry


class Configurer(abc.ABC):
    @abc.abstractmethod
    def add_interceptors(self, registry: InterceptorRegistry):
        pass


def run_configurers():
    injector = get_injector()
    for configurer_class in Configurer.__subclasses__():
        configurer = injector.get(configurer_class)
        configurer.add_interceptors(interceptor_registry)
