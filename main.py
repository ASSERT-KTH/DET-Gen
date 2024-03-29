import argparse
from src.code_runner import CodeRunner
import logging
from datetime import datetime

logging.basicConfig(filename='logging_{:%Y-%m-%d}.log'.format(datetime.now()),
                    filemode='a',
                    format='%(asctime)s,%(msecs)d %(name)s %(levelname)s %(message)s',
                    datefmt='%H:%M:%S',
                    level=logging.INFO)


def get_args():
    parser = argparse.ArgumentParser()

    parser.add_argument(
        "-f",
        "--is_func",
        default=True,
        help="Run the function runner",
        required=False,
    )

    parser.add_argument(
        "-q",
        "--is_qb",
        default=False,
        help="Run the QuixBugs runner",
        required=False,
    )

    parser.add_argument(
        "-i",
        "--is_iterative",
        default=True,
        help="Run the iterative runner",
        required=False,
    )

    parser.add_argument(
        "-mc",
        "--meta_data_config",
        choices=["BA", "BAD", "BADT"],
        default="BADT",
        help="Config for meta data",
        required=False,
    )

    args = parser.parse_args()

    return args.is_func, args.is_qb, args.is_iterative, args.meta_data_config


def main() -> None:

    (is_func, is_qb, is_iterative, meta_data_config) = get_args()

    logging.info(f"Running with is_func: {is_func}, is_qb: {is_qb}, is_iterative: {is_iterative}, meta_data_config: {meta_data_config}")

    code_runner = CodeRunner(is_func, is_qb, is_iterative, meta_data_config)
    code_runner.run()


if __name__ == "__main__":
    main()
