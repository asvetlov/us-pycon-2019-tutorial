import asyncio
import functools
from contextlib import asynccontextmanager
from dataclasses import dataclass
from typing import Any, AsyncIterator, Awaitable, Callable, List, Optional

import aiohttp
import click
from yarl import URL


@dataclass(frozen=True)
class Post:
    id: int
    owner: str
    editor: str
    title: str
    text: Optional[str]

    def pprint(self) -> None:
        click.echo(f"Post {self.id}")
        click.echo(f"  Owner:  {self.owner}")
        click.echo(f"  Editor: {self.editor}")
        click.echo(f"  Title:  {self.title}")
        if self.text is not None:
            click.echo(f"  Text:   {self.text}")


class Client:
    def __init__(self, base_url: URL, user: str) -> None:
        self._base_url = base_url
        self._user = user
        self._client = aiohttp.ClientSession(raise_for_status=True)

    async def close(self) -> None:
        return await self._client.close()

    def _make_url(self, path: str) -> URL:
        return self._base_url / path

    async def create(self, title: str, text: str) -> Post:
        async with self._client.post(
            self._make_url("api"),
            json={"owner": self._user, "title": title, "text": text},
        ) as resp:
            ret = await resp.json()
            return Post(**ret["data"])

    async def get(self, post_id: int) -> Post:
        async with self._client.get(self._make_url(f"api/{post_id}")) as resp:
            ret = await resp.json()
            return Post(**ret["data"])

    async def delete(self, post_id: int) -> None:
        async with self._client.delete(self._make_url(f"api/{post_id}")) as resp:
            resp  # to make linter happy

    async def update(
        self, post_id: int, title: Optional[str] = None, text: Optional[str] = None
    ) -> Post:
        json = {"editor": self._user}
        if title is not None:
            json["title"] = title
        if text is not None:
            json["text"] = text
        async with self._client.patch(
            self._make_url(f"api/{post_id}"), json=json
        ) as resp:
            ret = await resp.json()
            return Post(**ret["data"])

    async def list(self) -> List[Post]:
        async with self._client.get(self._make_url(f"api")) as resp:
            ret = await resp.json()
            return [Post(text=None, **item) for item in ret["data"]]


@dataclass(frozen=True)
class Root:
    base_url: URL
    user: str
    show_traceback: bool

    @asynccontextmanager
    async def client(self) -> AsyncIterator[Client]:
        client = Client(self.base_url, self.user)
        try:
            yield client
        finally:
            await client.close()


def async_cmd(func: Callable[..., Awaitable[None]]) -> Callable[..., None]:
    @functools.wraps(func)
    def inner(root: Root, **kwargs: Any) -> None:
        try:
            return asyncio.run(func(root, **kwargs))
        except Exception as exc:
            if root.show_traceback:
                raise
            else:
                click.echo(f"Error: {exc}")

    inner = click.pass_obj(inner)
    return inner


@click.group()
@click.option("--base-url", type=str, required=True)
@click.option("--user", type=str, default="Anonymous")
@click.option("--show-traceback", is_flag=True, default=False)
@click.pass_context
def main(ctx: click.Context, base_url: str, user: str, show_traceback: bool) -> None:
    """REST client for tutorial server"""
    ctx.obj = Root(URL(base_url), user, show_traceback)


@main.command()
@click.argument("title")
@click.argument("text")
@async_cmd
async def create(root: Root, title: str, text: str) -> None:
    async with root.client() as client:
        post = await client.create(title, text)
        click.echo(f"Created post {post.id}")
        post.pprint()


@main.command()
@click.argument("post_id", type=int)
@async_cmd
async def get(root: Root, post_id: int) -> None:
    async with root.client() as client:
        post = await client.get(post_id)
        post.pprint()


@main.command()
@click.argument("post_id", type=int)
@async_cmd
async def delete(root: Root, post_id: int) -> None:
    async with root.client() as client:
        await client.delete(post_id)
        click.echo(f"Post {post_id} is deleted")


@main.command()
@click.argument("post_id", type=int)
@click.option("--text", type=str)
@click.option("--title", type=str)
@async_cmd
async def update(
    root: Root, post_id: int, title: Optional[str], text: Optional[str]
) -> None:
    async with root.client() as client:
        post = await client.update(post_id, title, text)
        post.pprint()


@main.command()
@async_cmd
async def list(root: Root) -> None:
    async with root.client() as client:
        posts = await client.list()
        click.echo("List posts:")
        for post in posts:
            post.pprint()


if __name__ == "__main__":
    main()
