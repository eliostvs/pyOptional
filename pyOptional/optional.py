from typing import TypeVar, Generic, Any, Union, Callable

from .exceptions import NoneValueError

T = TypeVar('T')


class Optional(Generic[T]):
    def __init__(self, value: T) -> None:
        self._value = value

    def get(self) -> T:
        if self._value is None:
            raise NoneValueError('Called get on empty optional')
        return self._value

    def get_or_else(self, default: Any) -> Union[T, Any]:
        try:
            return self.get()
        except NoneValueError:
            return default

    def get_or_else_get(self, default_callable: Callable[[], Any]) -> Union[T, Any]:
        try:
            return self.get()
        except NoneValueError:
            return default_callable()

    def get_or_raise(self, exception, *args, **kwargs) -> Union[T, Exception]:
        if self._value is None:
            raise exception(*args, **kwargs)
        else:
            return self._value

    def map(self, transform_callable: Callable[[T], Any]) -> Union['Optional[None]', Any]:
        if self._value is None:
            return type(self)(None)
        else:
            return type(self)(transform_callable(self._value))

    def flat_map(self, transform_callable: Callable[[T], Any]) -> Union['Optional[None]', Any]:
        if isinstance(self._value, type(self)):
            return self._value.flat_map(transform_callable)
        else:
            return type(self)(self._value).map(transform_callable)

    def if_present(self, func: Callable[[T], None]) -> None:
        if self._value is not None:
            func(self._value)

    def is_present(self) -> bool:
        return self._value is not None

    def __bool__(self):
        return self.is_present()

    def __nonzero__(self) -> bool:
        return self.__bool__()

    def __str__(self) -> str:
        if self._value is None:
            return 'Optional empty'
        else:
            return 'Optional of: {}'.format(self._value)

    def __repr__(self) -> str:
        return 'Optional({})'.format(repr(self._value))

    def __eq__(self, o: object) -> bool:
        return isinstance(o, Optional) and o._value == self._value

    def __ne__(self, o: object) -> bool:
        return not self.__eq__(o)

    @staticmethod
    def empty() -> 'Optional':
        return Optional(None)
