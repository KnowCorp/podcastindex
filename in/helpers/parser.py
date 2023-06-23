import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()


def read_response(map: dict):
    parsed_map: dict = {}

    for key, value in map.items():
        logger.info(key, value)
        parsed_map[key] = value

        if isinstance(value, dict):
            read_response(value)

        elif isinstance(value, list):
            for item in value:
                if isinstance(item, dict):
                    read_response(item)

        else:
            logger.info(f"{key} : {value}")
            parsed_map[key] = value

    return parsed_map
