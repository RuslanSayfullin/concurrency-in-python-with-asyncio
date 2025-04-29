# Ручное управление транзакцией
import asyncio
import asyncpg
from asyncpg.transaction import Transaction

async def main():
    connection = await asyncpg.connect(host='127.0.0.1',
                                        port=5432,
                                        user='postgres',
                                        database='products',
                                        password='password')
    # Создать экземпляр транзакции
    transaction: Transaction = connection.transaction()
    # Начать транзакцию
    await transaction.start()

    try:
        await connection.execute("INSERT INTO brand "
                                    "VALUES(DEFAULT, 'brand_1')")
        await connection.execute("INSERT INTO brand "
                                    "VALUES(DEFAULT, 'brand_2')")
    
    except asyncpg.PostgresError:
        print('Ошибка, транзакция откатывается!')
        await transaction.rollback()    # Если было исключение, откатить
    else:
        print('Ошибки нет, транзакция фиксируется!')
        await transaction.commit()      # Если исключения не было, зафиксировать
    
    query = """SELECT brand_name FROM brand
                WHERE brand_name LIKE 'brand%'"""
    brands = await connection.fetch(query)
    print(brands)
    
    await connection.close()
    
asyncio.run(main())