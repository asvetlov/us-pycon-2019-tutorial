import aiohttp
from aioresponses import aioresponses


async def test_request() -> None:
    with aioresponses() as mocked:
        mocked.get("http://example.com", status=200, body="test")
        session = aiohttp.ClientSession()
        resp = await session.get("http://example.com")

        assert resp.status == 200
        assert "test" == await resp.text()
