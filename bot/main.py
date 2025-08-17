import aiohttp


async def get_pussy_pic():
    async with aiohttp.ClientSession() as session:
        id_url = 'https://cataas.com/cat?json=true'
        async with session.get(id_url) as request:
            response = await request.json()
            pic_id = response.get('id')
        return pic_id