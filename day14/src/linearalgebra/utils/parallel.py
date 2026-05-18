import time
import pandas as pd
from linearalgebra.configurations.conf import Config


def sequential_tax_calculator(product_path):
    products = pd.read_csv(product_path)

    start_time = time.time()
    tax_array = []

    for cost in products["cost"]:
        tax_array.append(cost * 0.1)

    end_time = time.time()
    print(f"Sequential time: {end_time - start_time:.6f} seconds")

    return tax_array


def vectorized_tax_calculator(product_path):
    products = pd.read_csv(product_path)

    start_time = time.time()

    products["tax"] = products["cost"] * 0.1

    end_time = time.time()
    print(f"Vectorized time: {end_time - start_time:.6f} seconds")

    return products["tax"].tolist()


if __name__ == "__main__":
    product_path = Config.product_path

    sequential_tax_calculator(product_path)
    vectorized_tax_calculator(product_path)