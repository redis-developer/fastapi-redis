from aioredis import Redis


class MoleculesRepository:
    """Stores and Retrieves chemical molecules from Redis Hash"""

    def __init__(self, redis: Redis):
        self._redis = redis

    async def set_multiple(self, key: str, smiles: dict):
        """
        Set multiple hash fields to multiple values.
        dict can be passed as first positional argument:
        Hash field is molecule canonical representation
        Hash value is molecule type i.e. SMILES.

        :param key:
        :param smiles:
        :return:
        """
        return await self._redis.hmset_dict(key, smiles)

    async def len(self, key: str):
        """
        Get the number of fields in a given hash.

        :param key:
        :return: int:
        """
        return await self._redis.hlen(key)

    async def get_all(self, key: str):
        """

        :param key:
        :return: dict:
        """
        return await self._redis.hgetall(key)
