# Обработка ошибки в транзакции
import asyncio
import logging
import asyncpg

async def main():
    connection = await asyncpg.connect(host='127.0.0.1',
                                        port=5432,
                                        user='postgres',
                                        database='products',
                                        password='password')
    try:
        async with connection.transaction():
            insert_brand = "INSERT INTO brand VALUES(9999, 'big_brand')"
            await connection.execute(insert_brand)
            # Команда insert завершится неудачно из-за дубликата первичного ключа
            await connection.execute(insert_brand)
    except Exception:
        logging.exception('Ошибка при выполнении транзакции')
    finally:
        # Если было исключение, протоколировать ошибку
        query = """SELECT brand_name FROM brand WHERE brand_name LIKE 'big_%'"""
        # Выбрать марки и убедиться, что ничего не вставлено
        brands = await connection.fetch(query)
        print(f'Результат запроса: {brands}')
        await connection.close()

asyncio.run(main())