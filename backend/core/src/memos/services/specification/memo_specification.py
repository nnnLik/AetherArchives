from src.core.utils import SingletonMeta


class MemoSpecification(metaclass=SingletonMeta):
    @staticmethod
    def is_satisfied(
        title: str,
        description: str,
        body: str,
    ) -> bool:
        return (len(title) < 100) or (len(description) < 250) or (title or body)
