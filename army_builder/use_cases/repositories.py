from typing import Protocol

from army_builder.domain.army import Army


class RepositoryError(Exception):
    """The base error raised by the repo"""


class ArmyNotFoundError(RepositoryError):
    """Raied when an army is not found"""


class ArmyStorageError(RepositoryError):
    """Raised when any sort of storage error is encountered"""


class ArmyReaderRepo(Protocol):
    def list(self) -> list[Army]:
        """
        _Summary_: Returns a list of the armies stored in the repo
        _Raises_: ArmyStorageError
        """

    def get_army_by_name(self, army_name: str) -> Army: ...


class ArmyWriterRepo(Protocol):
    def delete(self, army: Army) -> None:
        """Delete the army from storage

        :raises ArmyStorageError: if the underlying store fails.
        :raises ArmyNotFoundError: if the army does not exist in storage
        """

    def save(self, army: Army) -> None:
        """Save the army to storage. Silently overwrites existing armies.

        :raise ArmyStorageError: if the army could not be saved to storage.
        """
