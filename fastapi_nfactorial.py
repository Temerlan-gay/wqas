from fastapi import FastAPI

app = FastAPI()


def factorial(n):
    result = 1

    for i in range(1, n + 1):
        result *= i

    return result


@app.get("/{num}")
def get_factorial(num: int):
    return {"nfactorial": factorial(num)}