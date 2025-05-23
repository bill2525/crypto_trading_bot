import abc

class Strategy(abc.ABC):
    """Abstract trading strategy."""

    @abc.abstractmethod
    async def should_buy(self, *args, **kwargs) -> bool:
        ...

    @abc.abstractmethod
    async def should_sell(self, *args, **kwargs) -> bool:
        ...
