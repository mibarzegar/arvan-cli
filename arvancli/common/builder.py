from argparse import _SubParsersAction
class Builder:
    def __init__(self, subparsers: _SubParsersAction, builders_dict: dict) -> None:
        self._service_builders = builders_dict
        self._parsers = {}
        self._subparsers = {}
        self._parent_subparsers = subparsers
        self._build_parsers()
    def _build_parsers(self)  -> None:
        for service in self._service_builders:
            self._parsers[service] = self._parent_subparsers.add_parser(service)
            self._subparsers[service] = self._parsers[service].add_subparsers()
    def _service_registrar(self) -> None:
        for service in self._service_builders:
            self._provider.register_builder(service, self._service_builders[service](self._subparsers[service]))
