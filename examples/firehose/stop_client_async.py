import asyncio

from atproto.firehose import (
    AsyncFirehoseSubscribeReposClient,
    parse_subscribe_repos_message,
)

_STOP_AFTER_SECONDS = 3


async def main():
    client = AsyncFirehoseSubscribeReposClient()

    async def on_message_handler(message):
        print(message.header, parse_subscribe_repos_message(message))

    async def _stop_after_n_sec():
        await asyncio.sleep(_STOP_AFTER_SECONDS)
        await client.stop()

    # save ref to task to eliminate problems with GC
    _ = asyncio.create_task(_stop_after_n_sec())

    await client.start(on_message_handler)

    print(f'Successfully stopped after {_STOP_AFTER_SECONDS} seconds!')


if __name__ == '__main__':
    # use run() for a higher Python version
    asyncio.get_event_loop().run_until_complete(main())
