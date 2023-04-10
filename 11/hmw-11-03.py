# Написати власний менеджер контексту, задачею якого буде друкувати "==========" –
# 10 знаків дорівнює перед виконанням коду та після виконання коду,
# таким чином виділяючи блок коду символами дорівнює.
#
# У випадку виникнення будь-якої помилки вона має бути надрукована текстом, проте
# програма не має завершити своєї роботи.

class CtxManager:
    def __enter__(self):
        print('=' * 10)

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type is not None:
            print(f'The error with the name "{exc_val}" occurred')
        print('=' * 10)
        return True


with CtxManager() as manager:
    print('Here\'s happening some code')
    print(1/0)
